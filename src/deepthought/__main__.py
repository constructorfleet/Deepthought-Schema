"""Allow ``python -m deepthought ...`` as an alias for the CLI."""

from deepthought.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
