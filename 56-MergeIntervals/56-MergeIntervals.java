// Last updated: 8/16/2026, 9:53:08 PM
// class Solution {
//     public int[][] merge(int[][] intervals) {
//         if (intervals.length == 1) return intervals;
//         Arrays.sort(intervals, (a, b)->a[0]-b[0]);
//         Stack<int[]> stack = new Stack<>();
//         stack.push(intervals[0]);

//         for (int[] interval: intervals) {
//             int[] curr = stack.pop();
//             if (interval[0] > curr[1]) { 
//                 // no overlap
//                 stack.push(curr.clone());
//                 stack.push(interval.clone());
//             } else {
//                 // overlap
//                 curr[1] = Math.max(curr[1], interval[1]);
//                 stack.push(curr.clone());
//             }
//         }
//         int size = stack.size();
//         // System.out.println("stack.size = " + size);
//         // int[][] res = new int[size][2];
//         // for(int p = size - 1; p >= 0; p --) 
//         //     res[p] = stack.pop().clone();
//         // return res;
//         return stack.toArray(new int[size][2]);
//     }
// }

// No need to use Stack to keep track of the current interval
// we can directly modify/update the current inveral value
class Solution {
	public int[][] merge(int[][] intervals) {
		if (intervals.length <= 1)
			return intervals;

		// Sort by ascending starting point
		Arrays.sort(intervals, (a, b) -> a[0]-b[0]);

		List<int[]> result = new ArrayList<>();
		result.add(intervals[0]);
		for (int[] interval : intervals) {
            int[] curr = result.get(result.size()-1);
			if (interval[0] <= curr[1]) 
                // Overlapping intervals, change curr values
				curr[1] = Math.max(curr[1], interval[1]);
			else {                             
                // Disjoint intervals, add the new interval to the list
				result.add(interval);
			}
		}

		return result.toArray(new int[result.size()][]);
	}
}