s = input()
d = {}
for harf in s:
    if harf in d:
        d[harf] += 1
    else:
        d[harf] = 1
res = []
for harf, son in d.items():
    res.append(f"{harf}:{son}")
print(" ".join(res))