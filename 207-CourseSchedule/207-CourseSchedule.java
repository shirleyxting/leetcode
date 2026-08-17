// Last updated: 8/16/2026, 9:51:24 PM
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // if there is a cycle in directed graph
        // topological sort via DFS
        boolean[] marked = new boolean[numCourses];
        // graph[i] = all adjacent nodes / prerequisites
        List<List<Integer>> graph = new ArrayList<>();
        for(int i = 0; i < numCourses; i ++) graph.add(new ArrayList<Integer>());

        for(int[] pair: prerequisites) {
            graph.get(pair[0]).add(pair[1]);
        }
        System.out.println(graph);

        // status: 0-unknown, 1-visiting, 2-visited
        int[] status = new int[numCourses];

        for(int i = 0; i < numCourses; i ++) {
            if(!marked[i]) {
                if(!dfs(graph, status, i)) return false;
                // if dfs return false, means cycle found, return false

                marked[i] = true;
            }
        }
        return true;
    }

    private boolean dfs(List<List<Integer>> graph, int[] status, int i) {
        if(status[i] == 1) return false; // meet visiting nodes, has cycle, return false
        if(status[i] == 2) return true; // already visited this node-i before, no cycle

        // mark node-i as visiting
        status[i] = 1;
        // iterate node-i adjacent nodes
        for(int j: graph.get(i)) {
            if( !dfs(graph, status, j) ) return false;
            // if found cycle, return false
        }

        // finish checking, mark node-i as visited
        status[i] = 2;
        return true;
    }
}