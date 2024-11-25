# Source: https://leetcode.com/problems/valid-anagram/

# Approach 1: Sorting
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        return False

# Time complexity: O(nlogn)
# Space complexity: O(1)


#  Approach 2: Using Hash Map
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count = {}
        t_count = {}

        for i in range(len(s)):
            if s[i] in s_count:
                s_count[s[i]] += 1
            else:
                s_count[s[i]] = 1
            if t[i] in t_count:
                t_count[t[i]] += 1
            else:
                t_count[t[i]] = 1

        return s_count == t_count

# Time complexity: O(n)
# Space complexity: O(n)



