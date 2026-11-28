# Halloumi Boxes 1903A

test = int(input())
for i in range(test):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr_c = sorted(arr)
    if arr == arr_c:
        print("YES")
    elif k >= 2:
        print("YES")
    else:
        print("NO")