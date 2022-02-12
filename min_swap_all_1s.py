'''
https://practice.geeksforgeeks.org/problems/minimum-swaps-required-to-group-all-1s-together2451/1/# 

Minimum Swaps required to group all 1s together 
Easy Accuracy: 35.86% Submissions: 1635 Points: 2
Given an array of 0’s and 1’s, we need to write a program to find the minimum number of swaps required to group all 1’s present in the array together.

Example 1:

â€‹Input : arr[ ] = {1, 0, 1, 0, 1}
Output : 1
Explanation:
Only 1 swap is required to group all 1's together. 
Swapping index 1 and 4 will give arr[] = {1, 1, 1, 0, 0}.

â€‹Example 2:

Input : arr[ ] = {1, 0, 1, 0, 1, 1} 
Output :  1
 

Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function minSwaps() that takes an array (arr), sizeOfArray (n) and return the minimum number of swaps required and if no 1's are present print -1. The driver code takes care of the printing.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
'''

def minSwaps (arr, n) : 
    if arr.count(0) == len(arr):
        return -1 
        
    #Complete the function
    k = arr.count(1) #window size
    
    numZero = arr[0:k].count(0) #first window
    minSwap = numZero
    
    j = 0
    for i in range(k, n):
        if arr[j] == 0:
            numZero -= 1
        if arr[i] == 0:
            numZero += 1
        minSwap = min(minSwap, numZero)
        j += 1
        
    return minSwap 
  
  
