a = input().strip()
b = input().strip()
c = set(a) & set(b)
if c:
    print("".join(sorted(c)))
else:
    print("BO'SH")