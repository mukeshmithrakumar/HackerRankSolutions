// Java Date and Time "https://www.hackerrank.com/challenges/java-date-and-time/problem"

import java.util.Scanner;
import java.time.LocalDate;


public class Exercise10 {

    // Complete the function below
    public static String findDay(int month, int day, int year) {
        return LocalDate.of(year, month, day).getDayOfWeek().name();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int month = sc.nextInt();
        int day = sc.nextInt();
        int year = sc.nextInt();
        sc.close();

        String res = findDay(month, day, year);
        System.out.println(res);
    }
}
