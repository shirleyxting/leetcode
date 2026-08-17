// Last updated: 8/16/2026, 9:49:03 PM
class Solution {
    public int[][] kClosest(int[][] points, int k) {
        // // method 1 - self defined comparator, sort func
        // Arrays.sort(points, (a,b)->(a[0]*a[0]+a[1]*a[1]) - (b[0]*b[0]+b[1]*b[1]));
        // return Arrays.copyOfRange(points, 0, k);

    //     // method 2 - maintain a max-heap with size k
    //     // time O(nlogk), deal with realtime(online) stream data
    //     int n = points.length;
    //     int[][] res = new int[k][2];
    //     PriorityQueue<int[]> pq = new PriorityQueue<>(k, (a, b) -> (a[0]*a[0]+a[1]*a[1]) - (b[0]*b[0]+b[1]*b[1]));

    //     for(int i = 0; i < n; i ++) {
    //         int[] p = points[i];
    //         pq.add(p);
    //     }
    //     for(int i = 0; i < k; i ++) {
    //         res[i] = pq.poll();
    //     }
    //     return res;

        // method 3 - quick sort/quick select
        // [< pivot], pivot, [> pivot]
        // if pivot < k, continue until pivoy = k, return left side
        // time:o(n) ~ o(n^2)
        // disadvantage: not stable, not an online solution,
        // and return results are not SORTED
        int n = points.length, l = 0, r = n - 1;
        while(l < r) {
            int mid = helper(points, l, r);
            if(mid == k) break;
            if(mid < k) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return Arrays.copyOfRange(points, 0, k);
    }

    private int helper(int[][] points, int l, int r) {
        int[] pivot = points[l];
        while(l < r) {
            // find all r >= pivot, r--, until not satisfy
            while(l < r && compare(points[r], pivot) >= 0) r--;
            points[l] = points[r]; // move not-satify[r>=pivot] to left side

            // find all l <= pivot, l++, until not satisfy
            while(l < r && compare(points[l], pivot) <= 0) l++;
            points[r] = points[l]; // move not-satify[l<=pivot] to right side
        }
        points[l] = pivot;
        return l;
    }

    private int compare(int[] a, int[] b) {
        return (a[0]*a[0]+a[1]*a[1]) - (b[0]*b[0]+b[1]*b[1]);
    }
}