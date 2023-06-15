"""
383. Ransom Note
Easy
3.9K
417
Companies
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran_letters = {}
        for letter in ransomNote:
            if letter not in ran_letters:
                ran_letters[letter] = 0
            ran_letters[letter]+= 1

        for m_letter in magazine:
            if m_letter in ran_letters:
                ran_letters[m_letter] -= 1

        for v in ran_letters.values():
            if v > 0:
                return False
        return True
