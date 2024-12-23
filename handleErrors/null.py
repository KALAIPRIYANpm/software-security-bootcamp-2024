# Example to simulate a Null Pointer Error in Python
def dereference_none():
    my_var = None
    # Trying to call a method on None (which will raise an error)
    my_var.some_method()

try:
    dereference_none()
except AttributeError as e:
    print(f"Null Pointer Error: {e}")
