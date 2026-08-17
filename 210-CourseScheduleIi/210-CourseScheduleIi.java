// Last updated: 8/16/2026, 9:51:14 PM
class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        // find cycle in directed graph, topological sort - DFS
        // next ligitable node will be pushed to the head of the order -> Stack, LIFO
        Stack<Integer> order = new Stack<>();

        // build graph[i] = adajacent nodes of i / next ready courses
        List<List<Integer>> graph = new ArrayList<>();
        for(int i = 0; i < numCourses; i ++) graph.add(new ArrayList<>());

        for(int[] pair: prerequisites) {
            graph.get(pair[1]).add(pair[0]);
        }
        System.out.println(graph);
        // marked[]: T-processed already, F-not processed so far
        boolean[] marked = new boolean[numCourses];

        // status[]: 0-unknown, 1-visiting, 2-visited
        int[] status = new int[numCourses];

        for(int i = 0; i < numCourses; i ++) {
            if (!marked[i]) {
                if( !dfs(graph, status, i, order) ) return new int[0]; // cycle found, false
                marked[i] = true;
            }
        }

        int[] res = new int[numCourses];
        for(int i = 0; i < numCourses; i ++) res[i] = order.pop();
        return res;
    }

    private boolean dfs(List<List<Integer>> graph, int[] status, int i, Stack<Integer> order) {
        if(status[i] == 1) return false; // cycle found
        if(status[i] == 2) return true; // visited before

        // mark current node-i as visiting
        status[i] = 1;

        // iterate adjacent nodes of i
        for(int j : graph.get(i)) {
            if( !dfs(graph, status, j, order) ) return false; // if node-j found cycle, false
        }

        // mark node-i as visited
        status[i] = 2;
        // add visited node to Stack-order
        order.push(i);
        return true;
    }
}