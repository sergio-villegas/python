"""
In the first line insert N the size of the array and M the number of operation
The next line is the array with a N size
The next M lines you give the solutions for each sum in base of the index (first number)
and the second number is the sum expected and the output gives the index where the sum
from the first number to the sum is completed.

Note: Each sum is guaranteed that exist in each operation

Sample input:
10 2
3 6 10 3 5 2 8 1 9 2
1 24
4 27

Sample output:
4
9
"""

import sys

firstLine = str(input())
firstLine = firstLine.split(" ")
N = firstLine[0]
M = firstLine[1]

arr = str(input())
arr = arr.split(" ")

if(len(arr) > int(N) or len(arr) < int(N)):
    sys.exit()

for number in range(int(M)):
    line = str(input())
    line = line.split(" ")
    startingIndex = line[0]
    sumExpexted = line[1]

    sumatoria = 0

    for num in range(int(startingIndex), (len(arr))):
        sumatoria = sumatoria + int(arr[num])
        if(sumatoria == int(sumExpexted)):
            print(str(num))
