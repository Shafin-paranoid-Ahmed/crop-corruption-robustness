# Implementation notes

- Small shared helpers are versioned copies; metrics, splits, checkpoint tensors, prediction CSVs and embedding arrays are kept byte-for-byte as produced by the recorded runs.

- Large frozen embedding arrays are kept in a local bundle (`.artifacts/embeddings-v1.zip`); no release is published. Each consumer checks its required file hashes.

- Quantum training-module imports are lazy inference imports. E3 inference classes are copies of their training definitions with a local VQC import; model state keys and equations are unchanged. `CROP_DATA_ROOT`/`--image-root` selects raw images. The parallel runner interpreter defaults to `.venv`. Frozen baseline inference inputs are local copies.
