a = set(map(int, input().split()))
b = set(map(int, input().split()))
c = a ^ b
if c:
    print(*sorted(c))
else:
    print("BO'SH")