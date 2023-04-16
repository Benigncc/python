print("---calculadora---")
print("1-suma")
print("2-resta")
print("3-multiplicar")
print("4-dividir")
print("5-elevar")

eleccion = int(input("ingresa el numero\n"))
match eleccion:
    case 1: 
        print("usted eligio sumar")
        num1 = float(input("ingrese el primer numero\n"))
        num2 = float(input("ingrese el segundo numero\n"))
        resultado = round(num1 + num2,2) 
        print(resultado,)
    case 2:     
        print("ha elegido resta")
        num1 = float(input("ingrese el primer numero\n"))
        num2 = float(input("ingrese el segundo numero\n"))
        resultado = round(num1 - num2,2) 
        print(resultado)
    case 3:
        print("ha elegido multiplicar")
        num1 = float(input("ingrese el primer numero\n"))
        num2 = float(input("ingrese el segundo numero\n"))
        resultado = round(num1 * num2,2) 
        print(resultado)
    case 4:
        print("ha elegido division")
        num1 = float(input("ingrese el primer numero\n"))
        num2 = float(input("ingrese el segundo numero\n"))
        resultado = round(num1 / num2,2) 
        print(resultado)
    case 5:
        print("ha elegido elevar")
        num1 = float(input("ingrese el primer numero\n"))
        num2 = float(input("ingrese el segundo numero\n"))
        resultado = round(num1 ** num2,2)
        print(resultado)
    case _:
        print("eleccion no valida")
 