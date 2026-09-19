#!/usr/bin/env python3
"""Set Python semantic highlighting without reformatting VS Code JSONC."""

from __future__ import annotations

import re
import sys
from pathlib import Path


SETTING = "editor.semanticHighlighting.enabled"


def matching_brace(text: str, opening: int) -> int:
    depth = 0
    in_string = False
    escaped = False
    line_comment = False
    block_comment = False

    index = opening
    while index < len(text):
        char = text[index]
        following = text[index + 1] if index + 1 < len(text) else ""

        if line_comment:
            if char in "\r\n":
                line_comment = False
        elif block_comment:
            if char == "*" and following == "/":
                block_comment = False
                index += 1
        elif in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
        elif char == "/" and following == "/":
            line_comment = True
            index += 1
        elif char == "/" and following == "*":
            block_comment = True
            index += 1
        elif char == '"':
            in_string = True
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return index

        index += 1

    raise ValueError("unclosed JSONC object")


def patch_settings(text: str) -> str:
    newline = "\r\n" if "\r\n" in text else "\n"
    python_match = re.search(r'(?m)^(?P<indent>\s*)"\[python\]"\s*:\s*\{', text)

    if python_match:
        opening = text.find("{", python_match.start())
        closing = matching_brace(text, opening)
        block = text[opening : closing + 1]
        setting_pattern = re.compile(
            rf'("{re.escape(SETTING)}"\s*:\s*)(?:true|false)'
        )

        if setting_pattern.search(block):
            patched = setting_pattern.sub(r"\g<1>false", block, count=1)
        else:
            property_indent = python_match.group("indent") + "  "
            patched = (
                "{"
                + newline
                + property_indent
                + f'"{SETTING}": false,'
                + block[1:]
            )

        return text[:opening] + patched + text[closing + 1 :]

    opening = text.find("{")
    if opening == -1:
        raise ValueError("VS Code settings do not contain a root object")

    override = (
        newline
        + "  \"[python]\": {"
        + newline
        + f'    "{SETTING}": false,'
        + newline
        + "  },"
    )
    return text[: opening + 1] + override + text[opening + 1 :]


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: {Path(sys.argv[0]).name} <settings.json>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    original = path.read_text(encoding="utf-8") if path.exists() else "{\n}\n"
    patched = patch_settings(original)

    if patched != original:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(patched, encoding="utf-8", newline="")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
