"""Rights-aware release gating for Python production pipelines."""

STAGES = ("preproduction", "production", "postproduction", "delivery")
RIGHTS = ("cleared", "licensed", "synthetic", "unknown")


def lint_manifest(value):
    """Return deterministic validation errors; an empty list means releasable."""
    if not isinstance(value, dict):
        return ["manifest must be a JSON object"]

    errors = []
    for field in ("title", "project", "stage", "rights_status"):
        if not isinstance(value.get(field), str) or not value[field].strip():
            errors.append(f"{field} is required")
    if value.get("stage") and value["stage"] not in STAGES:
        errors.append("stage must be one of: " + ", ".join(STAGES))
    if value.get("rights_status") and value["rights_status"] not in RIGHTS:
        errors.append("rights_status must be one of: " + ", ".join(RIGHTS))
    if value.get("rights_status") == "unknown":
        errors.append("rights_status=unknown is not releasable")
    return errors
