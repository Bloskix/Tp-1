palabra = "martia"
indice = 3
def caracter_perdido(str,n):
    str = str[:n] + (str[n+1:])
    return str
print(caracter_perdido(palabra,indice))