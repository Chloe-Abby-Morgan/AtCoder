N = int(input())
T = list(map(int, input().split()))
print(" ".join(map(str, list(i[0] for i in sorted(list(enumerate(T, start=1)), key=lambda x: x[1])[:3]))))
