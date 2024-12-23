#include <stdio.h>

int main() {
    char user_input[100];
    printf("Enter your input: ");
    gets(user_input);   
    printf("%c",user_input);  ////affected block of code 
    return 0;
}