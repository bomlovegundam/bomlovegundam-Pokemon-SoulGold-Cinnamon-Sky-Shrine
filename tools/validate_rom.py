#!/usr/bin/env python3
"""Static validation for the verified Pokémon SoulGold Safe V2 ROM."""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

EXPECTED_SIZE = 33_554_432
EXPECTED_SHA256 = "9de6c224e54a006ae361435d72da4524fdde6077365c95871715a31032e7c23f"

MAP55_HEADER_OFFSET = 0x156CC38
EXPECTED_MAP55_HEADER = bytes.fromhex(
    "e071f309cc72f3097f70390800000000"
    "43034d02cd00000008000400"
)

ENTRY_SCRIPT_OFFSET = 0x1F03C60
EXPECTED_ENTRY_SCRIPT = bytes.fromhex("3d1900ff1f000d002702ffff")

RETURN_SCRIPT_OFFSET = 0x1F03C6C
EXPECTED_RETURN_SCRIPT = bytes.fromhex("3d0302ff1e000e002702ffff")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def check_bytes(data: bytes, offset: int, expected: bytes, name: str) -> bool:
    actual = data[offset : offset + len(expected)]
    ok = actual == expected
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if not ok:
        print(f"       expected: {expected.hex()}")
        print(f"       actual:   {actual.hex()}")
    return ok


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python tools/validate_rom.py <rom.gba>")
        return 2

    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"[FAIL] ROM not found: {path}")
        return 1

    data = path.read_bytes()
    ok = True

    size_ok = len(data) == EXPECTED_SIZE
    print(f"[{'PASS' if size_ok else 'FAIL'}] ROM size")
    if not size_ok:
        print(f"       expected: {EXPECTED_SIZE}")
        print(f"       actual:   {len(data)}")
    ok &= size_ok

    digest = sha256(path)
    hash_ok = digest == EXPECTED_SHA256
    print(f"[{'PASS' if hash_ok else 'FAIL'}] SHA-256")
    print(f"       actual:   {digest}")
    print(f"       expected: {EXPECTED_SHA256}")
    ok &= hash_ok

    ok &= check_bytes(
        data, MAP55_HEADER_OFFSET, EXPECTED_MAP55_HEADER, "Group3/Map55 safe header"
    )
    ok &= check_bytes(
        data, ENTRY_SCRIPT_OFFSET, EXPECTED_ENTRY_SCRIPT, "Sky Shrine entry script"
    )
    ok &= check_bytes(
        data, RETURN_SCRIPT_OFFSET, EXPECTED_RETURN_SCRIPT, "Return script"
    )

    print()
    if ok:
        print("STATIC VALIDATION PASS")
        print("Note: runtime emulator validation is still required.")
        return 0

    print("STATIC VALIDATION FAIL")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
