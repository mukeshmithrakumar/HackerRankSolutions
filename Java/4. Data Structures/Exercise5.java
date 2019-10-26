// Java Map "https://www.hackerrank.com/challenges/phone-book/problem"

import java.util.*;


public class Exercise5{
	public static void main(String [] args) {

		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		scan.nextLine();

        // Create a HashMap with String and Integer
        HashMap<String, Integer> phoneBook = new HashMap<>();

		for (int i=0; i<n; i++) {
			String name = scan.nextLine();
			int number = scan.nextInt();
			scan.nextLine();

            // Add name and number into the phone book
            phoneBook.put(name, number);
		}

		while (scan.hasNext()) {
			String query = scan.nextLine();

            // Check if key is present, then print details, else, print Not Found
            System.out.println((phoneBook.containsKey(query)) ? (query + "=" + phoneBook.get(query)) : "Not found");
		}
		scan.close();
	}
}
