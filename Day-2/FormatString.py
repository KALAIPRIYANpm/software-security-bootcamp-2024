import os
import re
import json

class FormatStringVulnerabilityScanner:
    def __init__(self, file_paths):
        self.file_paths = file_paths
        self.vulnerabilities = []

    def scan_files(self):
        for file_path in self.file_paths:
            if os.path.exists(file_path) and file_path.endswith(('.c', '.cpp')):
                with open(file_path, 'r') as file:
                    code = file.read()
                self.scan_code(file_path, code)
            else:
                print(f"Skipping invalid or non-C/C++ file: {file_path}")

    def scan_code(self, file_path, code):
        # Regex to match potentially unsafe usage of printf-like functions
        pattern = re.compile(r"\b(printf|sprintf|fprintf|snprintf|vfprintf|vsprintf)\s*\((.*?)\)", re.DOTALL)
        matches = pattern.finditer(code)

        for match in matches:
            function_name = match.group(1)
            arguments = match.group(2)

            # Check if the first argument is user-controlled
            if self.is_user_controlled(arguments):
                self.vulnerabilities.append({
                    "file": file_path,
                    "line": self.get_line_number(code, match.start()),
                    "function": function_name,
                    "code_snippet": code[match.start():match.end()].strip()
                })

    def is_user_controlled(self, arguments):
        # Simple heuristic: look for variables instead of string literals in the first argument
        first_arg = arguments.split(',')[0].strip()
        if not (first_arg.startswith('"') and first_arg.endswith('"')):  # Not a string literal
            return True
        return False

    def get_line_number(self, code, position):
        return code[:position].count('\n') + 1
    def generate_report(self, output_file):
        report = {
            "summary": {
                "total_files_scanned": len(self.file_paths),
                "total_vulnerabilities": len(self.vulnerabilities)
            },
            "vulnerabilities": self.vulnerabilities
        }
        with open(output_file, 'w') as file:
            json.dump(report, file, indent=4)
        print(f"Report generated: {output_file}")

if __name__ == "__main__":
    input_files = [
        "test.c",
        "test.cpp",
    ]


    scanner = FormatStringVulnerabilityScanner(input_files)
    scanner.scan_files()
    scanner.generate_report("vulnerability_report.json")
