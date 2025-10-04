package Sorting;

public class Insertion {
    public static void main(String[] args) {
        Integer[] n = { 5, 6, 8, 7, 9, 3, 1, 2 };
        for (int i = 1; i < n.length; i++) {
            int element = n[i];
            int j = i - 1;
            while (j >= 0 && n[j] > element) {
                n[j + 1] = n[j];
                j--;
            }
            n[j + 1] = element;
        }
        for (Integer integer : n) {
            System.out.println(integer);
        }
    }
}
