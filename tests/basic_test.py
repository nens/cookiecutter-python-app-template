from cookiecutter.main import cookiecutter

import os
import shutil
import subprocess
import sys
import tempfile
import unittest


class BasicTest(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.mkdtemp(prefix="python-template")
        self.cookiecutter_dir = os.getcwd()
        os.chdir(self.tempdir)
        cookiecutter(
            self.cookiecutter_dir,
            no_input=True,
            extra_context={
                "project_name": "my-project"
            },
        )

    def tearDown(self):
        os.chdir(self.cookiecutter_dir)
        shutil.rmtree(self.tempdir)

    def test_smoke(self):
        assert "my-project" in os.listdir()
