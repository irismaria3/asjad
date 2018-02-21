#IrisMariaRohelpuu

f = open("arvud.txt", encoding = "UTF-8-SIG")

for a in f:
    arv = int(a.strip())
    ferh = arv * 1.8 + 32
    print("Celsius:", arv, "Fahrenheit:",round(ferh, 2))


