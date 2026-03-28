N = int(input())
rList = []

for i in range(1,N+1):
    rList.append(str(i))

print(",".join(rList[::-1]))