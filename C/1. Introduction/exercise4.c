// Pointers in C "https://www.hackerrank.com/challenges/pointer-in-c/problem"

#include <stdio.h>
#include <stdlib.h>

void update(int *a,int *b) {
    // Complete this function
    // Creating a temporary variable because in the next line a* will change so getting abs will not work
    int temp_a = *a;
    *a += *b;
    *b = abs(temp_a - *b);
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;

    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
