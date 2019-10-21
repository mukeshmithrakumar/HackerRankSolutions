// Java List "https://www.hackerrank.com/challenges/java-list/problem"

import java.util.Scanner;
import java.util.LinkedList;


public class Exercise2 {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        // Using LinkedList because it is faster than ArrayList since it uses a doubly linked list
        LinkedList<Integer> arr = new LinkedList<Integer>();

        for (int i=0; i<n; i++) {
            arr.add(scan.nextInt());
        }

        int m = scan.nextInt();
        for (int j=0; j<m; j++) {
            String cmd = scan.next();
            if (cmd.equals("Insert")) {
                int index = scan.nextInt();
                int num = scan.nextInt();
                arr.add(index, num);
            }
            else {
                int index = scan.nextInt();
                arr.remove(index);
            }
        }
        for (int element: arr) {
            System.out.print(element + " ");
        }
        scan.close();
    }
}
