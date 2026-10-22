#!/usr/bin/env python3
"""Fail when a committed YAML or JSON document does not parse.

The repository is data, not code: the fast lane's job is to catch a malformed
profile, rule, collection or model source before it reaches a consumer.
"""
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SKIP_DIRS = {".git", "node_modules", "dist", "site"}
failures = []

for path in sorted(ROOT.rglob("*")):
    if not path.is_file():
        continue
    rel = path.relative_to(ROOT)
    if any(part in SKIP_DIRS for part in rel.parts):
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    try:
        if path.suffix in (".yaml", ".yml"):
            list(yaml.safe_load_all(text))
        elif path.suffix == ".json":
            json.loads(text)
    except Exception as exc:  # noqa: BLE001 - report every parser error
        failures.append((rel, str(exc).splitlines()[0]))

if failures:
    for rel, message in failures:
        print(f"::error file={rel}::{message}")
    sys.exit(1)

print("all YAML and JSON documents parse")
