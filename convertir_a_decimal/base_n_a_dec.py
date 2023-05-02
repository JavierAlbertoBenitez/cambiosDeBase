import os

base = ["0", "1", "2", "3", "4", "5", "6", "7",
        "8", "9", "A", "B", "C", "D", "E", "F"]

letras = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

continuar = True


def binADec(num, bas):
    dec = 0
    x = 0
    num = num[::-1]
    for i in num:
        if i in base[:9]:
            dec += int(i) * bas**x
        else:
            dec += letras[i]*bas**x
        x += 1
    return dec


def convertir(b):
    try:
        n = str(input("Ingresa el numero en base b: "))
        for x in n:
            if x not in base[:b]:
                raise ValueError
        print(f"El numero en base DEC es {binADec(n,b)}")
    except (ValueError):
        print('Ingrese numeros validos para dicha base')


def iniciar():
    try:
        b = int(input('Ingrese base (de 2 a 16): '))
        if b < 2 or b > 16:
            raise ValueError
        convertir(b)
    except (ValueError, AssertionError):
        print('Ingrese una base valida')


def seguir():
    r = str(input('Presionar Y para continuar de lo contrario otra letra: '))
    if r == "Y":
        os.system("cls")  # os.system("clear") fuera de android
    else:
        continuar = False


while continuar:
    iniciar()
    r = str(input('Presionar Y para continuar de lo contrario otra letra: '))
    if r == "Y":
        os.system("cls")  # os.system("clear") fuera de windows
    else:
        continuar = False
