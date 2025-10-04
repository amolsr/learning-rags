package HackerBlocks;

import java.util.Scanner;

public class RotatedImage {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        Integer N = s.nextInt();
        Integer[][] t = new Integer[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                t[i][j] = s.nextInt();
            }
        }
        Integer[][] temp = new Integer[N][N];
        for (int i = 0, k = N - 1; i < N && k >= 0; i++, k--) {
            for (int j = 0, l = 0; j < N && j < N; j++, l++) {
                temp[i][j] = t[l][k];
            }
        }
        for (Integer[] p : temp) {
            for (Integer q : p) {
                System.out.print(q + " ");
            }
            System.out.println();
        }
        s.close();
    }
}