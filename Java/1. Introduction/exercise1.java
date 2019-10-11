// Java If-Else "https://www.hackerrank.com/challenges/java-if-else/problem"

import java.util.Scanner;


public class exercise1 {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int N = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        // If  is odd, print Weird
        // If  is even and in the inclusive range of 6 to 20, print Weird
        if ((N%2==1) || (N%2==0 && (N>=6 && N<=20))) {
            System.out.println("Weird");
        }
        // If  is even and in the inclusive range of 2 to 5, print Not Weird
        // If  is even and greater than 20, print Not Weird
        else {
            if ((N>=2 && N<=5) || (N>20)) {
                System.out.println("Not Weird");
            }
        }

        scanner.close();
    }
}
