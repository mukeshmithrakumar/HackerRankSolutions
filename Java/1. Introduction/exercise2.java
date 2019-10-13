// Java Stdin and Stdout I "https://www.hackerrank.com/challenges/java-stdin-and-stdout-1/problem"

import java.util.Scanner;


public class Exercise2 {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();
        int b = scan.nextInt();
        int c = scan.nextInt();

        System.out.println(a);
        System.out.println(b);
        System.out.println(c);

        scan.close();
    }
}
