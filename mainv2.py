#importando el paquete sys, que se usa para cerrar el programa
import sys
#Interfaz Inicial
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
            #con esta linea se termina el programa, cuando el usuario asi lo quiera
            sys.exit()
        else:
            print("Opcion Invalida, Intente de nuevo\n")
            showMenu()
            
            
#Interfaz Desayuno
def showDesayuno():
    #Se crea el diccionario "desayuno" donde se pone la clave de cada opcion, y el producto con su respectivo precio
    desayuno = {
        "A": {"producto": "Café", "precio": 4.50},
        "B": {"producto": "Chocolate", "precio": 5.00},
        "C": {"producto": "Jugo de Fresas", "precio": 9.00},
        "D": {"producto": "Jugo de Papaya", "precio": 8.00},
        "E": {"producto": "Pan con Pollo", "precio": 7.00},
        "F": {"producto": "Pan con Jamón", "precio": 7.00},
        "G": {"producto": "Pan con Tortilla", "precio": 7.00},
    }
    
    print("|            Desayuno             |")
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
    
    
    
    while True:
        # la funcion.upper() convierte la letra ingresada por el usuario a mayuscula para no tener problemas con el case sentive del programa
        opcion = input("Seleccione un desayuno: ").upper() 
        
        # dentro de esta condicional se usa la palabra reservada ´in´ para verificar
        # sin el valor ingresado por el usuario este presente dentro del diccionario.
        if opcion in desayuno:
            #en la variable menú se guarda el resultado de buscar dentro del diccionario con la clave 'opcion' y el valor de 'precio'
            menu = desayuno[opcion]['precio']
            #se manda como parametro la variable 'menu' para poder calular la boleta.
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
