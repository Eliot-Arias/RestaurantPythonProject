#Interfaz inicial:
def showMenu():
    print("| ========================= |")
    print("|     RESTAURANTE S.A       |")
    print("|           MENÚ            |")
    print("| ========================= |")
    print("| A | Desayuno              |")
    print("| B | Almuerzo              |")
    print("| C | Cena                  |")
    print("| D | ======= SALIR ======= |")
    print("| ========================= |")

#Se crea el diccionario "desayuno" donde se pone la clave de cada opcion, el producto con su respectivo precio y la cantidad
desayuno = {
    "A": {"producto": "Café", "precio": 4.50, "cantidad" : 0},
    "B": {"producto": "Chocolate", "precio": 5.00, "cantidad" : 0},
    "C": {"producto": "Jugo de Fresas", "precio": 9.00, "cantidad" : 0},
    "D": {"producto": "Jugo de Papaya", "precio": 8.00, "cantidad" : 0},
    "E": {"producto": "Pan con Pollo", "precio": 7.00, "cantidad" : 0},
    "F": {"producto": "Pan con Jamón", "precio": 7.00, "cantidad" : 0},
    "G": {"producto": "Pan con Tortilla", "precio": 7.00, "cantidad" : 0},
}

#Se crea el diccionario "almuerzo" donde se pone la clave de cada opcion, el producto con su respectivo precio y la cantidad
almuerzo = {
        "A": {"producto": "Café", "precio": 4.50, "cantidad" : 0},
        "B": {"producto": "Chocolate", "precio": 5.00, "cantidad" : 0},
        "C": {"producto": "Jugo de Fresas", "precio": 9.00, "cantidad" : 0},
        "D": {"producto": "Jugo de Papaya", "precio": 8.00, "cantidad" : 0},
        "E": {"producto": "Pan con Pollo", "precio": 7.00, "cantidad" : 0},
        "F": {"producto": "Pan con Jamón", "precio": 7.00, "cantidad" : 0},
        "G": {"producto": "Pan con Tortilla", "precio": 7.00, "cantidad" : 0},
    }

#Se crea el diccionario "cena" donde se pone la clave de cada opcion, el producto con su respectivo precio y la cantidad
cena = {
        "A":{"producto": "Pizza Exprés", "precio": 9.50, "cantidad" : 0},
        "B":{"producto": "Ensalada Campera", "precio": 7.50, "cantidad" : 0},
        "C":{"producto": "Gazpacho", "precio": 6.00, "cantidad" : 0},
        "D":{"producto": "Caldo de Gallina", "precio": 6.00, "cantidad" : 0},
        "E":{"producto": "Pollo al horno", "precio": 5.50, "cantidad" : 0},
        "F":{"producto": "Menestrón", "precio": 4.00, "cantidad" : 0},
    }
def showDesayuno():    
    
    while True:
        print("|            Desayuno             |")
        print("| =============================== |")
        print("| A | Café              | S/ 4.50 |")
        print("| B | Chocolate         | S/ 5.00 |")
        print("| C | Jugo de Fresas    | S/ 9.00 |")
        print("| D | Jugo de Papaya    | S/ 8.00 |")
        print("| E | Pan con Pollo     | S/ 7.00 |")
        print("| F | Pan con Jamón     | S/ 7.00 |")
        print("| G | Pan con Tortilla  | S/ 7.00 |")
        # for codigo, item in desayuno.items():
        #     print(f"| {codigo} | {item['producto']} | S/ {item['precio']:.2f} |")
        print("| j | ========== SALIR ========== |")
        print("| =============================== |")
        opcion = input("Seleccione un desayuno (A - G) o J para salir: ").upper()         
        if opcion in desayuno:
            cantidad = int(input(f"Cuant@s {desayuno[opcion]['producto']} desea?"))
            desayuno[opcion]['cantidad'] = cantidad
        elif opcion == "J":
            print("Regresando a Menu")
            break
        else:
            print("Opcion Invalida, Intente de nuevo\n")
    totalMenu = sum(item['precio'] * item['cantidad'] for item in desayuno.values())
    showBoleta(totalMenu)
    
def showAlmuerzo():
    
    while True:
        print("|            Almuerzo             |")
        print("| =============================== |")
        print("| A | Café              | S/ 4.50 |")
        print("| B | Chocolate         | S/ 5.00 |")
        print("| C | Jugo de Fresas    | S/ 9.00 |")
        print("| D | Jugo de Papaya    | S/ 8.00 |")
        print("| E | Pan con Pollo     | S/ 7.00 |")
        print("| F | Pan con Jamón     | S/ 7.00 |")
        print("| G | Pan con Tortilla  | S/ 7.00 |")
        print("| j | ========== SALIR ========== |")
        print("| =============================== |")
        opcion = input("Seleccione un Almuerzo (A - G) o J para salir: ").upper()         
        if opcion in almuerzo:
            cantidad = int(input(f"Cuant@s {almuerzo[opcion]['producto']} desea?"))
            almuerzo[opcion]['cantidad'] = cantidad
        elif opcion == "J":
            print("Regresando a Menu")
            break
        else:
            print("Opcion Invalida, Intente de nuevo\n")
    totalMenu = sum(item['precio'] * item['cantidad'] for item in almuerzo.values())
    showBoleta(totalMenu)


def showCena():
    while True:
        print("|              Cena               |")
        print("| =============================== |")
        print("| A | Pizza Exprés      | S/ 9.50 |")
        print("| B | Ensalada Campera  | S/ 7.50 |")
        print("| C | Gazpacho          | S/ 6.00 |")
        print("| D | Caldo de Gallina  | S/ 6.00 |")
        print("| E | Pollo al horno    | S/ 5.50 |")
        print("| F | Menestrón         | S/ 4.00 |")
        print("| G | ========== SALIR ========== |")
        print("| =============================== |")
        opcion = input("Seleccione una Cena (A - F) o J para salir: ").upper()         
        if opcion in cena:
            cantidad = int(input(f"Cuant@s {cena[opcion]['producto']} desea?"))
            cena[opcion]['cantidad'] = cantidad
        elif opcion == "J":
            print("Regresando a Menu")
            break
        else:
            print("Opcion Invalida, Intente de nuevo\n")
    totalMenu = sum(item['precio'] * item['cantidad'] for item in cena.values())
    showBoleta(totalMenu)

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
    
    

while True:
    showMenu()
    option = input("Seleccione una categoria de menu ( A - C ): ").upper()
    if option == "A":
        showDesayuno()
        break
    elif option == "B":
        showAlmuerzo()
        break
    elif option == "C":
        showCena()
        break
    else:
        print("Opcion Invalida, Intente de nuevo")




