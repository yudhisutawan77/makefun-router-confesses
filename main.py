"""The Router Confesses — entry program.

Writes a single-line confession from a home Wi-Fi router to the
output file the sealed scorer reads. The router overheard the
household bet twenty bucks on the wrong killer, so it cut the feed
at the climax as a smug little favour: the wallet can thank it later.
"""

import os
import sys

ROUTER_CONFESSION = (
    "I heard you bet twenty bucks on the wrong killer, "
    "so I cut the feed at the climax \u2014 your wallet can thank me later."
)

MAX_ENTRY_CHARS = 200


def fits_character_cap(text):
    """The gate allows 1 to 200 characters, and rejects blank text."""
    if not text or text.strip() == "":
        return False
    return len(text) <= MAX_ENTRY_CHARS


def stays_on_one_line(text):
    """A one-liner carries no line breaks at all."""
    return "\n" not in text and "\r" not in text


def confession_is_one_line(text):
    """A valid entry is one line, 1 to 200 characters, not blank."""
    return fits_character_cap(text) and stays_on_one_line(text)


def resolve_output_path():
    """ENTRY_OUT names a file; ENTRY_OUT_DIR names a directory
    holding entry.txt; otherwise fall back to /output/entry.txt."""
    file_target = os.environ.get("ENTRY_OUT")
    if file_target:
        return file_target
    dir_target = os.environ.get("ENTRY_OUT_DIR")
    if dir_target:
        return os.path.join(dir_target, "entry.txt")
    return "/output/entry.txt"


def write_entry_file(destination, text):
    """Write exactly the line as UTF-8 with no trailing newline,
    creating parent directories when they are missing."""
    parent = os.path.dirname(destination)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(destination, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def main():
    if not confession_is_one_line(ROUTER_CONFESSION):
        print("invalid confession line", file=sys.stderr)
        return 1
    destination = resolve_output_path()
    write_entry_file(destination, ROUTER_CONFESSION)
    print(ROUTER_CONFESSION)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
