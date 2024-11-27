# Source https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        sorted_frequency = sorted(frequency, key=lambda x: frequency[x], reverse=True)

        return sorted_frequency[:k]
    
# Time complexity: O(nlogn)
# Space complexity: O(n)