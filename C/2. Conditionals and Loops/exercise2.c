// For Loop in C "https://www.hackerrank.com/challenges/for-loop-in-c/problem"

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

static const char *strings[] = {"one","two","three","four","five", "six","seven","eight","nine"};

int main() {
    int a, b;
    scanf("%d\n%d", &a, &b);
  	// Complete the code.
    for (a; a<=b; a++) {
        if (a>=1 && a<=9) {
            printf("%s\n", strings[a-1]);
        }
        else {
            printf((a%2==0) ? "even\n" : "odd\n");
        }
    }
    return 0;
}
