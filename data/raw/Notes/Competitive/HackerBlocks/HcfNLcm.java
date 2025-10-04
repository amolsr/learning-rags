package HackerBlocks;

public class HcfNLcm {
    public static void main(String args[]) {
        Integer i = 12;
        Integer j = 20;
        System.out.println(LCM(i, j));
    }
    public static Integer GCD(Integer a, Integer b) {
        if (b == 0)
            return a;
        else return GCD(b, a % b);
    }
    public static Integer LCM(Integer a, Integer b) {
        return (a * b) / GCD(a, b);
    }
}