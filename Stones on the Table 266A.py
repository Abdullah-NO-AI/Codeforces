# Stones on the Table 266A

count = int(input())
colour_order = input()
current = colour_order[0]
removed = 0
for stone in colour_order[1:]:
    if stone == current:
        removed+=1
    elif stone != current:
        current = stone
print(removed)

