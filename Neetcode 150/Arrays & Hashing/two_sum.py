# Source: https://leetcode.com/problems/two-sum/description/

# Approach 1: Brute Force
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Time complexity: O(n^2)
# Space complexity: O(1)


# Approach 2: Using Hash Map
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i in range(len(nums)):
            if target - nums[i] in seen:
                return [seen[target - nums[i]], i]
            seen[nums[i]] = i

# Time complexity: O(n)
# Space complexity: O(n)