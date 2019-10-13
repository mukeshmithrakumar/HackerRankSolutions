// Java Loops I "https://www.hackerrank.com/challenges/java-loops-i/problem"

import java.util.Scanner;


public class Exercise5 {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int N = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i=1; i<=10; i++) {
            System.out.printf("%d x %d = %d\n", N, i, (i*N));
        }

        scanner.close();
    }
}
