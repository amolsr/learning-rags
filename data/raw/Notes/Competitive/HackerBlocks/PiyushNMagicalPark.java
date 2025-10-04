package HackerBlocks;

import java.util.*;

public class PiyushNMagicalPark {
    public static void main(String args[]) {
        Integer N, M, K, S;
        Scanner s = new Scanner(System.in);
        N = s.nextInt();
        M = s.nextInt();
        K = s.nextInt();
        S = s.nextInt();
        char[][] temp = new char[N][M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                temp[i][j] = s.next().charAt(0);
            }
        }
        loop1: for (int i = 0; i < N; i++) {
            loop2: for (int j = 0; j < M; j++) {
                if (S < K) {
                    break loop1;
                } else {
                    if (temp[i][j] == '#') {
                        break loop2;
                    } else {
                        S = S - 1;
                        if (temp[i][j] == '*') {
                            S = S + 5;
                        } else if (temp[i][j] == '.') {
                            S = S - 2;
                        }
                    }
                }
            }
        }
        if (S < K) {
            System.out.println("No");
        } else {
            System.out.println("Yes");
            System.out.println(S);
        }
    }
}
