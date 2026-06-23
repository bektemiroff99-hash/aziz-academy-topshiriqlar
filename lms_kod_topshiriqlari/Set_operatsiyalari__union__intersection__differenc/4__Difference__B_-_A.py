a = set(map(int, input().split()))
b = set(map(int, input().split()))
c = b - a 
if c:
    print(*sorted(c))
else:
    print("BO'SH")