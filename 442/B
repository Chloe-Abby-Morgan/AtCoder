Q = int(input())
A = []
volume = 0
playing = False

for i in range(Q):
    A.append(int(input()))

for i in A:
    if i == 1:
        volume += 1
    elif i == 2 and volume > 0:
        volume -= 1
    elif i == 3:
        playing = not playing

    if volume >= 3 and playing:
        print("Yes")
    else:
        print("No")