n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = v
min_k = min(d, key=d.get)
print(min_k
     )