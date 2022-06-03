dias_de_la_semana = ["lunes","martes","miercoles","jueves","viernes"]
day= "lunes"
holidays = "no"
def dormimos (dia_semana,vacaciones):
    if (dia_semana in dias_de_la_semana):
            dia_semana = True
    else:
            dia_semana = False
    if vacaciones == "si":
        vacaciones = True
    else:
        vacaciones = False
    if dia_semana == False or vacaciones == True:
        return True
    else:
        return False
print(dormimos(day,holidays))


