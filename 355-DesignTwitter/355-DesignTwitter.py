# Last updated: 9/2/2026, 12:16:35 PM
1# need a global time counter to order tweets
2# the tweets list sent by every userId, is sorted naturally
3# maintain a maxHeap with size K, where K = count of followed + user itself
4# everytime we needs getNewsFeed, we pop from maxHeap, until reach 10 tweets, 
5# pop 1 tweet then push 1 tweet from same userId if not empty
6
7class Twitter:
8
9    def __init__(self):
10        self.time = 0   # global timer
11        self.tweets = defaultdict(list)     # userId -> [(time, tweet1), (time, t2), ..]
12        self.following = defaultdict(set)  # userId -> following users set(u1, u2, u3...)
13        
14
15    def postTweet(self, userId: int, tweetId: int) -> None:
16        self.tweets[userId].append((self.time, tweetId))
17        # do not forget the timer (+ 1 whenever there is a new tweet)
18        self.time += 1
19
20        
21    def getNewsFeed(self, userId: int) -> List[int]:
22        # maintain maxHeap with size <= K (# of following + itself)
23        # fan out on read
24
25        # build heap for curr userId
26        heap = []
27        # get user list = following + itself
28        users = self.following[userId] | {userId}
29        for uid in users:
30            if self.tweets[uid]:    # edge case, ensure uid has at least 1 tweet
31                # push the last idx, the latest tweet into heap
32                idx = len(self.tweets[uid]) - 1
33
34                t_time, t_id = self.tweets[uid][idx]
35
36                # maxHeap order by tweet time, save next possible idx
37                data = (-t_time, t_id, uid, idx - 1)
38                heapq.heappush(heap, data)
39        
40        # pop at most 10 tweets from maxHeap
41        res = []
42        while heap and len(res) < 10 :
43            neg_time, t_id, uid, idx = heapq.heappop(heap)
44            res.append(t_id)
45
46            # push uid's next tweets if available
47            if idx >= 0:    # uid has earilier tweets
48                t_time, t_id = self.tweets[uid][idx]
49                data = (-t_time, t_id, uid, idx - 1)
50                heapq.heappush(heap, data)
51        
52        return res
53
54
55    def follow(self, followerId: int, followeeId: int) -> None:
56        if followeeId is not None and followerId != followeeId:
57            self.following[followerId].add(followeeId)
58        
59
60    def unfollow(self, followerId: int, followeeId: int) -> None:
61        if followeeId in self.following[followerId]:
62            # check exists to avoid raise ValuerError
63            self.following[followerId].remove(followeeId)
64        
65
66
67# Your Twitter object will be instantiated and called as such:
68# obj = Twitter()
69# obj.postTweet(userId,tweetId)
70# param_2 = obj.getNewsFeed(userId)
71# obj.follow(followerId,followeeId)
72# obj.unfollow(followerId,followeeId)