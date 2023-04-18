print("--------pizzeria los pollos hermanos--------")
saldo = int(input("ingrese monto disponible\n"))
lista_ingredientes =[]
pchica = 6999
pgrande = 10000
pfamiliar = 14000
saldoR = 0
peperoni = 500
extra_queso = 1300
chile = 400
eleccionp = int(input("que pizza desea llevar:\n1--pizza tamaño chica\n2--pizza tamaño grande\n3--pizza tamaño familiar\n ingrese el numero correspondiente\n"))
if eleccionp < 1 or eleccionp > 3:
    print("eleccion invalida ejecuta el programa nuevamente")

match eleccionp:
    case 1:
        saldoR = saldo - pchica
        print(f"usted eligio pizza tamaño chica la cual tiene el valor de :${pchica}")
        print(f"su saldo restante es:${saldoR}")
    case 2:
        saldoR = saldo - pgrande
        print(f"usted eligio pizza tamaño grande la cual tiene el valor de :${pgrande}")
        print(f"su saldo restante es:${saldoR}")
    case 3:
        saldoR = saldo - pgrande
        print(f"usted eligio pizza tamaño familiar la cual tiene el valor de :${pfamiliar}")
        print(f"su saldo restante es:${saldoR}")

elecingre = str(input("¿desea añadir ingredientres? estos tienen un costo adicional!!!\ny--para añadir ingredientes\nn--para no\n"))
addingre = "y"

if elecingre == "y":   
    while addingre == "y": 
        ingred = int(input("¿cuales de los siguientes ingredientes desea añadir?\n1--peperoni\n2--extra queso\n3--chile\n"))
        match ingred :
            case 1:
                saldoR -= peperoni
                print(f"usted eligio perperoni su saldo restante es:${saldoR}")
                lista_ingredientes.append("peperoni")
            case 2:
                saldoR -= extra_queso
                print(f"usted eligio extra queso su saldo restante es:${saldoR}")
                lista_ingredientes.append("extra queso")
            case 3:
                saldoR -= chile
                print(f"usted eligio chile su saldo restante es:${saldoR}")
                lista_ingredientes.append("chile")
        addingre = input("¿desea añadir otro ingrediente?\ny--para seguir añandiendo\nn--para no añadir mas")




