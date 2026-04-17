M,D = list(map(int, input().split()))
festivals = [(1,7),(3,3),(5,5),(7,7),(9,9)]
print("Yes" if (M,D) in festivals else "No")