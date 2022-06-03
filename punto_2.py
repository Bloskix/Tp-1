mono_a = "si"
mono_b = "si"
def problemas_monos(a_sonriendo,b_sonriendo):
    if a_sonriendo == "si":
        a_sonriendo = True
    else:
        a_sonriendo = False
    print(a_sonriendo)
    if b_sonriendo == "si":
        b_sonriendo = True
    else:
        b_sonriendo = False
    print(b_sonriendo)
    if a_sonriendo == b_sonriendo:
        return True
    else:
        return False
print(problemas_monos(mono_a,mono_b))