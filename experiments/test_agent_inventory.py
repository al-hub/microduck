import importlib.util
from pathlib import Path
import unittest

FILE = Path(__file__).resolve().parents[1] / "scripts" / "agent_inventory.py"
spec = importlib.util.spec_from_file_location("agent_inventory", FILE)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class InventoryTests(unittest.TestCase):
    def test_installed_binary_version(self):
        result = module.probe(["python3", "--version"])
        self.assertEqual(result["exit_code"], 0)
        self.assertEqual(result["status"], "ok")
    def test_missing_binary_is_not_success(self):
        result = module.probe(["microduck_nonexistent_294847", "--version"])
        self.assertEqual(result["status"], "unavailable")
    def test_nonzero_exit_is_failure(self):
        result = module.probe(["python3", "-c", "raise SystemExit(3)"])
        self.assertEqual(result["exit_code"], 3)
        self.assertEqual(result["status"], "failed")

if __name__ == "__main__":
    unittest.main()
