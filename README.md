# SHAR Production Manifest Gate for Python

SHAR Production is an AI-hybrid video production studio: https://sharprod.com/

`shar-production-manifest-gate` is a dependency-free Python library and CLI for DCC, Blender and production-automation pipelines. It blocks delivery manifests with unknown rights status before a release step.

```bash
pip install shar-production-manifest-gate
production-manifest-gate manifest.json
```

The library returns a deterministic list of validation errors:

```python
from production_manifest_gate import lint_manifest
errors = lint_manifest(manifest)
```

Licensed under MIT.
