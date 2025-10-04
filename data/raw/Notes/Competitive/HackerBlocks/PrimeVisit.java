package HackerBlocks;

import java.util.Arrays;
import java.util.Scanner;

public class PrimeVisit {
    public static void main(String[] args) {
        Integer[] a = new Integer[1000002];
        Arrays.fill(a, 0);
        Integer[] k = primeSeive(a);
        for (int i = 1; i < 1000002; i++) {
            k[i] = k[i] + k[i - 1];
        }
        Scanner s = new Scanner(System.in);
        Integer t = s.nextInt();
        while (t > 0) {
            Integer n = s.nextInt();
            Integer m = s.nextInt();
            if (n == 0)
                System.out.println(k[m] - k[n]);
            else
                System.out.println(k[m] - k[n - 1]);
            t--;
        }

        s.close();
    }

    public static Boolean isPrime(Integer a) {
        if (a == 1) {
            return false;
        }
        if (a == 2) {
            return true;
        }
        for (int i = 2; i * i <= a; i++) {
            if (a % i == 0)
                return false;
        }
        return true;
    }

    public static Integer[] primeSeive(Integer[] t) {
        // Mark all odd numbers as prime
        for (int i = 3; i < t.length; i = i + 2) {
            t[i] = 1;
        }
        for (int i = 3; i < t.length; i = i + 2) {
            // If prime them mark all multiples not prime
            if (t[i] == 1) {
                for (int j = 2 * i; j < t.length; j = j + i) {
                    t[j] = 0;
                }
            }
        }
        t[2] = 1;
        return t;
    }

}