lista_numeros = [10, 45, 55, 76]
print(f"el valor mas pequeño en la lista es el {lista_numeros[0]} y el valor mas grande es el {lista_numeros[3]}")

lista_colores = ["rojo","azul","verde","amarillo"]
print(lista_colores[1][2])

lista_colores = ["rojo","azul","verde","amarillo"]
color1 = input("ingrsa el color que va antes del rojo\n")
lista_colores.insert(0,color1)
color2 = input("ingresa el color que va ultimo\n")
lista_colores.append(color2)
color3 = input("ingresa el color que va entre el azul y verde\n")
lista_colores.insert(3,color3)
print(lista_colores)


lista_colores = ["gris", "rojo", "azul", "naranja", "verde", "amarillo", "rosa"]
print(lista_colores)
lista_colores.pop(1)
print(lista_colores)
lista_colores.pop(3)  
print(lista_colores)
lista_colores.pop(3)
print(lista_colores)


lista_colores = ["rojo","azul","verde","amarillo"]
lista_colores2 = lista_colores.copy()
print(lista_colores2)