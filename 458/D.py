import statistics

X = int(input())
Q = int(input())
A,B = [],[]
board = [X]
for i in range(Q):
    x = input().split()
    A.append(int(x[0]))
    B.append(int(x[1]))

for i in range(Q):
    board.append(A[i])
    board.append(B[i])
    print(statistics.median(board))