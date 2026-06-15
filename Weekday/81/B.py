N = int(input())
dv = [map(int,input().split()) for i in range(N)]
stack = []
strength,gold = 0,0

def postpone():
    global strength,gold
    
    while stack:
        if stack[-1][0] <= strength:
            strength += stack[-1][0]
            gold += stack[-1][1]
            stack.pop()
        else:
            return
    return
        
for health, reward in dv:
    if health <= strength:
        strength += health
        gold += reward
        postpone()
    else:
        stack.append((health,reward))

print(gold)