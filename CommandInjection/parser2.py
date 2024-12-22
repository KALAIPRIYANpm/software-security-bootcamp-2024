import subprocess

cpp_code = """
#include <iostream>
#include <sstream>
#include <string>

std::string buildCommand(const std::string& input) {
    std::string cmd = "ping ";
    std::stringstream ss;
    ss << cmd << "-c " << "4 " << input;
    return ss.str();
}

void executeCommand(const std::string& target) {
    std::string finalCmd = buildCommand(target);
    std::cout << "Executing command: " << finalCmd << std::endl;
    // system(finalCmd.c_str()); // Uncomment to actually execute
}

int main() {
    std::string target = "example.com";
    executeCommand(target);
    return 0;
}
"""

def build_command(input):
    cmd = "ping "
    final_cmd = f"{cmd}-c 4 {input}"
    return final_cmd

def execute_command(target):
    final_cmd = build_command(target)
    print(f"Executing command: {final_cmd}")
    subprocess.run(final_cmd, shell=True)

if __name__ == "__main__":
    target = input("Enter the target for the ping command: ")
    execute_command(target)
