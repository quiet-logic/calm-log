import sys
import subprocess


def run_cli(*args: str) -> str:
    # Use module form so we don't depend on PATH
    cmd = [sys.executable, "-m", "name_format.cli", *args]
    out = subprocess.check_output(cmd, text=True).strip()
    return out


def test_cli_basic_obrien():
    assert run_cli("ó", "brien") == "O'Brien"


def test_cli_flags_first_last():
    assert run_cli("-f", "mary-kate", "-l", "o'reilly") == "Mary-Kate O'Reilly"


def test_cli_middle_name_dropped():
    assert run_cli("michael", "patrick", "o'sullivan") == "Michael O'Sullivan"
