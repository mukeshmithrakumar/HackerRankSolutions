// Java Substring "https://www.hackerrank.com/challenges/java-substring/problem"

import java.util.Scanner;


public class Exercise3 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String S = sc.next();
        int start = sc.nextInt();
        int end = sc.nextInt();

        System.out.println(S.substring(start, end));
    }
}
