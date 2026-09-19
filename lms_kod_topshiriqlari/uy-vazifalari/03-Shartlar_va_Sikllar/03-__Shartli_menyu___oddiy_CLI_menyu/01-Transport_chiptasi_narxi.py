transport = int(input())
toifa = int(input())
if transport not in [1, 2, 3]:
    print("Notogri transport")
elif toifa not in [1, 2, 3]:
    print("Notogri toifa")
else:
    if transport == 1 or transport == 2:
        narx = 1700
    else:
        narx = 4000
    if toifa == 1:
        print(narx)
    elif toifa == 2:
        print(narx // 2)
    else:
        print(0)