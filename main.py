from prettytable import PrettyTable, NONE
import sys
#Interfaz Inicial
def showMenu():
    menu = {
        "A": "Desayuno",
        "B": "Almuerzo",
        "C": "Cena"
    }
    table = PrettyTable()
    for codigo, items in menu.items():
        table.add_row([codigo, items + "             "])
    table.header=False
    table.align="l"
    table.horizontal_char=" "
    table.junction_char=" "
    table.hrules=NONE
    print("| ========================= |")
    print("|     RESTAURANTE S.A       |")
    print("|           MENÚ            |")
    print("| ========================= |")
    print(table)
    print("| D | ======= SALIR ======= |")
    print("| ========================= |")
    
    while True:
        opcion = input("Seleccione una categoria de menu: ").upper()
        if opcion == "A":
            showDesayuno()
            break
        elif opcion == "B":
            showAlmuerzo()
            break
        elif opcion == "C":
            showCena()
            break
        elif opcion == "D":
            print("Adios")
            sys.exit()
        else:
            print("Opcion Invalida, Intente de nuevo\n")
            showMenu()

#Interfaz Desayuno
def showDesayuno():
    desayuno = {
        "A": {"producto": "Café", "precio": 4.50},
        "B": {"producto": "Chocolate", "precio": 5.00},
        "C": {"producto": "Jugo de Fresas", "precio": 9.00},
        "D": {"producto": "Jugo de Papaya", "precio": 8.00},
        "E": {"producto": "Pan con Pollo", "precio": 7.00},
        "F": {"producto": "Pan con Jamón", "precio": 7.00},
        "G": {"producto": "Pan con Tortilla", "precio": 7.00},
    }

    table = PrettyTable()
    for codigo, item in desayuno.items():
        table.add_row([codigo, item["producto"], f"S/{item['precio']:.2f}"])

    table.header=False
    table.align="l"
    table.horizontal_char=" "
    table.junction_char=" "
    table.hrules=NONE
    print("|           Desayuno            |")
    print("| ============================= |")
    print(table)
    print("| j | ========= SALIR ========= |")
    print("| ============================= |")
    
    
    
    while True:
        opcion = input("Seleccione un desayuno: ").upper() 
        if opcion in desayuno:
            menu = desayuno[opcion]['precio']
            showBoleta(menu)
            break
        elif opcion == "J":
            print("Regresando a Menu")
            showMenu()
        else:
            print("Opcion Invalida, Intente de nuevo\n")
            showDesayuno()
    

#Interfaz Almuerzo    
def showAlmuerzo():
    almuerzo = {
        "A": {"producto": "Café", "precio": 4.50},
        "B": {"producto": "Chocolate", "precio": 5.00},
        "C": {"producto": "Jugo de Fresas", "precio": 9.00},
        "D": {"producto": "Jugo de Papaya", "precio": 8.00},
        "E": {"producto": "Pan con Pollo", "precio": 7.00},
        "F": {"producto": "Pan con Jamón", "precio": 7.00},
        "G": {"producto": "Pan con Tortilla", "precio": 7.00},
    }

    table = PrettyTable()
    for codigo, item in almuerzo.items():
        table.add_row([codigo, item["producto"], f"S/{item['precio']:.2f}"])

    table.header=False
    table.align="l"
    table.horizontal_char=" "
    table.junction_char=" "
    table.hrules=NONE
    print("|           Almuerzo            |")
    print("|===============================|")
    print(table)
    print("| j | ========= SALIR ========= |")
    print("| ============================= |")
    
    
    
    while True:
        opcion = input("Seleccione un almuerzo: ").upper()     
        if opcion in almuerzo:
            menu = almuerzo[opcion]['precio']
            showBoleta(menu)
            break
        elif opcion == "J":
            showMenu()
        else:
            print("Opcion Invalida, Intente de nuevo\n")
            showAlmuerzo()



#Interfaz Cena
def showCena():    
    cena = {
        "A":{"producto": "Pizza Exprés", "precio": 9.50},
        "B":{"producto": "Ensalada Campera", "precio": 7.50},
        "C":{"producto": "Gazpacho", "precio": 6.00},
        "D":{"producto": "Caldo de Gallina", "precio": 6.00},
        "E":{"producto": "Pollo al horno", "precio": 5.50},
        "F":{"producto": "Menestrón", "precio": 4.00},
    }
    
    table = PrettyTable()
    for codigo, item in cena.items():
        table.add_row([codigo, item["producto"], f"S/{item['precio']:.2f}"])
    table.header=False
    table.align="l"
    table.horizontal_char=" "
    table.junction_char=" "
    table.hrules=NONE
    print("|            Cena               |")
    print("| ============================= |") 
    print(table)
    print("| G | ========= SALIR ========= |")
    print("| ============================= |")
    
    while True:
        opcion = input("Seleccione una cena: ").upper()     
        if opcion in cena:
            menu = cena[opcion]['precio']
            showBoleta(menu)
            break
        elif opcion == "J":
            print("Adios")
            showMenu()
        else:
            print("Opcion Invalida, Intente de nuevo\n")
            showCena()

#Interfaz Boleta
def showBoleta(menu):
    #calculando el igv ademas de la suma total
    subtotal = menu - (menu * 0.18)
    IGV = menu * 0.18
    total = subtotal + IGV
    print("|       BOLETA DE VENTAS      |")
    print("| =========================== |") 
    print(f"| Subtotal       :   S/.{subtotal:.2f}  |")
    print(f"| IGV            :   S/.{IGV:.2f}  |")
    print(f"| Total a pagar  :   S/.{total:.2f}  |")
    print("|    Gracias por su compra    |")
    print("| =========================== |\n")
    



showMenu()
