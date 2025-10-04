package HackerBlocks;

public class GaneshPattern {
    public static void main(String args[]) {
        Integer n = 9;
        // component 1
        System.out.print("*");
        for (int i = 0; i < ((n - 1) / 2 - 1); i++) {
            System.out.print(" ");
        }
        for (int i = 0; i < (n + 1) / 2; i++) {
            System.out.print("*");
        }
        System.out.println();
        // component 2
        for (int j = 0; j < ((n - 3) / 2); j++) {
            System.out.print("*");
            for (int i = 0; i < ((n - 1) / 2 - 1); i++) {
                System.out.print(" ");
            }
            System.out.print("*");
            for (int i = 0; i < (n - 1) / 2; i++) {
                System.out.print(" ");
            }
            System.out.println();
        }
        // component 3
        for (int i = 0; i < n; i++) {
            System.out.print("*");
        }
        System.out.println();
        // component 4
        for (int j = 0; j < ((n - 3) / 2); j++) {
            for (int i = 0; i < (n - 1) / 2; i++) {
                System.out.print(" ");
            }
            System.out.print("*");
            for (int i = 0; i < ((n - 1) / 2 - 1); i++) {
                System.out.print(" ");
            }
            System.out.print("*");
            System.out.println();
        }
        // component 5
        for (int i = 0; i < (n + 1) / 2; i++) {
            System.out.print("*");
        }
        for (int i = 0; i < ((n - 1) / 2 - 1); i++) {
            System.out.print(" ");
        }
        System.out.print("*");
        System.out.println();
    }
}