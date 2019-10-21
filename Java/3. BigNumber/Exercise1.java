// Java Primality Test "https://www.hackerrank.com/challenges/java-primality-test/problem"

import java.math.BigInteger;
import java.util.Scanner;


public class Exercise1 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println((scanner.nextBigInteger().isProbablePrime(1)) ? "prime" : "not prime");
        scanner.close();
    }
}
