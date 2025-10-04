package HackerBlocks;

import java.util.Scanner;

public class IncredibleHulk {
    /* Counts how many times the substring appears in the larger string. */
    public static int countMatches(String text, String str) {
        if (text.isEmpty() || str.isEmpty()) {
            return 0;
        }
        int index = 0, count = 0;
        while (true) {
            index = text.indexOf(str, index);
            if (index != -1) {
                count++;
                index += str.length();
            } else {
                break;
            }
        }
        return count;
    }

    public static void main(String args[]) {
        Scanner s = new Scanner(System.in);
        Integer t = s.nextInt();
        for (int i = 0; i < t; i++) {
            Integer l = s.nextInt();
            System.out.println(countMatches(Integer.toBinaryString(l), "1"));
            System.out.println(Integer.bitCount(l));
        }
        s.close();
    }
}