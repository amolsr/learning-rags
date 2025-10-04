import java.util.Scanner;
import java.util.ArrayList;

public class CodeVitaQuestion {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> arrayListOne = new ArrayList<>();
        ArrayList<Integer> arrayListTwo = new ArrayList<>();

        int n1 = scanner.nextInt();
        int n2 = scanner.nextInt();
        scanner.close();

        arrayListOne.add(n1);
        arrayListOne = updatingList(arrayListOne, n1);

        arrayListTwo.add(n2);
        arrayListOne = updatingList(arrayListOne, n2);

        for (int i = arrayListOne.size() - 1, j = arrayListTwo.size() - 1; (i >= 0) && (j >= 0); i--, j--) {

            if (arrayListOne.get(i) == arrayListTwo.get(j)) {

                arrayListOne.remove(i);
                arrayListTwo.remove(j);

            }

        }

        System.out.println(arrayListOne.size() + arrayListTwo.size() - 1);

    }

    public static int factorising(int x) {

        ArrayList<Integer> arrayListThree = new ArrayList<>();

        for (int k = 1; k < x; k++) {
            if (x % k == 0) {
                arrayListThree.add(k);
            }

        }
        return arrayListThree.get(arrayListThree.size() - 1);

    }

    public static ArrayList<Integer> updatingList(ArrayList<Integer> arrayList, int n) {

        for (int x = n; x > 1;) {

            int listOneValue = factorising(x);
            arrayList.add(listOneValue);
            x = listOneValue;

        }
        return arrayList;

    }

}
