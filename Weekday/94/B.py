N,K = list(map(int,input().split()))
A = list(map(int,input().split()))
windows = []
curr = 0
left,right = 0,0

while right < N:
    if right-left == K:
        windows.append(curr)
        
    if right-left < K:
        curr += A[right]
        right += 1
    elif right-left >= K:
        curr -= A[left]
        left += 1
windows.append(sum(A[-K:]))   
print(windows)  
print(max(windows)-min(windows))

