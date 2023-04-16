l_numero = [10,45,356,10,10,10,46,67,45,10,10,43,10,65,10,10]
l_numero.sort()
for numero in l_numero:
    if numero == 10:
        continue
    if numero == 356:
        break
    print(f"el valor es: {numero}")

 