import json
import subprocess
import sys
import unittest

from production_manifest_gate import lint_manifest


class ManifestGateTests(unittest.TestCase):
    def test_accepts_cleared_delivery_manifest(self):
        self.assertEqual(
            [],
            lint_manifest(
                {
                    "title": "Synthetic delivery",
                    "project": "SHAR demo",
                    "stage": "delivery",
                    "rights_status": "cleared",
                }
            ),
        )

    def test_blocks_unknown_rights_and_invalid_stage(self):
        errors = lint_manifest(
            {"title": "x", "project": "y", "stage": "publish", "rights_status": "unknown"}
        )
        self.assertIn("stage must be one of: preproduction, production, postproduction, delivery", errors)
        self.assertIn("rights_status=unknown is not releasable", errors)

    def test_cli_returns_nonzero_for_unreleasable_manifest(self):
        fixture = "tests/fixtures/unknown.json"
        result = subprocess.run(
            [sys.executable, "-m", "production_manifest_gate", fixture],
            capture_output=True,
            text=True,
        )
        self.assertEqual(1, result.returncode)
        self.assertIn("rights_status=unknown is not releasable", result.stderr)


if __name__ == "__main__":
    unittest.main()
