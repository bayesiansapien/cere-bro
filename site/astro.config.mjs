import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://bayesiansapien.github.io',
  base: '/cere-bro',
  trailingSlash: 'ignore',
  build: {
    format: 'directory',
  },
});
