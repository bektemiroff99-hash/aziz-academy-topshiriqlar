s = input().strip()
d = {}
for harf in s:
    d[harf] = d.get(harf, 0) + 1 
for harf in sorted(d):
    print(f"{harf}={d[harf]}")