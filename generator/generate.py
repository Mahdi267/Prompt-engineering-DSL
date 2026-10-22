"""Command-line entry point for the DSL-to-prompt generation pipeline."""

import sys


def main() -> int:
    print(
        "Le générateur n'est pas encore configuré : définissez le format "
        "d'export AToMPM et le flux d'appel LLM.",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
