// Functions in C "https://www.hackerrank.com/challenges/functions-in-c/problem"

#include <stdio.h>
/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/

int max_of_four(int a, int b, int c, int d) {
    int max1, max2;
    return (max1=a>b?a:b)>(max2=c>d?c:d)?max1:max2;
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);

    return 0;
}
