import os

seguir = True

base2 = {"10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"}

base = ["0", "1", "2", "3", "4", "5", "6", "7",
        "8", "9", "A", "B", "C", "D", "E", "F"]

letras = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}


def basenADec(num, bas):
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


def decABasen(num, bas):
    bin = ''
    while num // bas != 0:
        aux = num % bas
        if aux < 10:
            bin = str(aux)+bin
        else:
            bin = base[str(aux)]+bin
        num //= bas
    return str(num) + bin


def iniciar():
    try:
        b = int(input("ingrese base inicial (2 a 16): "))
        assert b > 1 and b < 17
        baseAConvertir(b)
    except (ValueError, AssertionError):
        print('Ingrese base valida')


def baseAConvertir(b):
    try:
        c = int(input("ingrese base a convertir (2 a 16): "))
        assert c > 1 and c < 17
        convertir(b, c)
    except (ValueError, AssertionError):
        print('Ingrese base valida')


def convertir(b, c):
    try:
        n = str(input(f"Ingresa el numero en base {b}: "))
        for x in n:
            if x not in base[:b]:
                raise ValueError
            d = basenADec(n, b)
        print(f"El número en base {c} es: {decABasen(d,c)}")
    except (ValueError):
        print('Ingrese numeros validos para dicha base')


def continuar():
    r = str(input('Presionar Y para continuar de lo contrario otra letra: '))
    if r == "Y":
        limpiar()
        return True
    else:
        return False


def limpiar():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


while seguir:
    iniciar()
    seguir = continuar()
