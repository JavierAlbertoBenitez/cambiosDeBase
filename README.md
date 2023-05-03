# cambios De Base

el [programa](https://github.com/JavierAlbertoBenitez/cambiosDeBase/blob/main/conversor.py) sirve para convertir cualquier número entero positivo de una base comprendida entre 2 a 16 a otra base comprendida en el mismo intervalo.

para esto primero solicita la base inicial y luego la partida para finalmente preguntar el numero que deseamos convertir, es cual es convertido a decimal como se observa en el primer código

```Python
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
```

y luego transforma el retorno de esta a la base solicitada a traves del siguiente código

```Python

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
```
