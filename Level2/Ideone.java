import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.IntStream;
 
class Ideone {
    public static final int[] answer(int height, int[] nodes) {
        int[] ans = new int[nodes.length];
        Map<Integer, Integer> indices = new HashMap<>();
        IntStream.range(0, nodes.length).forEachOrdered(i -> indices.put(nodes[i], i));
        int next = postOrder(height, 0, 0, indices, ans);
        if (next < 0) {
            int i = indices.get(-next);
            ans[i] = -1;
        }
        return ans;
    }
 
    private static int postOrder(int limit, int depth, int next, Map<Integer, Integer> indices, int[] ans) {
        if (depth == limit) {
            return next;
        }
        // left
        int left = postOrder(limit, depth + 1, next, indices, ans);
        next = left < 0 ? -left : left;
        int right = postOrder(limit, depth + 1, next, indices, ans);
        next = right < 0 ? -right : right;
 
        int me = next + 1;
 
        if (left < 0) {
            int i = indices.get(-left);
            ans[i] = me;
        }
        if (right < 0) {
            int i = indices.get(-right);
            ans[i] = me;
        }
 
        return indices.containsKey(me) ? -me : me;
 
    }
 
    public static void main(String[] args) {
        testRun(3, new int[] { 7, 3, 5, 1 }, new int[] { -1, 7, 6, 3 });
        testRun(5, new int[] { 19, 14, 28 }, new int[] { 21, 15, 29 });
    }
 
    private static void testRun(int height, int[] input, int[] output) {
        int[] ans = answer(height, input);
        System.out.printf("Input height %d and nodes %s:\n%s\n%s\n", height, Arrays.toString(input),
                Arrays.toString(ans), Arrays.toString(output));
    }
 
}