// Last updated: 8/16/2026, 9:52:06 PM
/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    // public Node cloneGraph(Node node) {
    //     // BFS and skip visited nodes
    //     if(node == null) return null;

    //     Queue<Node> queue = new LinkedList<>();
    //     queue.offer(node);

    //     Map<Integer, Node> seen = new HashMap<>();
    //     seen.put(node.val, new Node(node.val));
        
    //     while (!queue.isEmpty()) {
    //         Node curr = queue.poll();
            
    //         if(curr.neighbors != null) {
    //             for(Node nei: curr.neighbors) {
    //                 // if not visited node before, add to queue and hashmap
    //                 if(!seen.containsKey(nei.val)) {
    //                     queue.offer(nei);
    //                     seen.put(nei.val, new Node(nei.val));
    //                 }

    //                 // append to cloned node's neighbors list
    //                 seen.get(curr.val).neighbors.add(seen.get(nei.val));
    //             }
    //         }
    //     }
    //     return seen.get(node.val);
    // }

    // DFS
    public Node cloneGraph(Node node) {
        return helper(node, new HashMap<Integer, Node>());
    }

    // return a cloned node
    private Node helper(Node node, HashMap<Integer, Node> seen) {
        if(node == null) return null;

        if(seen.containsKey(node.val)) return seen.get(node.val);

        Node newNode = new Node(node.val);
        seen.put(node.val, newNode);
        // add neighbors
        for(Node nei: node.neighbors) {
            newNode.neighbors.add( helper(nei, seen) );
        }
        return newNode;
    }
}