ids = set(map(int, input().split()))
banned = set(map(int, input().split()))
_ = input()  
c = ids - banned
if c:
    print(*sorted(c))
else:
    print("BO'SH")