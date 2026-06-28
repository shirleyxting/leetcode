# Last updated: 6/28/2026, 3:04:46 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        # loweercase letters -> each string has a count res: int[26]
4        # map: key: int[26] count, value: List[index]
5
6        anagram_map = {}
7        for i, s in enumerate(strs):
8            cnt = [0] * 26
9            for c in s:
10                cnt[ord(c) - ord('a')] += 1
11            anagram_map.setdefault(tuple(cnt), []).append(i)
12        
13        # res = []
14        # for i, (cnt, indices) in enumerate(anagram_map.items()):
15        #     res.append([strs[idx] for idx in indices])
16        
17        # return res
18        
19        # only map.values() is used, so just iterate values()
20        return [[strs[i] for i in indices] for indices in anagram_map.values()]
21
22