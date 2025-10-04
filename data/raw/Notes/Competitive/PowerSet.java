import java.util.ArrayList;
import java.util.List;

public class PowerSet {

	public static void main(String[] args) {

		int[] input = { 1, 2, 1 };
		List<List<Integer>> subsets = getSubsets(input);

		for (List<Integer> subset : subsets) {
			System.out.println(subset);
		}
	}

	public static List<List<Integer>> getSubsets(int[] input) {
		List<List<Integer>> list = new ArrayList<>();
		subsetsHelper(list, new ArrayList<>(), input, 0);
		return list;
	}

	private static void subsetsHelper(List<List<Integer>> list, List<Integer> resultList, int[] nums, int start) {
		list.add(new ArrayList<>(resultList));
		for (int i = start; i < nums.length; i++) {
			// add element
			resultList.add(nums[i]);
			// Explore
			subsetsHelper(list, resultList, nums, i + 1);
			// remove
			resultList.remove(resultList.size() - 1);
		}
	}

}
