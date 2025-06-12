# https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/
from typing import List


class Solution:

    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(current_index, current_xor):
            self.result += current_xor

            for i in range (current_index , len(nums)):
                next_xor = current_xor ^ nums[i]
                dfs(i+1 , next_xor)

        self.result = 0

        dfs(0,0)

        return self.result

