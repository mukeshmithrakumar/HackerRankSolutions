// For Loop "https://www.hackerrank.com/challenges/c-tutorial-for-loop/problem"

#include <iostream>
#include <cstdio>
using namespace std;

string num[9] = {"one","two","three","four","five", "six","seven","eight","nine"};

int main() {
    // Complete the code.
    int a, b;

    cin >> a;
    cin >> b;

    for (a; a<=b; a++) {
        cout << ((a>=1 && a <=9) ? num[a-1] + "\n" : ((a%2==0) ? "even\n" : "odd\n"));
    }
    return 0;
}
