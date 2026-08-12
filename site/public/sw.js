/* Cerebro service worker — network-first so the app always shows the freshest
 * deployed digest/media-zone when online, and falls back to the last-synced
 * copy when offline. Bump CACHE to force old caches out on the next visit. */
const CACHE = 'cerebro-v1';

self.addEventListener('install', () => self.skipWaiting());

self.addEventListener('activate', (event) => {
  event.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)));
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;

  const url = new URL(req.url);
  // Only manage our own origin; let cross-origin (fonts, youtube thumbnails,
  // arxiv, etc.) go straight to the network untouched.
  if (url.origin !== self.location.origin) return;

  event.respondWith((async () => {
    try {
      // Network-first: always try for the freshest content when online.
      const res = await fetch(req);
      if (res && res.ok && res.type === 'basic') {
        const cache = await caches.open(CACHE);
        cache.put(req, res.clone());
      }
      return res;
    } catch (err) {
      // Offline: serve the cached copy, or fall back to the app shell (start page).
      const cached = await caches.match(req);
      if (cached) return cached;
      const shell = await caches.match('./') || await caches.match(new URL('./', self.location).href);
      return shell || new Response('Offline', { status: 503, statusText: 'Offline' });
    }
  })());
});
