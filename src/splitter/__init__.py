"""Splitter: Splits datasets into train, validation and test sets with balanced classes."""

__version__ = "1.0.0"

from .core import run
from .cli import main

__all__ = ["main", "run", "__version__"]