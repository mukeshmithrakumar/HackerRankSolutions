// Playing With Characters "https://www.hackerrank.com/challenges/playing-with-characters/problem"

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>


int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    char ch;
    char s[100];
    char sen[1024];

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    scanf("%c", &ch);
    scanf("%s%*c", &s);
    scanf("%[^\n]%*c", &sen);

    printf("%c\n%s\n%s", ch, s, sen);
    return 0;
}
