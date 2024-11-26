# Source https://leetcode.com/problems/group-anagrams/

# Approach 1: Categorize by Sorted String
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        def is_anagram(s1, s2):
            return sorted(s1) == sorted(s2)
        
        result = []
        for word in strs:
            added = False
            for group in result:
                if is_anagram(word, group[0]):
                    group.append(word)
                    added = True
                    break
            if not added:
                result.append([word])
        return result

# Time complexity: O(n^2 * mlogm) where n is the number of strings and m is the maximum length of a string
# Space complexity: O(n)


# Approach 2: Using Hashing
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = {}
        for word in strs:
            key = tuple(sorted(word))
            if key in result:
                result[key].append(word)
            else:
                result[key] = [word]
        return list(result.values())

# Time complexity: O(n * mlogm) where n is the number of strings and m is the maximum length of a string
# Space complexity: O(n)