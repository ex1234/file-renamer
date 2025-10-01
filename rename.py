import sys, pathlib
if len(sys.argv)<4: print('Usage: rename.py <dir> <prefix> <suffix>'); raise SystemExit
d, pre, suf = map(pathlib.Path, [sys.argv[1]]), sys.argv[2], sys.argv[3]
for p in d[0].iterdir():
    if p.is_file():
        p.rename(p.with_name(pre + p.stem + suf + p.suffix))
