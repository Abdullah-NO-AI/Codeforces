# Bit++ 282A

n = int(input())
x = 0

statement = []
for i in range(n):
    sequence = list(input())
    statement.append(sequence)

for sequence in statement:
    if '+' in sequence:
        x += 1
    else:
        x -= 1
        
print(x)
