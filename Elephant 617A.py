# Elephant 617A

house = int(input())

steps = 0 

while house > 0:
    if house >= 5:
        house = house -5
        steps+=1
    elif house == 4:
        house = house -4
        steps+=1
    elif house == 3:
            house = house -4
            steps+=1
    elif house == 2:
            house = house -4
            steps+=1
    elif house == 1:
            house = house -4
            steps+=1

print(steps)