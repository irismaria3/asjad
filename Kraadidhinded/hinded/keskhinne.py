#IrisMariaRohelpuu

f = open("hinded.txt", encoding = "UTF-8-SIG")
summa = 0
loendur = 0

for a in f:
    hinne = int(a.strip())
    summa += hinne
    loendur += 1

aritmeetiline = summa / loendur
print("Keskmiseks hindeks on", str(round(aritmeetiline, 1)))