# Last updated: 8/30/2026, 8:04:51 PM
1class Solution:
2    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
3        # union find
4        # for acc: union all emails with the first email
5
6        parent = {}         # email -> parent email
7        email_to_name = {}  # email -> name
8
9        def find(x):
10            while x != parent[x]:
11                parent[x] = parent[parent[x]]   # path halving
12                x = parent[x]
13            return x
14        
15        def union(x, y):
16            rx, ry = find(x), find(y)
17            parent[rx] = ry
18        
19        
20        for name, *emails in accounts:
21            # 1: every email as own group, and record its name
22            for email in emails:
23                email_to_name[email] = name
24                if email not in parent:
25                    parent[email] = email   # new email: self as root
26            
27            # 2: union every email in account with the first email
28            for email in emails[1:]:
29                union(email, emails[0])
30
31        # 3: group by root email
32        groups = defaultdict(list)  # root email -> [e1, e2, e3, ..] (inclduing root eamil itself)
33        for email in parent:
34            root = find(email)
35            groups[root].append(email)
36        
37        # 4: sort emails in graoups[root], find name by email_to_name[root]
38        res = []
39        for root, emails in groups.items():
40            name = email_to_name[root]
41            res.append( [name] + sorted(emails) )
42        
43        return res
44