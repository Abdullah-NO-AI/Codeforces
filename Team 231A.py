# Team 231A

n = int(input())

problem = []
for i in range(n):
    confidence = list(map(int, input().split()))
    problem.append(confidence)

result  = 0
for confidence in problem:
    if (confidence[0]+confidence[1]+confidence[2]) >= 2:
        result +=1

print(result)