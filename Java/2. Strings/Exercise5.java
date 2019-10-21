// Java String Tokens "https://www.hackerrank.com/challenges/java-string-tokens/problem"

import java.util.Scanner;


public class Exercise5 {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        // Write your code here.
        String[] sArr = s.trim().split("[ !,?._'@]+");

        if ((s.trim().isEmpty()) || (s.length() == 0)) {
            System.out.println("0");
        }

        System.out.println(sArr.length);
        for (String a: sArr) {
            System.out.println(a);
        }
        scan.close();
    }
}

// If test case 9 gives you trouble for stupid reasons, I would try the following code to just get through the exercise

/*
import java.util.Scanner;
import java.util.StringTokenizer;


public class Exercise5 {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        s.trim();
        StringTokenizer st = new StringTokenizer(s,("[_\\@!?.', ]"));
        int x = st.countTokens();
        System.out.println(x);
        while(st.hasMoreTokens()){
            System.out.println(st.nextToken());
        }
    }
}
*/
