import re

def analyze_command_building(cpp_code):
    """
    Analyze C++ code for command building and execution patterns.

    Args:
        cpp_code (str): C++ source code as a string.

    Returns:
        list: Detected issues and details about operations.
    """
    results = []

  
    stringstream_decl = re.compile(r'stringstream\s+(\w+)')
    stringstream_append = re.compile(r'(\w+)\s*<<\s*(.+?);')
    function_def = re.compile(r'(?:void|string|\w+)\s+(\w+)\s*\(.*?\)\s*{')
    system_call = re.compile(r'system\s*\((.*?)\);')
    function_call = re.compile(r'(\w+)\s*\((.*?)\);')

    lines = cpp_code.splitlines()
    current_function = None

    for line_number, line in enumerate(lines, start=1):
        line = line.strip()

        func_match = function_def.match(line)
        if func_match:
            current_function = func_match.group(1)

        decl_match = stringstream_decl.search(line)
        if decl_match:
            results.append({
                "line": line_number,
                "type": "stringstream_declaration",
                "details": f"stringstream {decl_match.group(1)} declared in function {current_function}"
            })

        append_match = stringstream_append.search(line)
        if append_match:
            results.append({
                "line": line_number,
                "type": "append_operation",
                "details": f"{append_match.group(1)} << {append_match.group(2)} in function {current_function}"
            })

        system_match = system_call.search(line)
        if system_match:
            results.append({
                "line": line_number,
                "type": "system_call",
                "details": f"system({system_match.group(1)}) called in function {current_function}"
            })

        call_match = function_call.search(line)
        if call_match:
            results.append({
                "line": line_number,
                "type": "function_call",
                "details": f"Call to {call_match.group(1)}({call_match.group(2)}) in function {current_function}"
            })

    return results


if __name__ == "__main__":
    cpp_code = """
    string buildCommand(const string& input) {
        string cmd = "ping ";
        stringstream ss;
        ss << cmd << "-c " << "4 " << input;
        return ss.str();
    }
    void executeCommand(const string& target) {
        string finalCmd = buildCommand(target);
        system(finalCmd.c_str());
    }
    """

    results = analyze_command_building(cpp_code)

    for result in results:
        print(f"Line {result['line']}: {result['details']}")
