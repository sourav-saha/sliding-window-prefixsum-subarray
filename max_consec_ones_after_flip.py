'''
https://leetcode.com/problems/max-consecutive-ones-iii/

very good vairable sized sliding window problem

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
''' 

class Solution:
    def longestOnes(self, arr: List[int], k: int) -> int:
        cz = maxans = 0 #count zero
        start = end = 0
        n = len(arr)

        while end < n:
            if arr[end] == 0:
                cz += 1

            #shrink if required
            while cz > k:
                if arr[start] == 0:
                    cz -= 1
                start += 1

            #calculate the length of substring at each pass and store in max if applicable
            #because it's guaranteed every time start & end will have valid substring
            maxans = max(maxans, end-start+1)
            end += 1

        return maxans
