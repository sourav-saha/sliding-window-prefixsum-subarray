'''
Given an array A of N integers, find the maximum subarray sum of size K and minimum subarray sum of size K and output the difference between them.

Input Format

First line of each test case contains T, no. of test cases.
First line of each test case contains N, K
Second line of each test case contains N integers

Constraints


Output Format

For each test case, print the difference between the max(sum of subarrays of size K) - min(sum of subarrays of size K).

Sample Input 0

1
6 3
5 6 -1 4 6 7
Sample Output 0

8
Explanation 0

For the first test case, all subarrays of size k
(5, 6, -1) = 10
(6, -1, 4) = 9
(-1, 4, 6) = 9
(4, 6, 7) = 17

Max - Min = 17 - 9 = 8
''' 



def findDifference(arr, n, k):
  maxSum = 0 
  minSum = 0 
  curSum = 0
  #first window 
  for i in range(0, k):
    curSum += arr[i]
  maxSum = minSum = curSum 
  
  #sliding window 
  j = 0 
  for i in range(k, n):
    curSum -= arr[j]
    curSum += arr[i]
    maxSum = max(maxSum, curSum)
    minSum = min(minSum, curSum)
    j += 1 
  
  return (maxSum-minSum)

if __name__ == "__main__":
  T = int(input().strip())
  for ti in range(T):
    n, k = map(int, input().strip().split(' '))
    arr = list(map(int, input().strip().split(' ')))
    print(findDifference(arr, n, k))
    
