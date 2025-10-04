package Hackerrank;

import java.util.Arrays;
import java.util.Scanner;

public class HourGlass {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        Integer[][] arr = new Integer[6][6];
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                arr[i][j] = s.nextInt();
            }
        }

        Integer[][] sum = new Integer[arr.length - 2][arr[0].length - 2];
        for (Integer[] integers : sum) {
            Arrays.fill(integers, 0);
        }

        for (int i = 0; i < sum.length; i++) {
            for (int j = 0; j < sum[i].length; j++) {
                sum[i][j] = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j]
                        + arr[i + 2][j + 1] + arr[i + 2][j + 2];
            }
        }
        Integer max = -1000;
        for (Integer[] integers : sum) {
            for (Integer integers2 : integers) {
                if (max < integers2) {
                    max = integers2;
                }
            }
        }
        s.close();
        System.out.println(max);

    }
}