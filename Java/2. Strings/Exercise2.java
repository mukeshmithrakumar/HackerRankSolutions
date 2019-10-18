// Java String Reverse "https://www.hackerrank.com/challenges/java-string-reverse/problem"

import java.lang.StringBuilder;
import java.util.Scanner;


public class Exercise2 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        /* Enter your code here. Print output to STDOUT. */
        String reverse = "";

        for (int i=A.length()-1; i>=0; i--) {
            reverse += A.charAt(i);
        }
        System.out.print((A.equals(reverse)) ? "Yes" : "No");
        sc.close();

        // One liner solution below:
        // System.out.println(A.equals(new StringBuilder(A).reverse().toString()) ? "Yes" : "No");
    }
}
