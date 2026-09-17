n = int(input())
d = {}
for _ in range(n):
    soz = input()
    if soz in d:
        d[soz] += 1
    else:
        d[soz] = 1 
max_soz = max(d, key=d.get)
print(max_soz)