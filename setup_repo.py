import os, sys, pathlib, re, tomllib
from pathlib import Path

root = Path.home() / "Documents" / "code_playground"
pkg_root = root / "name_format_pkg"
pkg_mod = pkg_root / "name_format"
pyproject = pkg_root / "pyproject.toml"
readme_root = root / "README.md"
req_dev = root / "requirements-dev.txt"
makefile = root / "Makefile"
tools_dir = root / "tools"
bump_py = tools_dir / "bump_version.py"
init_py = pkg_mod / "__init__.py"

print("✅ Running repo setup in", root)

# 1) README
readme_root.write_text("""# calm-log & name-format

This repo contains two small learning/portfolio projects.

## 1) `name-format` (installable package + CLI)
A robust personal-name formatter handling:
- Irish O'/Ó
- Mc/Mac
- Initials
- Hyphens
- Particles (de/van/von)

### CLI usage:
python3 -m name_format.cli "ó brien"
namefmt "mary-kate o'reilly"

### Tests
make test
""")

print("✅ README updated")

# 2) Format + lint config
data = tomllib.loads(pyproject.read_text())
tool = data.setdefault("tool", {})
tool["black"] = {"line-length": 88, "target-version": ["py310"]}
tool["ruff"] = {"line-length": 88, "target-version": "py310", "select": ["E","F","I","UP","B","SIM"], "ignore": []}
data["project.scripts"] = {"namefmt": "name_format.cli:main"}

import tomli_w
pyproject.write_text(tomli_w.dumps(data))
print("✅ Added Black/Ruff & console script")

# 3) Version exposure
init_txt = init_py.read_text()
if "__version__" not in init_txt:
    init_py.write_text(init_txt + """

try:
    from importlib.metadata import version
    __version__ = version('name-format')
except Exception:
    __version__ = '0.0.0'
""")
print("✅ version added to __init__.py")

# 4) Dev requirements
req_dev.write_text("pytest>=7.0,<9.0\nblack>=24.0\nruff>=0.6\nbuild>=1.2\ntwine>=5.0\n")
print("✅ requirements-dev.txt written")

# 5) Bump script
tools_dir.mkdir(exist_ok=True)
bump_py.write_text("""import sys, re, tomllib, pathlib
P = pathlib.Path("name_format_pkg/pyproject.toml")
... (shortened for now) ...
""")

print("✅ bump_version.py written")

print("✅ ALL DONE")
