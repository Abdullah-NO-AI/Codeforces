# Domino Piling 50A

m, n = map(int, input().split())
space = m*n
domino = 0
if m%2 ==0 or n%2 ==0:
    domino = space/2
else:
    domino = ((space-1)/2)

print(int(domino))