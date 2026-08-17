// Last updated: 8/16/2026, 9:48:57 PM
class Solution {
    /*
    public int findJudge(int n, int[][] trust) {
        // judge cannot be the a_i
        // judge should be 'n-1' paris of b_i
        // if trust size < n-1, then no judge
        int len = trust.length;
        if(len < n - 1) return -1;
        if(n == 1) return 1;
        
        // aCountMap: b people -> count of a people who trust b
        // bCountMap: a people -> count of b people whom a trusts
        // if aCountMap.val = n-1 
        //  && bCountMap.val = 0 (i.e. cannot find the key in bCountMap) 
        // -> a judge
        Map<Integer, Integer> aCountMap = new HashMap<Integer, Integer>();
        Map<Integer, Integer> bCountMap = new HashMap<Integer, Integer>();
        for(int i = 0; i < len; i ++) {
            aCountMap.merge(trust[i][1], 1, (a, b) -> a+b);
            bCountMap.merge(trust[i][0], 1, (a, b) -> a+b);
        }
        System.out.println(aCountMap);
        System.out.println(bCountMap);

        for(int people : aCountMap.keySet()) {
            if (aCountMap.get(people) == n - 1 
                && !bCountMap.containsKey(people)) {
                return people;
            }
        }
        return -1;
    }
    */

    // use 2 vectors to record the in-degree and out-degree
    // find in-degree = n-1 && out-degree = 0 -> judge
    public int findJudge(int n, int[][] trust) {
        int[] in = new int[n+1]; // we will only use index >=1
        int[] out = new int[n+1];

        for (int[] pair : trust) {
            in[pair[1]] ++;
            out[pair[0]] ++;
        }
        for (int i = 1; i < n + 1; i ++) {
            if (in[i] == n-1 && out[i] == 0) return i;
        }
        return -1;
    }
}