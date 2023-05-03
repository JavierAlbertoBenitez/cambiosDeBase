import os


base = {"10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"}

seguir = True


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


def convertir(b):
    try:
        i = int(input("ingrese el numero en base 10: "))
        assert i >= 0
        print(f"el numero en la base {b} es : {decABasen(i, b)}")
    except:
        print('Solo numeros >=0')


def iniciar():
    try:
        b = int(input("ingrese base (2 a 16): "))
        assert b > 1 and b < 17
        convertir(b)
    except (ValueError, AssertionError):
        print('Ingrese base valida')


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
