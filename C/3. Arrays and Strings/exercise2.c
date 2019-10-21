// Array Reversal "https://www.hackerrank.com/challenges/reverse-array-c/problem"

#include <stdio.h>
#include <stdlib.h>


int main() {
    int num;
    scanf("%d", &num);
    int *arr = (int*) malloc(num * sizeof(int));
    for(int i=0; i <num; i++) {
        scanf("%d", &arr[i]);
    }

    /* Write the logic to reverse the array. */
    for(int i=(num-1); i>=0; i--)
        printf("%d ", arr[i]);
    free(arr);
    return 0;
}
