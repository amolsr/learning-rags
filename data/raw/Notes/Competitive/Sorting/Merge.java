package Sorting;

public class Merge {
    public static void main(String[] args) {
        int[] n = { 5, 6, 8, 7, 9, 3, 1, 2 };
        mergeSort(n, 0, n.length - 1);
        for (int i : n) {
            System.out.print(i + " ");
        }
    }

    public static void merge(int[] a, int s, int e) {
        int m = (s + e) / 2;
        int i = s;
        int j = m + 1;
        int k = s;
        int temp[] = new int[a.length];
        while (i <= m && j <= e) {
            if (a[i] < a[j]) {
                temp[k++] = a[i++];
            } else {
                temp[k++] = a[j++];
            }
        }
        while (i <= m)
            temp[k++] = a[i++];

        while (j <= e)
            temp[k++] = a[j++];

        for (int l = s; l <= e; l++) {
            a[l] = temp[l];
        }
    }

    public static void mergeSort(int[] a, int start, int end) {
        if (start == end) {
            return;
        } else {
            int mid = (start + end) / 2;
            mergeSort(a, start, mid);
            mergeSort(a, mid + 1, end);
            merge(a, start, end);
        }
    }
}