// Java Loops II "https://www.hackerrank.com/challenges/java-loops/problem"

import java.util.Scanner;


class exercise6{

    public static void main(String []arg){
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();

        for (int i=0; i<t; i++) {
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            int sum = 0;

            for (int j=0; j<n; j++) {
                sum += (Math.pow(2, j) * b);
                System.out.print((sum+a) + " ");
            }
        System.out.println();
        }
        in.close();
    }
}
