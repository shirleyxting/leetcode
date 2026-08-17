# Last updated: 8/16/2026, 9:53:46 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:
    # left: 0, right: n-1
    # find a quantity (width) that will change(increase/decrease) monotonically while pointers moving inward
    # then you can safely eliminate one boundry each step w/o missing the optimal pair
    # 这类"双指针从两端往中间收"的题，本质是找到一个"随着指针靠近会单调变化的量"（这里是宽度），用它来构造一个每一步都能安全排除一个候选的规则
    # 关键结构：面积 = 宽度 × min(两条线高度)，而"宽度"这个维度有单调性
    # 宽度 j - i 这个量有个很好的性质：只要两个指针不再往外扩（只能往中间收），宽度就会单调递减，永远不会变大。
    # 为什么"都从左边出发"不行——没有天然的"淘汰"逻辑
    # 如果两个指针都从左边出发（比如 left=0, right=1），然后想办法往右扩展，你会发现没有一个干净的规则能告诉你"这一步该扩大哪个指针，同时保证不会错过更优解"——因为宽度不再是单调变化的（你可能扩left也可能扩right，宽度变大变小都有可能，无法用一个简单规则安全地排除某些候选对），最终还是得靠某种嵌套式的搜索，绕不开 O(n²)。

        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            w = right - left
            h = min(height[left], height[right])
            max_area = max(max_area, w * h)

            # move shorter 'h'
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area