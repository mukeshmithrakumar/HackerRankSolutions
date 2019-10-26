// Java HashSet "https://www.hackerrank.com/challenges/java-hashset/problem"

import java.util.*;


public class Exercise4 {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int t = s.nextInt();
        String [] pair_left = new String[t];
        String [] pair_right = new String[t];

        for (int i = 0; i < t; i++) {
            pair_left[i] = s.next();
            pair_right[i] = s.next();
        }
        s.close();

        //Write your code here
        HashSet<String> names = new HashSet();
        for (int j=0; j<t; j++) {
            names.add(pair_left[j] + " " + pair_right[j]);
            System.out.println(names.size());
        }
    }
}
