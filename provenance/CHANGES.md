# Extraction changes

- New repository entrypoints, dependency records, attribution, source manifests, artifact manifest/fetcher and standalone verifier. Raw datasets, caches, credentials, runtime logs, unrelated tracks and smoke/benchmark-only outputs excluded.

- Small required helpers are frozen copies; metrics, splits, checkpoint tensors, prediction CSVs and embedding arrays are preserved byte-for-byte. Missing historical Markdown links resolve to source-commit permalinks when their targets exist in the parent repository.

- Large frozen embedding arrays are local-only and packaged once in the baseline .artifacts/embeddings-v1.zip local bundle; no release published. Each consumer checks its required file hashes.

- Unconditional quantum training-module imports replaced by lazy inference imports. E3 inference classes copied from their original definitions with a local VQC import; model state keys/equations unchanged. CROP_DATA_ROOT/--image-root selects raw images. Parallel-runner interpreter defaults to .venv. Frozen baseline inference inputs copied locally.
