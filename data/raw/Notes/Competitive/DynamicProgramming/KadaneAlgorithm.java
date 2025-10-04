import java.util.Scanner;
public class KadaneAlgorithm {
    
    static int largestContiguousSum(int arr[]) {
        int i, len = arr.length, cursum = 0, maxsum = Integer.MIN_VALUE;
        if (len == 0)    //empty array
            return 0;
        for (i = 0; i < len; i++) {
            cursum += arr[i];
            // If sum is greater then the maxsum update.
            if (cursum > maxsum) {
                maxsum = cursum;
            }
            // If sum become negative drop it.
            if (cursum <= 0) {
                cursum = 0;
            }
        }
        return maxsum;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n, arr[], i;
        int t = sc.nextInt();
        while(t--!=0){
            n = sc.nextInt();
            arr = new int[n];
            for (i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }
            int maxContSum = largestContiguousSum(arr);
            System.out.println(maxContSum);
        }
        sc.close();
    }

}
