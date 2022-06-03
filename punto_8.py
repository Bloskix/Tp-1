x = -8
y = -9
neg = False
def pos_neg(num1,num2,negativo):
    if negativo == False and (num1 < 0 ^ num2 < 0):
        return True
    elif negativo == True and (num1 < 0 and num2 < 0):
        return True
    else:
        return False
print(pos_neg(x,y,neg))

