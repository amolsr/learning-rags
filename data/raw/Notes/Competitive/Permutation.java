import java.util.ArrayList;
import java.util.List;

public class Permutation {

    public static void permutations(String consChars, String input, List<String> list) {
        if (input.isEmpty()) {
            list.add(consChars);
            return;
        }
        for (int i = 0; i < input.length(); i++) {
            permutations(consChars + input.charAt(i), input.substring(0, i) + input.substring(i + 1), list);
        }
    }

    public static void main(String a[]) {
        List<String> output = new ArrayList<String>();
        permutations("", "123", output);
        for (String c : output) {
            System.out.println(c);
        }
    }

    public static List<List<Integer>> listPermutations(List<Integer> list) {

        if (list.size() == 0) {
            List<List<Integer>> result = new ArrayList<List<Integer>>();
            result.add(new ArrayList<Integer>());
            return result;
        }

        List<List<Integer>> returnMe = new ArrayList<List<Integer>>();

        Integer firstElement = list.remove(0);

        List<List<Integer>> recursiveReturn = listPermutations(list);
        for (List<Integer> li : recursiveReturn) {

            for (int index = 0; index <= li.size(); index++) {
                List<Integer> temp = new ArrayList<Integer>(li);
                temp.add(index, firstElement);
                returnMe.add(temp);
            }

        }
        return returnMe;
    }
}
