package HackerBlocks;

import java.util.*;

public class TrailingZero {
    public static void main(String args[]) {
        Scanner s = new Scanner(System.in);
        Integer i = s.nextInt();
        Integer noOfZeros = 0;
        Integer t = i / 5;
        while (t > 0) {
            noOfZeros += t;
            ;
            t = t / 5;
        }
        System.out.print(noOfZeros);
        s.close();
    }
}