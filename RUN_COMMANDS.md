# Current standalone runbook

Run from this repository root in native Windows PowerShell. The commands below
are examples for manual use; extraction does not launch training or regenerate data.

## Environment

Create a Python 3.10 environment and select an appropriate PyTorch wheel for your machine.
The source environment used torch 2.11.0+cu128 and torchvision 0.26.0+cu128;
the portable requirements omit the CUDA suffix. The original pins are preserved in
`provenance/source-requirements.txt`.

```powershell
py -3.10 -m venv .venv
$PY = Join-Path $PWD '.venv/Scripts/python.exe'
& $PY -m pip install -r requirements.txt
& $PY scripts/verify.py
```

For E3 evaluation also install `requirements-quantum.txt`. Classical evaluation does not require PennyLane.

## Frozen embedding inputs

The Git checkout includes the small checkpoints and CSV evidence. Large NPZ inputs
are excluded from Git. Sign in with GitHub CLI (`gh auth login`) using an account with
access to the private baseline repository, then run:

```powershell
& $PY scripts/fetch_artifacts.py --download
& $PY scripts/verify.py --artifacts
```

Alternatively, copy verified inputs from a baseline checkout that already has them:

```powershell
& $PY scripts/fetch_artifacts.py --from-directory ../crop-multimodal-baselines
```

The helper refuses to overwrite differing artifacts and validates SHA-256.
It copies only paths listed in ARTIFACTS.json, without extracting arbitrary archive paths.
Raw datasets are separate inputs and are not included in this release.

## Reproduction examples

Use new run names and output directories when rerunning. Do not overwrite archived
results or manually promote a new model to canonical without an explicit decision.
The validation split selects checkpoints; the test set is not a tuning target.

Read `corruption_study/results/THESIS_STYLE_ROBUSTNESS_REPORT.md` and
`corruption_study/results/E3_CORRUPTION_EXTENSION_SUMMARY.md` for archived findings.

```powershell
& $PY corruption_study/gen/corrupt_images.py --help
& $PY corruption_study/gen/corrupt_iot.py --help
& $PY corruption_study/gen/regen_embeddings.py --help
& $PY corruption_study/eval/run_corruption_eval.py --help
& $PY corruption_study/eval/bootstrap_difference_of_drops.py --help
& $PY scripts/verify.py --artifacts
# Optional quantum wiring verification:
& $PY scripts/verify.py --quantum --artifacts
```

The evaluator's `--image-root` or `CROP_DATA_ROOT` selects raw TEST images. Fixed
manifests remain local. `--iot-features` and `--embedding-dir` select corrupted inputs.
Generation tools take explicit input/output directories; point their outputs into
`corruption_study/data/`, which is Git-ignored. Existing condition names would overwrite
archived results, so choose distinct names for new evaluations.

The parallel E3 runner defaults to `.venv/Scripts/python.exe`. Its `-CleanE3Outputs`
switch deletes existing outputs and is not part of this extraction or verification.
The root verifier reads saved results without rerunning inference or bootstrap draws.
