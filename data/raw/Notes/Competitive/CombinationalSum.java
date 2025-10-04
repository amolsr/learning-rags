import java.util.ArrayList;
import java.util.*;

class CombinationalSum {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if (candidates == null || candidates.length == 0) {
            return result;
        }
        Arrays.sort(candidates);
        List<Integer> combination = new ArrayList<Integer>();
        dfs(candidates, combination, 0, target, result);
        return result;
    }

    public void dfs(int[] candidates, List<Integer> combination, int startIndex, int target,
            List<List<Integer>> result) {
        if (target == 0) {
            result.add(new ArrayList<>(combination));
            return;
        }
        for (int i = startIndex; i < candidates.length; i++) {
            if (candidates[i] > target) {
                break;
            }
            combination.add(candidates[i]);
            dfs(candidates, combination, i, target - candidates[i], result);
            combination.remove(combination.size() - 1);
        }

    }
}