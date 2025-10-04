import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws java.lang.Exception {
        Scanner s = new Scanner(System.in);
        String input = s.nextLine();
        String[] parted = input.split(" ");
        Integer n1 = Integer.parseInt(parted[0]);
        Integer n2 = Integer.parseInt(parted[1]);
        s.close();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("HHmmss");
        int count = 0;
        for (int i = n1; i <= n2; i++) {
            for (int j = 0; j <= 23; j++) {
                for (int k = 0; k <= 59; k++) {
                    for (int l = 0; l <= 59; l++) {
                        String Hours = "";
                        String Minutes = "";
                        String Second = "";
                        if (j < 10) {
                            Hours = String.valueOf("0" + j);
                        } else {
                            Hours = String.valueOf(j);
                        }
                        if (k < 10) {
                            Minutes = String.valueOf("0" + k);
                        } else {
                            Minutes = String.valueOf(k);
                        }
                        if (l < 10) {
                            Second = String.valueOf("0" + l);
                        } else {
                            Second = String.valueOf(l);
                        }
                        String str = Hours + Minutes + Second;
                        try {
                            LocalTime.parse(str, formatter);
                            String kml = String.valueOf(i) + str;
                            if (isPalindrome(kml)) {
                                count++;
                            }
                        } catch (Exception e) {
                            System.out.println(str);
                        }
                    }
                }
            }
        }
        System.out.print(count);
    }

    static boolean isPalindrome(String s) {
        int n = s.length();
        for (int i = 0; i < (n / 2); ++i) {
            if (s.charAt(i) != s.charAt(n - i - 1)) {
                return false;
            }
        }

        return true;
    }
}