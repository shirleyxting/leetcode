// Last updated: 8/16/2026, 9:49:33 PM
class Solution {
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        int n = accounts.size();
        UnionFind uf = new UnionFind(n);
        // email -> index of acc
        Map<String, Integer> emailToAcc = new HashMap<>();
        for(int i = 0; i < n; i ++) {
            List<String> acc = accounts.get(i);
            // skip the first string (name)
            for(int j = 1; j < acc.size(); j ++) {
                String e = acc.get(j);
                if (emailToAcc.containsKey(e)) {
                    // current 'e' already exist in one account before, union the 2 accounts
                    uf.union(i, emailToAcc.get(e));
                } else {
                    emailToAcc.put(e, i);
                }
            }
        }

        // index of acc -> list of emails
        Map<Integer, List<String>> emailGroup = new HashMap<>();
        emailToAcc.forEach((e, i) -> {
            int leader = uf.find(i);
            // if(emailGroup.containsKey(leader)) {
            //     emailGroup.get(leader).add(e);
            // } else {
            //     emailGroup.put(leader, new ArrayList<>(Arrays.asList(e)) );
            // }
            emailGroup.computeIfAbsent(leader, (x -> new ArrayList<>())).add(e);
        });

        // convert to results format
        List<List<String>> res = new ArrayList<>();
        emailGroup.forEach((i, emails) -> {
            String name = accounts.get(i).get(0);
            Collections.sort(emails);
            List<String> temp = new ArrayList<>();
            temp.add(name);
            temp.addAll(emails);
            res.add(temp);
        });

        return res;
    }
}

public class UnionFind {
    private int[] par;
    private int[] rank;

    public UnionFind(int n) {
        par = new int[n];
        rank = new int[n];

        for (int i = 0; i < n; i ++) {
            par[i] = i;
            rank[i] = 1;
        }
    }

    // find which group 'x' belongs to, take amortized const time
    public int find(int x) {
        int root = x;
        while(root != par[root]) root = par[root];
        // Path compression: compress the path back to root
        // this operatiaon gives amoritized const time
        while(x != root) {
            int next = par[x];
            par[x] = root;
            x = next;
        }
        return root;
    }

    // unify the groups containing x and y
    public void union(int x, int y) {
        int root1 = find(x);
        int root2 = find(y);
        // x and y already in same group
        if (root1 == root2) return;

        // merge smaller group into the larger one
        if (rank[root1] < rank[root2]) {
            par[root1] = root2;
            rank[root2] += rank[root1];
        } else {
            par[root2] = root1;
            rank[root1] += rank[root2];
        }
    }
}