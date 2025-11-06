import sys, re, tomllib, pathlib

P = pathlib.Path("name_format_pkg/pyproject.toml")

def get_tuple(s: str):
    m = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", s.strip())
    if not m:
        raise SystemExit(f"Invalid version format: {s}")
    return tuple(map(int, m.groups()))

def bump(kind: str) -> str:
    data = tomllib.loads(P.read_text(encoding="utf-8"))
    old = data["project"]["version"]
    major, minor, patch = get_tuple(old)

    if kind == "patch":
        patch += 1
    elif kind == "minor":
        minor += 1
        patch = 0
    elif kind == "major":
        major += 1
        minor = 0
        patch = 0
    else:
        raise SystemExit("Use: bump_version.py [patch|minor|major]")

    new = f"{major}.{minor}.{patch}"

    txt = P.read_text(encoding="utf-8")
    new_txt = re.sub(
        r'(?m)^version\s*=\s*"[0-9.]+"',
        f'version = "{new}"',
        txt,
    )
    P.write_text(new_txt, encoding="utf-8")
    print(new)
    return new

if __name__ == "__main__":
    kind = sys.argv[1] if len(sys.argv) > 1 else "patch"
    bump(kind)
