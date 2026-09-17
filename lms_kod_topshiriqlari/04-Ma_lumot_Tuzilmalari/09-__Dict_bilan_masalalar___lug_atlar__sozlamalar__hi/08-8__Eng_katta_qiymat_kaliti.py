n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)
max_k = max(d, key=d.get)
print(max_k)