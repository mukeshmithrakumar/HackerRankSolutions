// Java ArrayList "https://www.hackerrank.com/challenges/java-arraylist/problem"

import java.util.*;

public class Exercise3 {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        // Read the first number
        int n = scan.nextInt();

        // Creating a Hashmap to store the ArrayLists
        HashMap<String, ArrayList<Integer>> items = new HashMap<String, ArrayList<Integer>>();

        // Iterate over n and store the inputs in a ArrayList
        for (int i=1; i<=n; i++) {
            int s = scan.nextInt();
            // Create an ArrayList
            ArrayList<Integer> arrList = new ArrayList<Integer>();

            // Scan for the input and put the input into ArrayList
            for (int j=0;j<s; j++) {
                arrList.add(scan.nextInt());
            }
            // Put the array list in a map
            items.put("items"+i, arrList);
        }

        // Read q number of queries
        int q = scan.nextInt();

        // Iterate over q number of queries
        for (int k=0; k<q; k++) {
            int x = scan.nextInt();
            int y = scan.nextInt();

            // verify if the query is in the respected ArrayList
            try {
                System.out.println(items.get("items"+x).get(y-1));
            }
            catch (Exception e){
                System.out.println("ERROR!");
            }
        }
        scan.close();
    }
}
