def print_message(message):
    if message is None:
        print("Message is None. Cannot display.")
    else:
        print(message[0]) 

def main():
    
    ptr = None
    if ptr is None:
        print("Pointer is None. Skipping dereference.")
    else:
        print(ptr[0])

   
    print_message("Hello, World!")  
    print_message(None) 

    value = None
    if value is None:
        print("Value is None.")
    else:
        print(f"Value: {value}")

if __name__ == "__main__":
    main()
