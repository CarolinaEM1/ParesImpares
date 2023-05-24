#Hacer un programa que pida dos números y se de cuenta cuál de ellos es par o si ambos lo son

num1 = int(input("Digite un número"))
num2 = int(input("Digite otro número"))

if num1%2==0 and num2%2==0:
    print("Ambos números son pares :)")
elif num1%2==0 and num2%2!=0:
    print(f"{num1} el primer número es par")
elif num1%2!=0 and num2%2==0:
    print(f"{num2} el segundo número es par")
else:
    print("Ambos números son impares")

#Carolina EM :)