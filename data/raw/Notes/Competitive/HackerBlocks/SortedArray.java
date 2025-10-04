package HackerBlocks;

import java.util.Scanner;

public class SortedArray {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        Integer n = s.nextInt();
        Integer[] N = new Integer[n];
        for (int i = 0; i < N.length; i++) {
            N[i] = s.nextInt();
        }
        Integer k = s.nextInt();
        int start = 0;
        int end = n - 1;
        int mid = (start + end) / 2;
        while (start <= end) {
            if (N[mid] > k) {
                end = mid - 1;
                mid = (start + end) / 2;
            } else if (N[mid] < k) {
                start = mid + 1;
                mid = (start + end) / 2;
            } else if (N[mid] == k) {
                System.out.println(mid + 1);
                break;
            }
        }
        s.close();
    }
}