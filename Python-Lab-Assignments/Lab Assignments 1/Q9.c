// Program to convert Fahrenheit to Celsius

#include <stdio.h>
int main() {
    float f, c;
    printf("Enter temperature in Fahrenheit: ");
    scanf("%f", &f);  // input
    c = (f - 32) * 5 / 9;  // computation
    printf("Temperature in Celsius: %f", c);  // output
    return 0;
}
