# utils.py - helper functions
from datetime import datetime


def format_timestamp(dt: datetime | None = None) -> str:
    """Returns a clean ISO timestamp string."""
    target = dt or datetime.now()
    return target.strftime("%Y-%m-%d %H:%M:%S")


def is_error_line(line: str) -> bool:
    """Checks if a log line represents an error."""
    return "[ERROR]" in line
