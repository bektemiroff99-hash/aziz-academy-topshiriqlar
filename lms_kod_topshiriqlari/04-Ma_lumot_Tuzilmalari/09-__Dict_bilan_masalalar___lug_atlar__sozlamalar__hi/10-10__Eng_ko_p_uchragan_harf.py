soz = input()
d = {}
for harf in soz:
    if harf in d:
        d[harf] += 1
    else:
        d[harf] = 1
max_harf = max(d, key=d.get)
print(max_harf)