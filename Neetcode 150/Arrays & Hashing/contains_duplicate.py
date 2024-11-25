# Source: https://leetcode.com/problems/contains-duplicate/

# Approach 1: Sorting
class Solution:
    def hasDuplicate(self, nums) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
    
# Time complexity: O(nlogn)
# Space complexity: O(1)


# Approach 2: Using Hash Set
class Solution:
    def hasDuplicate(self, nums) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
# Time complexity: O(n)
# Space complexity: O(n)