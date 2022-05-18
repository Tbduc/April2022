while True:
    dane = input("POdaje liczbe: ")
    try:
        print(int(dane))
        break
    except ValueError:
        print("podaj jescze raz")
        
        
c = 0
while True:
    dane = input("Podaje liczbe: ")
    if c >= 10:
        break
    try:
        print(int(dane))
        break
    except ValueError:
        c += 1
        print("podaj jescze raz")