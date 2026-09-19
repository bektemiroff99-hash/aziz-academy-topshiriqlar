n = int(input())
d = {}
for _ in range(n):
    word = input().strip()
    d[word] = d.get(word, 0) + 1 
target = input().strip()
print(d.get(target, 0))