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
    
    




def selectMenu(menu_dict, menu_name):
    selected_items = []
    
    while True:
        print(f"|            {menu_name:11}             |")
        print("| ================================== |")
        for codigo, item in menu_dict.items():
            print(f"| {codigo} | {item['producto']:20} | S/ {item['precio']:.2f} |")
        print("| S | Terminar selección             |")
        print("| ================================== |")
        opcion = input(f"Seleccione {menu_name} (A - G) o 'S' para terminar: ").upper()
        
        if opcion in menu_dict:
            cantidad = int(input(f"Cuant@s {menu_dict[opcion]['producto']} desea? "))
            menu_dict[opcion]['cantidad'] = cantidad
            selected_items.append(menu_dict[opcion])
        elif opcion == "S":
            print("Terminando selección")
            break
        else:
            print("Opcion Invalida, Intente de nuevo\n")
            
    totalMenu = sum(item['precio'] * item['cantidad'] for item in selected_items)
    showBoleta(totalMenu)
    

while True:
    showMenu()
    option = input("Seleccione una categoria de menu ( A - C ) o 'D' para salir: ").upper()
    if option == "A":
        selectMenu(desayuno, "Desayuno")
    elif option == "B":
        selectMenu(almuerzo, "Almuerzo")
    elif option == "C":
        selectMenu(cena, "Cena")
    elif option == "D":
        print("Adios")
        break
    else:
        print("Opcion Invalida, Intente de nuevo")

