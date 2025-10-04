package HackerBlocks;

import java.util.*;

public class SortTheString {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        Integer t = s.nextInt();
        String[][] matStr = new String[t][t];
        s.nextLine();
        for (int i = 0; i < matStr.length; i++) {
            matStr[i][0] = s.nextLine();
            String[] slice = matStr[i][0].split(" ");
            for (int j = 1; j < t; j++) {
                matStr[i][j] = slice[j - 1];
            }
        }
        String option = s.nextLine();
        String[] options = option.split(" ");
        Integer key = Integer.parseInt(options[0]);
        Boolean reversal = Boolean.parseBoolean(options[1]);
        String ordering = options[2];
        if (ordering.equals("lexicographical")) {
            Arrays.sort(matStr, new Comparator<String[]>() {
                @Override
                public int compare(String[] o1, String[] o2) {
                    if (reversal == true) {
                        String itemIdOne = o1[key];
                        String itemIdTwo = o2[key];
                        return -1 * itemIdOne.compareTo(itemIdTwo);

                    } else {
                        String itemIdOne = o1[key];
                        String itemIdTwo = o2[key];
                        return itemIdOne.compareTo(itemIdTwo);
                    }
                }
            });
            for (int i = 0; i < matStr.length; i++) {
                System.out.print(matStr[i][0] + " ");
            }
        } else {
            Object[][] temp = new Object[t][t];
            for (int i = 0; i < matStr.length; i++) {
                for (int j = 0; j < matStr[i].length; j++) {
                    if (j != 0) {
                        temp[i][j] = Integer.parseInt(matStr[i][j]);
                    } else {
                        temp[i][j] = matStr[i][j];
                    }
                }
            }
            Arrays.sort(temp, new Comparator<Object[]>() {
                @Override
                public int compare(Object[] o1, Object[] o2) {
                    if (reversal == true) {
                        Integer itemIdOne = (Integer) o1[key];
                        Integer itemIdTwo = (Integer) o2[key];
                        return -1 * itemIdOne.compareTo(itemIdTwo);

                    } else {
                        Integer itemIdOne = (Integer) o1[key];
                        Integer itemIdTwo = (Integer) o2[key];
                        return itemIdOne.compareTo(itemIdTwo);
                    }
                }
            });
            for (int i = 0; i < matStr.length; i++) {
                System.out.println(temp[i][0] + " ");
            }
        }
        s.close();
    }
}