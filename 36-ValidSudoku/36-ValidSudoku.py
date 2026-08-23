# Last updated: 8/23/2026, 12:30:53 PM
1class Solution:
2    def isValidSudoku(self, board: List[List[str]]) -> bool:
3        # check duplicates in row, col, 3*3 box
4        # convert (r, c) -> 3*3 box_id
5        #  (r//3)*3 + (c//3)
6
7        rows = defaultdict(set)     # row_id -> (visited nums)
8        cols = defaultdict(set)     # col_id -> (visited nums)
9        boxes = defaultdict(set)    # box_id -> (visited nums)
10
11        for i in range(len(board)):
12            for j in range(len(board[0])):
13                num = board[i][j]
14                if num == ".":
15                    continue
16                
17                box_id = (i//3) * 3 + (j//3)
18                if num in rows[i] or num in cols[j] or num in boxes[box_id]:
19                    return False
20                
21                # record legit visited num
22                rows[i].add(num)
23                cols[j].add(num)
24                boxes[box_id].add(num)
25        
26        return True
27                