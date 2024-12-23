def print_message(message):
    
    print(message[0]) 

def main():
    ptr = None
    try:
        print(ptr[0])  
    except TypeError as e:
        print(f"Issue detected: {e}")

  
    try:
        print_message(None)  
    except TypeError as e:
        print(f"Issue detected: {e}")

   
    value = None
    if value:  
        print("This will not print because value is None.")

if __name__ == "__main__":
    main()
