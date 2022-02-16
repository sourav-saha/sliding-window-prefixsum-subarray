'''
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

https://leetcode.com/problems/contiguous-array/

Explain: https://www.youtube.com/watch?v=fjZ1-Iz576U
'''

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        #replace the 0s with -1s, so that sum of equal no. of 0s and 1s becomes zero
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1 
                
        prefixSumNums = [0]*len(nums)
        my_dict = {}
        
        prefixSumNums[0] = nums[0]
        my_dict[prefixSumNums[0]] = 0 #store the first index of the occurance of prefixSumNums[i]
        
        maxL = 0
        for i in range(1, len(nums)):
            prefixSumNums[i] = prefixSumNums[i-1] + nums[i]
            if prefixSumNums[i] == 0:
                subArrayL = i+1 #nums[0:i] subarray range
                maxL = max(maxL, subArrayL)
            elif prefixSumNums[i] in my_dict:
                subArrayL = i - my_dict[prefixSumNums[i]]
                maxL = max(maxL, subArrayL)
            else:
                my_dict[prefixSumNums[i]] = i 
                
        return maxL 
