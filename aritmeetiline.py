#IrisMariaRohelpuu

sisestus = ""
i=0

while sisestus != "stop":
    sisestus = int(input("Palun sisesta üks hinne: "))
    if sisestus != "stop":
        print("ma ütsin " + str("stop"))
    hinne = (i + sisestus) / 2