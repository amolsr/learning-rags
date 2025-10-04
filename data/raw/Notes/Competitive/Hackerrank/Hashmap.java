package Hackerrank;
//Complete this code or write your own from scratch
import java.util.*;

class Hashmap {
    public static void main(String[] argh) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            String name = in.next();
            Integer phone = in.nextInt();
            map.put(name, phone);
        }
        while (in.hasNext()) {
            String s = in.next();
            if(map.containsKey(s)) {
                Integer phone = map.get(s);
                System.out.println(s + "=" + phone);
            } else {
                System.out.println("Not found");
            }
        }
        in.close();
    }
}