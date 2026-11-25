import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINE = "I checked with the satellite, the map and the lake \u2014 two out of three said shortcut, and democracy is not my department."

# The grader collects /output as another user, so the file must be
# world-readable: umask 022 for files we open, plus an explicit chmod.
os.umask(0o022)
path = os.path.join(OUTPUT_DIR, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(LINE)
os.chmod(path, 0o644)
