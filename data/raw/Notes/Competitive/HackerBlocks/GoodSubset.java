package HackerBlocks;

import java.util.Arrays;
import java.util.Scanner;

public class GoodSubset {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        Integer[] pre = new Integer[1000005];
        Integer[] arr = new Integer[1000005];
        Integer t = 1;
        while (t-- != 0) {
            Integer n = s.nextInt();
            Arrays.fill(pre, 0);
            pre[0] = 1;
            int sum = 0;
            for (int i = 0; i < n; i++) {
                arr[i] = s.nextInt();
                sum += arr[i];
                sum %= n;
                sum = (sum + n) % n;
                pre[sum]++;
            }
            int ans = 0;
            for (int i = 0; i < n; i++) {
                int m = pre[i];
                // nC2 of a number m
                ans += (m) * (m - 1) / 2;
            }
            if (arr[0] == 0 && n == 1)
                System.out.println(0);
            else
                System.out.println(ans);
        }
        s.close();
    }
}