"""Tests for the dedicated MCP test-dispatch API."""
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location("dev_tasks", Path(__file__).resolve().parents[1] / "tools/mcp/dev_tasks.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class DedicatedTests(unittest.TestCase):
    def test_unknown_id_fails_closed(self):
        r = module.run_registered_test("shell")
        self.assertFalse(r["ok"])
        self.assertEqual(r["error"], "unknown task id")
    def test_not_allowed_to_pass_arguments(self):
        r = module.run_registered_test("inventory_tests;echo dangerous")
        self.assertFalse(r["ok"])
    def test_fixed_inventory(self):
        r = module.run_registered_test("inventory_tests")
        self.assertTrue(r["ok"], r)
        self.assertEqual(r["exit_code"], 0)

if __name__ == "__main__":
    unittest.main()
