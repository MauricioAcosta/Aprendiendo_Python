
num1=int(input("num1:" ))
num2=int(input("num2:" ))
num3=int(input("num3:" ))
if num1<num2 and num1<num3:
    print("Numero menor ", num1)
else:
    if num2<num3:
        print("Numero menor ",num2)
    else:
        print("Numero menor ",num3)
print("-")
if num1>num2 and num1>num3:
    print("Numero mayor",num1)
else:
    if num2>num3:
        print("Numero mayor",num2)
    else:
        print("Numero mayor",num3)
