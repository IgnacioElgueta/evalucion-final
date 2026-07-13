def Mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Stock por plataforma")
    print("2. Búsqueda de juegos por rango de precio")
    print("3. Actualizar precio de juego")
    print("4. Agregar juego")
    print("5. Eliminar juego")
    print("6. Salir")
    print("=====================================")

def Leer_menu():

    Mostrar_menu()
    while True:

        try:
            opcion = int(input("Elige una de las 6 opciones\n"))

            if opcion < 1 or opcion > 6:
                print("Error, elige un numero del 1 al 6")
                return opcion
            
            else:
                break
        except Exception:
            print("Error, solo debe contener numeros, no letras")
            return Mostrar_menu()
            

def precio_juego(precio):
    
    if precio <= 0:
        return False
    return True

def stock_juego(stock):

    if stock < 0:
        return False
    return True

def codigo(codigo):

    if codigo.strip() == "":
        return False
    return True

def titulo(titulo):
    if titulo.strip() == "":
        return False
    return True

def platadorma(plataforma):
    if plataforma.strip() == "":
        return False
    return True

def genero(genero):
    if genero.strip() == "":
        return False
    return True


def clasificacion(clasificacion):

    if clasificacion == "M" or clasificacion == "E" or clasificacion == "T":
        return True
    return False

def multiplayer(multiplayer):

    multiplayer = input("Escribe 's' o 'n' ")

    if multiplayer == "s" or multiplayer == "n":
        return True
    return False

def editor(editor):
    if editor.strip() == "":
        return False
    return True

def stock_plataforma(plataforma):

    if (len(plataforma)) == 0:
        print("No se encuentra ningun juego en stock")
        return
    
    else:
        plataforma = input("¿Que plataforma?\n")

def agregar_juego(juego):

    codigo = input("Ingrese código del juego\n")
    if codigo(codigo) == False:
        print("Error, no puede estar vacio")
        return   
    else:
        print(f"Codigo creado con exito como {codigo}") 
    
    titulo = input("Ingresa el titulo del juego\n")
    if titulo(titulo) == False:
        print("Error, no puede estar vacio")
        return

    plataforma = input("Ingrese la plataforma\n")
    if plataforma(plataforma) == False:
        print("Error, no puede estar vacio")
        return

    genero = input("Ingrese género\n")
    if genero(genero) == False:
        print("Error, no puede estar vacio")
        return
    
    clasificacion = input("Ingrese la clasificacio 'E' 'T' 'M'\n").upper
    if clasificacion(clasificacion) == False:
        print("Error, las unicas opciones son: E, T, M")
        return
    
    multiplayer = input("¿Es multiplayer? (s/n)\n")
    if multiplayer(multiplayer) == False:
        print("Error, solo se puede 's' o 'n'")
        return
    
    editor = input("Ingrese editor\n")
    if editor(editor) == False:
        print("Error, no puede estar vacio")
        return

    precio = int(input("Ingrese precio\n"))
    if precio(precio) == False:
        print("Error, debe ser un numero entero mayor a 0")
        return

    stock = int(input("Ingrese stock\n"))
    if stock(stock) == False:
        print("Error, debe ser un Número entero mayor o igual a cero")
        return
    
    ficha = {
        "codigo": codigo,
        "titulo": titulo,
        "plataforma": plataforma,
        "genero": genero,
        "clasificacion": clasificacion,
        "multiplayer": multiplayer,
        "editor": editor,
        "precio": precio,
        "stock": stock
    }
    juego.append(ficha)

    inventario = {
         "codigo": codigo [precio] [stock]
    }
    juego.append(inventario)

def buscar_juego(juego):

    for i in range(len(juego)):
        if juego[i]["titulo"] == buscar_juego:
            return i
    return -1

def eliminar_juego(juego):
    
    eliminar = input("Que juego desea eliminar\n")
    posicion = buscar_juego(juego,eliminar)

    if posicion == -1:
        print("no se encuentra ningun juego")
        return
    else:
        del posicion[eliminar]

def actualizar_precio(codigo):
    if (len(codigo)) == 0:
        codigo = False
    else:
        codigo = True


juego = []

while True:

    opcion = Leer_menu()

    opcion = int(input("Elige una de las 6 opciones\n"))

    if opcion == 1:
        pass
    elif opcion == 2:
        
        buscar = input("¿Que juego busca?\n")
        if buscar == buscar_juego(juego):
            print(f"El juego a sidoencontradocomo {buscar}")
        else:
            print("el juego no se encuentra")

    elif opcion == 3:
       actualizar_precio(codigo)
    elif opcion == 4:
        agregar_juego(juego)

    elif opcion == 5:
        eliminar_juego(juego)
    
    elif opcion == 6:
        print("Programa finalizado.")
        break
    