# Beautiful Matrix 263A
matrix = []
for i in range(5):
    given = list(map(int, input().split()))
    matrix.append(given)

position = []
for row in range(5):
    for element in range(5):
        if matrix[row][element] == 1:
            position.extend([row, element])

x = 2
y = 2

turns = abs(position[0]- x) + abs(position[1] - y)

print(turns)