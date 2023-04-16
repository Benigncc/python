edad = int(input("introduzca su edad:\n"))
respuesta = None
if edad >= 18:
        print("usted es mayor de edad, puede comprar alcohol ¿cual desea llevar? introduzca")
        respuesta = input("1-ron.\n2-whisky.\n3-ginebra.\n")

        if respuesta == "1":
            print("usted a elegido ron")
        elif respuesta == "2":
            print("usted a elegido whisky")
        elif respuesta == "3":
            print("usted a elegido ginebra")
        else:
            print("opcion no valida")
else:
     print("no es mayor de edad no puede compara alcohol")



     