N, K = map(int, input().split())
total = 0
years = 0

while total < K:
    total += N+years
    years += 1

print(years-1)