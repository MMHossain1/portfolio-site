#!/usr/bin/env python3
"""Find 5-letter dictionary words that match a Wordle-style pattern.

Use '_' for unknown letters.
Examples:
- a__le
- _r__e
"""

from __future__ import annotations

import argparse
import os
import sys
from typing import Iterable, List

DEFAULT_WORD_LIST_PATH = "/usr/share/dict/words"

def validate_pattern(pattern: str) -> str:
    """Return a normalized pattern or raise ValueError if invalid."""
    normalized = pattern.strip().lower()

    if len(normalized) != 5:
        raise ValueError("Pattern must be exactly 5 characters long.")

    for char in normalized:
        if not (char.isalpha() or char == "_"):
            raise ValueError("Pattern can contain only letters (a-z) or '_' characters.")

    return normalized


def pattern_matches(word: str, pattern: str) -> bool:
    """Check whether a word satisfies the given pattern."""
    lower_word = word.lower()
    for idx, char in enumerate(pattern):
        if char != "_" and lower_word[idx] != char:
            return False
    return True


def find_dictionary_file(provided_path: str | None) -> str:
    """Find a readable dictionary path."""
    if provided_path:
        if os.path.isfile(provided_path):
            return provided_path
        raise FileNotFoundError(f"Dictionary file not found: {provided_path}")

    if os.path.isfile(DEFAULT_WORD_LIST_PATH):
        return DEFAULT_WORD_LIST_PATH

    raise FileNotFoundError(
        "Could not find a dictionary file. Provide one with --dict, "
        "or install words (usually at /usr/share/dict/words)."
    )


def load_candidate_words(dictionary_path: str) -> List[str]:
    """Load 5-letter alphabetic words from dictionary, preserving original case."""
    candidates: set[str] = set()
    with open(dictionary_path, "r", encoding="utf-8", errors="ignore") as file:
        for line in file:
            word = line.strip()
            if len(word) == 5 and word.isalpha():
                candidates.add(word)
    return sorted(candidates, key=lambda value: value.lower())


def find_matches(words: Iterable[str], pattern: str) -> List[str]:
    """Return all words that match the pattern."""
    return [word for word in words if pattern_matches(word, pattern)]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Find possible 5-letter words from a Wordle-style pattern."
    )
    parser.add_argument(
        "pattern",
        nargs="?",
        help="A 5-character pattern using letters and '_' for unknown letters.",
    )
    parser.add_argument(
        "--dict",
        dest="dict_path",
        help="Path to dictionary file (defaults to /usr/share/dict/words when available).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    raw_pattern = args.pattern
    if not raw_pattern:
        raw_pattern = input("Enter a 5-letter pattern (use '_' for unknown letters): ")

    try:
        pattern = validate_pattern(raw_pattern)
        dictionary_path = find_dictionary_file(args.dict_path)
    except (ValueError, FileNotFoundError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    words = load_candidate_words(dictionary_path)
    matches = find_matches(words, pattern)

    if not matches:
        print("No matches found.")
        return 0

    for match in matches:
        print(match)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
