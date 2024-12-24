def dereference_none():
    my_var = None

    my_var.some_method()

try:
    dereference_none()
except AttributeError as e:
    print(f"Null Pointer Error: {e}")
