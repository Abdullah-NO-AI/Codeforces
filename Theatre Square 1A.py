# Theatre Square 1A

n,m,a = list(map(int, input().strip().split()))
slab1=(n+a-1)//a
slab2=(m+a-1)//a
slab=slab1*slab2
print(int(slab))