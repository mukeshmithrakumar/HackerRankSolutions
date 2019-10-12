// Conditional Statements "https://www.hackerrank.com/challenges/c-tutorial-conditional-if-else/problem"

#include <bits/stdc++.h>

using namespace std;

string num[9] = {"one","two","three","four","five", "six","seven","eight","nine"};

int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    // Write Your Code Here
    cout << ((n>=1 && n<=9) ? num[n-1] : "Greater than 9");

    return 0;
}
