import json
import sys
from pathlib import Path

from . import lint_manifest


def main(argv=None):
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) != 1:
        print("Usage: production-manifest-gate <manifest.json>", file=sys.stderr)
        return 2
    try:
        payload = json.loads(Path(args[0]).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"Invalid JSON: {error}", file=sys.stderr)
        return 2
    errors = lint_manifest(payload)
    if errors:
        print("FAIL\n- " + "\n- ".join(errors), file=sys.stderr)
        return 1
    print("PASS: production metadata manifest is releasable")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
