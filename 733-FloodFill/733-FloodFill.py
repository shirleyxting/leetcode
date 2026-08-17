# Last updated: 8/16/2026, 9:49:30 PM
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # # BFS state change, from curr_color -> color
        # curr_color = image[sr][sc]
        # if curr_color == color: return image

        # m, n = len(image), len(image[0])
        # dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        
        # queue = deque()
        # queue.append([sr, sc])

        # while queue:
        #     curr = queue.popleft()
        #     # make the color change
        #     image[curr[0]][curr[1]] = color

        #     # find next nodes
        #     for dir in dirs:
        #         i = curr[0] + dir[0]
        #         j = curr[1] + dir[1]
        #         if i >= 0 and i <= m-1 and j >= 0 and j <= n-1 and image[i][j] == curr_color: 
        #             queue.append([i,j])
        # return image

        # DFS - recursion (slower)
        old_color = image[sr][sc]
        if old_color == color: return image

        self._helper(image, sr, sc, old_color, color)
        
        return image

    def _helper(self, image: List[List[int]], i: int, j: int, old_color: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]

        if i >= 0 and i <= m-1 and j >= 0 and j <= n-1 and image[i][j] == old_color: 
            # make the color (state) change
            image[i][j] = color 
            # iterate over next possibilities
            for dir in dirs:
                ii = i + dir[0]
                jj = j + dir[1]
                self._helper(image, ii, jj, old_color, color)

        return image