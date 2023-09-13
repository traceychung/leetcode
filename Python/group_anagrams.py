"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a hashmap that holds the values of each unique word
        unique = {}

        # Loop through each string in each list
        for string in strs:
            #For each word in the list, sort it and add it to the dict as a key.
            sort = ''.join(sorted(string))

            #if it's in the dict then add the string to the value's list
            if sort in unique.keys():
                unique[sort].append(string)
            else:
                unique[sort] = [string]

        return unique.values()
