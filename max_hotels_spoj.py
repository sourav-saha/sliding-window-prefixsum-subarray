'''
https://www.spoj.com/problems/HOTELS/en/

:Varoiable size sliding window:

There are N hotels along the beautiful Adriatic coast. Each hotel has its value in Euros.

Sroljo has won M Euros on the lottery. Now he wants to buy a sequence of consecutive hotels, such that the sum of the values of these consecutive hotels is as great as possible - but not greater than M.

You are to calculate this greatest possible total value.

Input
In the first line of the input there are integers N and M (1 ≤ N ≤ 300 000, 1 ≤ M < 231).

In the next line there are N natural numbers less than 106, representing the hotel values in the order they lie along the coast.

Output
Print the required number (it will be greater than 0 in all of the test data).

Example
input
5 12
2 1 3 4 5
output
12
	input
4 9
7 3 5 6
output
8
'''


def maxValue(arr, n, m)->int:
	start = end = 0
	maxans = cursum = 0
	while(end<n):
		cursum += arr[end]
		
		#shrink logic
		while cursum > m:
			cursum -= arr[start]
			start += 1

		#store the length
		maxans = max(maxans, cursum)
		end += 1

	return maxans

if __name__ == "__main__":
	n, m = map(int, input().strip().split(' '))
	arr = list(map(int, input().strip().split(' ')))
	print(maxValue(arr, n, m))
