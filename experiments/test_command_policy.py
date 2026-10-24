import importlib.util
from pathlib import Path
import unittest

spec=importlib.util.spec_from_file_location("policy",Path(__file__).resolve().parents[1]/"scripts"/"command_policy.py")
policy=importlib.util.module_from_spec(spec)
spec.loader.exec_module(policy)

class PolicyTests(unittest.TestCase):
    def test_safe_read_only(self):
        self.assertTrue(policy.validate(["git","status","--short"],"experiments/agent-smoke"))
        self.assertTrue(policy.validate(["python3","-m","unittest","discover"],"experiments/agent-smoke"))
    def test_no_arbitrary_python(self):
        for a in (["python3","-c","print('hello')"],["python3","-m","pip","install","x"]):
            with self.assertRaises(ValueError): policy.validate(a,"experiments/agent-smoke")
    def test_no_openended_agents(self):
        for a in (["opencode","run","--auto"],["agy","--dangerously-skip-permissions"]):
            with self.assertRaises(ValueError): policy.validate(a,"experiments/agent-smoke")
    def test_no_upstream(self):
        with self.assertRaises(ValueError): policy.validate(["git","status"],"upstream/microduck")
    def test_no_git_mutation(self):
        with self.assertRaises(ValueError): policy.validate(["git","reset","--hard"],"experiments/agent-smoke")
    def test_no_git_config_hooks(self):
        with self.assertRaises(ValueError): policy.validate(["git","diff","-c","core.pager=evil"],"experiments/agent-smoke")

if __name__=="__main__": unittest.main()
