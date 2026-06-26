A = set(input().strip().split())
B = set(input().strip().split())
C = A & B 
print(len(C))
for name in sorted(C):
    print(name)