x = 10
y = 5
def hacer10(num1,num2):
    if num1 == 10 or num2 ==10:
        return True
    elif num1 + num2 == 10:
        return True
    else:
        return False
print(hacer10(x,y))