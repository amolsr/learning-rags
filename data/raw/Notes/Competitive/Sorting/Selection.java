package Sorting;

public class Selection {
    public static void main(String[] args) {
        Integer[] n = { 5, 6, 8, 7, 9, 3, 1, 2 };
        for (int i = 0; i < n.length; i++) {
            int smallest = i;
            for (int j = i; j < n.length; j++) {
                if (n[j] < n[smallest]) {
                    smallest = j;
                }
            }
            if(i!=smallest){
                n[i] = n[i] + n[smallest];
                n[smallest] = n[i] - n[smallest];
                n[i] = n[i] - n[smallest];
            }
        }
        for (Integer integer : n) {
            System.out.println(integer);
        }
    }
}