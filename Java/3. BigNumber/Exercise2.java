// Java BigInteger "https://www.hackerrank.com/challenges/java-biginteger/problem"

import java.math.BigInteger;
import java.util.Scanner;


public class Exercise2 {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        BigInteger a = scan.nextBigInteger();
        BigInteger b = scan.nextBigInteger();
        System.out.println(a.add(b)+"\n"+a.multiply(b));
    }
}
