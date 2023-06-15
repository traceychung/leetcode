"""
844. Backspace String Compare
Easy
6.4K
292
Companies
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.



Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".


Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.


Follow up: Can you solve it in O(n) time and O(1) space?
"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_list = []
        t_list = []

        for char in s:
            if char == "#" and len(s_list) > 0:
                s_list.pop()
            elif char == "#" and len(s_list) == 0:
                continue
            else:
                s_list.append(char)

        for char in t:
            if char == "#" and len(t_list) > 0:
                t_list.pop()
            elif char == "#" and len(t_list) == 0:
                continue
            else:
                t_list.append(char)

        return s_list == t_list
