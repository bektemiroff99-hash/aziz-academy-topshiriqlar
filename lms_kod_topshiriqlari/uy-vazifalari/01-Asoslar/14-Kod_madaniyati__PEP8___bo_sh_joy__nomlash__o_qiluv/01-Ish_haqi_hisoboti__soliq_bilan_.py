soat = int(input())
stavka = int(input())
soliq = int(input())
yalpi = soat * stavka 
soliq_miqdori = yalpi * soliq // 100
sof = yalpi - soliq_miqdori
print(yalpi)
print(soliq_miqdori)
print(sof)