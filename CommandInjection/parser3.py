import subprocess
def build_command(target, count):
    cmd = "ping "
    final_cmd = f"{cmd}-c {count} {target}"
    return final_cmd
def main():
    target = input("Enter the target (IP address or hostname): ")
    count = int(input("Enter the number of ping packets (e.g., 4): "))
    command = build_command(target, count)
    print(f"Built Command: {command}")
    print("Executing command...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print("Ping command executed successfully.")
            print(result.stdout)  
        else:
            print("Error occurred while executing the ping command.")
            print(result.stderr)  
    except Exception as e:
        print(f"Exception occurred: {e}")
if __name__ == "__main__":
    main()