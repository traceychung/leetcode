'''
In this exercise, you will be working with the interviewer to create an "isPalindrome" function that will take in a string input and return a Boolean.

Definitions:
An Palindrome is a string that is read the same forward and/or backwards.

Requirements:
- O(1) Space complexity
- Ignore upper/lower cases
- Ignore Special characters. [e.g: ! @ # $ % ^ & * ( ) _ -]
- Can only utilize your choice of language's standard library
- You are not allowed to Google, but you can ask your interview for help.

You can assume that the input for this exercise will ALWAYS be a string.
'''

# def isPalindrome(s):
#     # s_lower = s.lower()
#     # if length of s is 0: return true
#     if len(s) <= 1:
#         return True
#     # two pointers - one at the beginning and one at the end
#     start = 0
#     end = len(s) -1
#     # keep moving pointers inward to see if the pairs match
#     while start <= end:
#         if not s[start].isalnum() and s[end].isalnum():
#             start += 1
#         if s[start].isalnum() and not s[end].isalnum():
#             end -= 1
#         if s[start].lower().isalnum() != s[end].lower().isalnum():
#             return False
#         else:
#             # s[start] != s[end]
#             start += 1
#             end -= 1

#     return True


# # print(isPalindrome("Racecar")) # return true
# # print(isPalindrome("racecar")) # return true
# # print(isPalindrome("!Mam")) # return true
# # print(isPalindrome("%mamm^")) # return false
# # print(isPalindrome("")) # return true
# # print(isPalindrome("bAab")) # return true
# # print(isPalindrome("a")) # return true
# # print(isPalindrome("1Aa1")) # return true

# print(isPalindrome(".,")) # return true
# print(isPalindrome("0p")) # return false
# print(isPalindrome(".a")) # return true


def isPalindrome(s):
    # s_lower = s.lower()
    # if length of s is 0: return true
    if len(s) <= 1:
        return True
    # two pointers - one at the beginning and one at the end
    start = 0
    end = len(s) -1
    # keep moving pointers inward to see if the pairs match
    while start <= end:
        if not s[start].isalnum():
            start += 1
        if not s[end].isalnum():
            end -= 1

        if start <= end and s[start].lower() != s[end].lower():
            return False

        start += 1
        end -= 1

    return True


print(isPalindrome("Racecar")) # return true
print(isPalindrome("racecar")) # return true
print(isPalindrome("!Mam")) # return true
print(isPalindrome("%mamm^")) # return false
print(isPalindrome("")) # return true
print(isPalindrome("bAab")) # return true
print(isPalindrome("a")) # return true
print(isPalindrome("1Aa1")) # return true

print(isPalindrome(".,")) # return true
print(isPalindrome("0p")) # return false
print(isPalindrome(".a")) # return true
