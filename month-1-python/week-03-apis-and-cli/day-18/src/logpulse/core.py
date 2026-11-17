# core.py - business logic
# Write your parse_log_stream function here independently.
# Remember to import is_error_line from logpulse.utils!
from logpulse.utils import is_error_line, format_timestamp


def parse_log_stream(lines: list[str]) -> dict:
    total_line = len(lines)
    error_count = sum(1 for line in lines if is_error_line(line))
    return {
        "processed_at": format_timestamp(),
        "total_lines": total_line,
        "error_lines": error_count,
    }
