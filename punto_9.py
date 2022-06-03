ejemplo = "no hace"
def no_cadena(word):
    if "no " in word:
        return word
    else:
        return "no" + " " + word
print(no_cadena(ejemplo))