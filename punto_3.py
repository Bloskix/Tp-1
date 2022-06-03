a = 3
b = 3
def suma_doble(num1,num2):
    if num1 == num2:
        ans = (num1 + num2) * 2
    else:
        ans = num1 + num2
    return ans
print(suma_doble(a,b))