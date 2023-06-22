"""
Implement a simple text editor. The editor initially contains an empty string, S. 
Perform Q operations of the following 4 types:

1 - append(W) - Append string W to the end of S.
2 - delete(k) - Delete the last k characters of S.
3 - print(k) - Print the k'th character of S.
4 - undo() - Undo the last (not previously undone) operation of type 1 or 2, 
    reverting S to the state it was in prior to that operation.

Sample:
Sample input:
8
1 abc
3 3
2 3
1 xy
3 2
4
4
3 1

Sample output:
c
y
a
"""

Q = int(input())
S = ""

history = []
history.append(S)

for q in range(Q):

    line = str(input())
    line = line.split(" ")
    operation = line[0]
    if(int(operation) != 4):
        param = line[1]

    if(int(operation) == 1):
        S = S + str(param)
        history.append(S)
    
    if(int(operation) == 2):
        S = S[:-int(param)]
        history.append(S)

    if(int(operation) == 3):
        print(S[int(param)-1])
    
    if(int(operation) == 4):
        S = history[-2]
        history.pop()
