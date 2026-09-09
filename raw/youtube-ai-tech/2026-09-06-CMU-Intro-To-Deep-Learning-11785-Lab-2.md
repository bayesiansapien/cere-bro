# CMU Introduction To Deep Learning 11-785, Fall 2026: Lab 2

**Channel:** Carnegie Mellon University Deep Learning
**Published:** 2026-09-06
**Source:** https://www.youtube.com/watch?v=ed74ViuofcY

## TL;DR
A TA-led recitation on systematically debugging neural network code, split between "MyTorch" (a from-scratch NumPy autograd library graded by a hidden autograder) and the applied PyTorch pipeline for frame-level phoneme classification. The technical core is a taxonomy of failure modes in DL code: tolerance failures on numerical closeness tests, silent shape errors that pass a closeness check but produce wrong gradients, and boundary errors between pipeline components. The prescribed method is `ipdb.set_trace()` inside the failing layer rather than print-statement archaeology, plus overfitting a single batch to isolate a forward-pass bug before rerunning a full training loop.

## Key Takeaways
- **Silent errors are the real enemy.** Two of the seeded bugs (`*` instead of `@` for matmul, `np.minimum` instead of `np.maximum` in ReLU forward) produce correctly-shaped tensors with wrong values. Shape assertions alone would not catch either. The autograder shares expected values but deliberately withholds shapes, forcing manual shape derivation.
- **Autograder closeness uses a hard 1e-4 tolerance,** and both compared arrays must pass. Values that "look right" at 3 significant figures still fail. Adding trailing 9s to a guessed value does not converge to the reference.
- **The ReLU backward bug** was multiplying by the wrong mask sign. Backward through ReLU must gate on the *forward* activation being positive, not on the incoming gradient.
- **Debug workflow prescribed:** re-read the writeup first (most bugs are misread specs, not code), derive tensor shapes by hand before writing code, then `ipdb` breakpoints over print statements. Critically, edits made inside the debugger do not persist to the source file, so a passing test inside `ipdb` is a hypothesis, not a fix.
- **Data pipeline mechanics for HW1P2:** utterances are concatenated into one array, each padded with `context` zero-frames at both ends, then sliced into windows of `2*context + 1` frames. Context size is a tunable hyperparameter. Note the deliberate mismatch: the lab notebook uses 27 MFCC features while the actual homework ships 32 log-mel features.
- **Overlapping windows exist for a signal-processing reason, not a linguistic one.** The stated justification is that STFT attenuates energy at frame edges, so a 25 ms frame with a 10 ms stride ensures edge features from frame *n* land mid-frame in *n+1*. A student's guess about neighbouring phoneme context was explicitly rejected.
- **Training-curve triage table:** flat loss with decaying LR means the model is learning nothing (kill it). Fluctuating validation with rising train accuracy means unstable hyperparameters. Both curves tracking but capped at 30% accuracy means underfitting (need a stronger model). Validation loss turning upward means stop at the minimum.
- **HW4 will ship as a Python package, not a notebook.** Tracebacks will originate many frames below the executed cell. Read tracebacks bottom-to-top, and restart the kernel after editing an imported module or you will keep testing the cached old version.

## Architecture & Optimization Mechanics
The pedagogically interesting part is the error-localization strategy, which generalizes directly to production inference debugging. The TA's advice to "fit into one batch or even several samples to narrow down the exact error" instead of rerunning the full pipeline is the same bisection principle used when a quantized model diverges: shrink the input until the failure is deterministic and cheap to reproduce.

The claim that errors concentrate "at the boundary between components" (dataset to dataloader, layer *n* output to layer *n+1* input) is the correct mental model. Interface contracts, not internal math, are where most real pipelines break. In a compression context the analogous boundaries are dequantization scale placement, KV cache layout between prefill and decode, and tensor-parallel shard concatenation.

Two details worth noting for anyone writing custom kernels or quantization code. First, the 1e-4 closeness tolerance is roughly the practical floor for float32 accumulation differences, which is exactly the regime where a fused kernel and a reference NumPy implementation legitimately disagree. Second, the cepstral mean-variance normalization the lab describes (log-transform converts a multiplicative channel distortion into an additive offset, which subtracting the mean then removes) is a clean example of choosing a representation so that a nuisance factor becomes linearly separable. That is the same reasoning behind log-scale activation quantization.

The lab's own data preprocessing is explicitly labelled as a naive reference implementation, with the real handout using `Dataset.__getitem__` and a `DataLoader`. Worth flagging: the naive path materializes every context window, which multiplies memory by `2*context + 1`. The `__getitem__` approach slices lazily from the concatenated array instead. That is a memory-vs-indexing-overhead tradeoff Amit will recognize from dataset streaming for calibration sets.

## Grounded Context (Web Enrichment)
The course structure holds up against the public record. 11-785 has long run six assignments split into an Autolab-graded from-scratch component and a Kaggle-graded applied component, with HW1 specifically being frame-level speech classification and phoneme state labelling on WSJ utterances. The MyTorch-then-PyTorch progression is the course's signature.

The feature-representation detail in the lab is more interesting than it first appears. The TA noted almost in passing that the notebook uses 27-dimensional MFCCs while the current homework uses 32 log-mel features. That is not an arbitrary change. Current practice has moved decisively from MFCCs to log-mel spectrograms for deep learning ASR, because the DCT step in MFCC extraction decorrelates and compresses features specifically to help GMM-HMM systems, discarding structure that a CNN would happily exploit. Recent comparative work reports log-mel at roughly 96.7% accuracy against MFCC at roughly 85.2% on comparable classification tasks, and STFT spectrograms landing between them. The 25 ms frame length the TA drew on the board is the standard local-stationarity window across both feature types. So the course switching its handout to log-mel while leaving the lab notebook on MFCC is a curriculum catching up to the field, and the student confusion about feature counts in the recitation is a direct symptom of that lag.

## Real-World Application / Actionable Step
Steal the failure taxonomy for the compression workflow. When a pruned or quantized model regresses, the debugging order should be: (1) does the tensor shape survive the transform, (2) does the numerical output match the FP16 reference at a *stated* tolerance, and (3) does it match at the *component boundary* rather than only end-to-end. Most quantization regressions are silent-value errors, exactly the class this lab seeds deliberately, and end-to-end perplexity is too coarse a detector.

Concretely, add a per-layer closeness harness to the pruning pipeline: run one fixed calibration batch through the dense and compressed models, capture activations at every module boundary with a forward hook, and report the first layer where relative error exceeds a threshold you pick deliberately (1e-2 for int8, 1e-4 for FP16 passthrough). This turns "the pruned model got worse" into "layer 14's down-projection diverges first," which is actionable. The single-batch bisection principle applies too: never debug a compression bug by rerunning a full eval sweep.

One habit to adopt directly: the observation that debugger-local edits do not persist. When testing a quantization config interactively, the config that made the numbers look right in the REPL is not the config that ships. Write it to the YAML before celebrating.

Sources:
- [11-785 Deep Learning course site](https://deeplearning.cs.cmu.edu/S26/index.html)
- [11-785 course overview](https://www.courses.scottylabs.org/course/11-785)
- [Comparing MFCCs and Spectrograms for ASR](https://apxml.com/courses/applied-speech-recognition/chapter-2-feature-extraction-for-speech/comparing-mfccs-and-spectrograms)
- [Leveraging MFCC and Mel-Spectrogram Representations for Deep Learning-Based Speech Recognition](https://www.mdpi.com/2673-4591/123/1/22)
