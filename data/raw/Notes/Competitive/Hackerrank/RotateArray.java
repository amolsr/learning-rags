package Hackerrank;

import java.util.*;

public class RotateArray {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        Integer test = s.nextInt();
        Integer r = s.nextInt();
        Integer[] arr = new Integer[test];
        Integer[] result = new Integer[test];
        for (int i = 0; i < test; i++) {
            arr[i] = s.nextInt();
        }
        Integer rotate = r % test;
        Integer[] temp = new Integer[test - rotate];
        for (int j = 0, i = rotate; i < arr.length; i++, j++) {
            temp[j] = arr[i];
        }
        for (int j = test - rotate, i = 0; i < rotate; i++, j++) {
            result[j] = arr[i];
        }
        for (int j = 0; j < temp.length; j++) {
            result[j] = temp[j];
        }
        Arrays.stream(result).forEach(e->System.out.print(e + " ")); 
        s.close();
    }
}
