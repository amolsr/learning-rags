package Sorting;

public class Quick {
    public static void main(String[] args) {
        Integer[] n = { 5, 6, 8, 7, 9, 3, 1, 2 };
        quickSort(n, 0, n.length - 1);
        for (int i : n) {
            System.out.print(i + " ");
        }
    }

    public static int partition(Integer[] n, Integer start, Integer end) {
        int pivot = n[end];
        int i = (start - 1);
        for (int j = start; j < end; j++) {
            if (n[j] < pivot) {
                i++;
                int temp = n[i];
                n[i] = n[j];
                n[j] = temp;
            }
        }
        int temp = n[i + 1];
        n[i + 1] = n[end];
        n[end] = temp;

        return i + 1;
    }

    public static void quickSort(Integer[] n, Integer start, Integer end) {
        if (start <= end) {
            int i = partition(n, start, end);
            quickSort(n, start, i - 1);
            quickSort(n, i + 1, end);
        }
    }
}