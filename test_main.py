import subprocess
from pathlib import Path

import pytest


def get_main_path():
    return Path(__file__).parent / "dnos-kdev"


def run(argv, **kw):
    return subprocess.run(
        [get_main_path()] + argv, text=True, capture_output=True, **kw
    )


def test_run_help():
    proc = run(["--help"])
    assert "Kernel tool for dnos" in proc.stderr
    assert proc.returncode != 0


def test_run_dry():
    proc = run(["--dry-run", "kpatch-build"])
    assert "DRY: docker build" in proc.stderr
    assert "DRY: docker run" in proc.stderr
    assert proc.returncode == 0


def test_build_focal():
    subprocess.run(["docker", "build", "./ubuntu-focal-docker"], check=True)


def test_build_bionic():
    subprocess.run(["docker", "build", "./ubuntu-bionic-docker"], check=True)
