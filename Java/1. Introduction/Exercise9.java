// Java Strings Introduction "https://www.hackerrank.com/challenges/java-strings-introduction/problem"

import java.util.Scanner;

public class Exercise9 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        String B = sc.next();
        sc.close();

        /* Enter your code here. Print output to STDOUT. */
        // Sum the lengths of A and B.
        System.out.println(A.length() + B.length());

        // Determine if A is lexicographically larger than B
        System.out.println((A.compareTo(B) <= 0 ? "No" : "Yes"));

        // Capitalize the first letter in A and B and print them on a single line, separated by a space.
        String capitalizeA = A.substring(0, 1).toUpperCase() + A.substring(1);
        String capitalizeB = B.substring(0, 1).toUpperCase() + B.substring(1);
        System.out.println(capitalizeA + " " + capitalizeB);
    }
}
