// Valid Username Regular Expression "https://www.hackerrank.com/challenges/valid-username-checker/problem"

import java.util.Scanner;


public class Exercise7 {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = Integer.parseInt(scan.nextLine());
        String regularExpression = "^[[A-Z]|[a-z]][[A-Z]|[a-z]|\\d|[_]]{7,29}$";

        while (n-- != 0) {
            String userName = scan.nextLine();
            if (userName.matches(regularExpression)) {
                System.out.println("Valid");
            } else {
                System.out.println("Invalid");
            }
        }
        scan.close();
    }
}
