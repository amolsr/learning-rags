import java.util.*;

public class SortAsPerValue {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int N = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        Set<Map.Entry<String,Integer>> set = new TreeSet<>((o1,o2)->{
			return o1.getValue() - o2.getValue();
		});
        for (int i = 0; i < N; i++) {
            String[] str = scanner.nextLine().split(" ");

            String key = str[0];
            Integer value = Integer.parseInt(str[1]);
            set.add(new AbstractMap.SimpleEntry<>(key, value));
        }
        for (Map.Entry<String, Integer> entry : set) {
            System.out.println(entry.getValue());
        }
        scanner.close();
    }
}
