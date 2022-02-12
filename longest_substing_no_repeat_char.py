'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/

Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # empty string
        if len(s) == 0:
            return 0
        
        # all same element
        if s.count(s[0]) == len(s):
            return 1
        
        l = r = 0
        maxlen = 0
        my_dict = {}
        while r < len(s):
            if s[r] not in my_dict:
                my_dict[s[r]] = True 
                maxlen = max(maxlen, len(my_dict))
                r += 1
            else: #duplicate
                del my_dict[s[l]]
                l += 1
                
        return maxlen
      
      
