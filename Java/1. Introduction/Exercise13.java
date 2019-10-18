// Java Static Initializer Block "https://www.hackerrank.com/challenges/java-static-initializer-block/problem"

import java.util.Scanner;


public class Exercise13 {

    public static Scanner sc = new Scanner(System.in);
    public static int B;
    public static int H;
    public static boolean flag;

    static {
        B = sc.nextInt();
        H = sc.nextInt();
        sc.close();

        if ((B<=0) || (H<=0)) {
            flag = false;
            System.out.println("java.lang.Exception: Breadth and height must be positive");
        }
        else {
            flag = true;
        }
    }

    public static void main(String[] args){
        if(flag){
            int area = B*H;
            System.out.print(area);
        }
    }
}
