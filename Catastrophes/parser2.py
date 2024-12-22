import re

def find_uninitialized_pointers_in_file(file_path):
    """
    Detect uninitialized pointers in a C++ file.
    Args:
        file_path (str): Path to the C++ file.
    Returns:
        list: A list of tuples containing the line number and uninitialized pointer declarations.
    """
    pointer_pattern = re.compile(r'(\b(?:int|float|char|double|bool|void|\w+)\s*\*\s*\w+)(?!\s*=\s*(nullptr|0|\w+\s*\(|\&\w+|[^;]+))\s*;')

    uninitialized_pointers = []
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                matches = pointer_pattern.findall(line)
                for match in matches:
                    uninitialized_pointers.append((line_number, match[0]))
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
    except Exception as e:
        print(f"Error reading file: {e}")

    return uninitialized_pointers


if __name__ == "__main__":
    cpp_file_path = "example.cpp"  

    uninitialized = find_uninitialized_pointers_in_file(cpp_file_path)

    if uninitialized:
        print("Uninitialized pointers found:")
        for line_number, pointer in uninitialized:
            print(f"Line {line_number}: {pointer}")
    else:
        print("No uninitialized pointers found.")
