# Way Too Long Words 71A

n = int(input())

list = []
for i in range(n):
    list.append(str(input()))

for word in list:
    if len(word) > 10:
        print(f"{word[0]}{len(word[1:len(word)-1])}{word[-1]}")
    else:
        print(word)
