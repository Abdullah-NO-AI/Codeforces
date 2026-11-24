# Soldier and bananas 546A

k, n, w = map(int, (input().split()))
cost = 0
for i in range (w+1):
    cost += i*k
debt = n - cost

if debt > 0:
    print("0")
else:
    print(debt*-1)