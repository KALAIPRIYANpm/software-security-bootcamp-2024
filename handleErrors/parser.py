import re
import sys

class NullPointerError(Exception):
    """Custom exception for misuse of None."""
    pass

def read_file(file_path):
    """Reads the content of a file."""
    try:
        with open(file_path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise RuntimeError(f"Error reading file: {e}")

def detect_none_misuse(lines):
    """Detects potential misuse of None in the provided lines."""
    issues = []
    none_pattern = re.compile(r"None")

    for line_number, line in enumerate(lines, start=1):
        # Check for potential None misuse
        if "None" in line:
            # Heuristic checks
            if not re.search(r"if\s+\w+\s*==\s*None|is\s+None", line) and "None" in line:
                issues.append((line_number, line.strip()))

    return issues

def main(file_path):
    try:
        lines = read_file(file_path)
        issues = detect_none_misuse(lines)

        if not issues:
            print("No potential misuse of None detected.")
        else:
            print("Detected potential issues:")
            for line_number, issue in issues:
                print(f"Line {line_number}: {issue}")
            # Raising a NullPointerError if misuse of None is detected
            raise NullPointerError("Misuse of None detected in the code.")

    except NullPointerError as e:
        print(f"NullPointerError: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file_path>")
        sys.exit(1)

    main(sys.argv[1])
