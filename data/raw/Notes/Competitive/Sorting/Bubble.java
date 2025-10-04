package Sorting;

public class Bubble {
    public static void main(String[] args) {
        Integer[] n = { 5, 6, 8, 7, 9, 3, 1, 2 };
        for (int i = 0; i < n.length - 1; i++) {
            for (int j = 1; j < n.length - i; j++) {
                if (n[j] < n[j - 1]) {
                    n[j - 1] = n[j - 1] + n[j];
                    n[j] = n[j - 1] - n[j];
                    n[j - 1] = n[j - 1] - n[j];
                }
            }
        }
        for (Integer integer : n) {
            System.out.println(integer);
        }
    }
}