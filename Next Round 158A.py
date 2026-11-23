# Next Round 158A

n , k = map(int, input().split())
nxt = 0

score = list(map(int, input().split()))
cutoff = score[k-1]
for i in score:
    if i >= cutoff and i > 0:
        nxt += 1

print(nxt)



