numero = 21
def diferencia(num):
    if num > 21:
        cuenta = (num - 21) * 2
    else:
        cuenta = 21 - num
    return cuenta
print(diferencia(numero))