hora_prohibidas = [21,22,23,24,1,2,3,4,5,6,7]
hour = 21
speaking = "si"
def problema_loro (hablando,hora):
    if (hora in hora_prohibidas):
        hora = True
    else:
        hora = False
    if hablando == "si":
        hablando = True
    else:
        hablando = False
    if (hablando and hora) == True:
        return True
    else:
        return False
print(problema_loro(speaking,hour))

