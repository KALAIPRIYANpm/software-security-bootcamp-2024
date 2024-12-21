
#include <iostream>
using namespace std;

void test_function() {
    unsigned int x = 0;
    int y = x - 1;  // Intentional underflow
    cout << "Value of y: " << y << endl;

    int maxInt = 2147483647; 
    int overflow = maxInt + 1; // Intentional overflow
    cout << "Value of overflow: " << overflow << endl;

    float z = 3.14;
    int unsafeCast = (int)z;  // Unsafe type casting
    cout << "Value of unsafeCast: " << unsafeCast << endl;
}

int main() {
    test_function();
    return 0;
}
