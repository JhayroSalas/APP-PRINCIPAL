while(True):
    try:
        numero= int(input("Ingrese un año: "))
        resultado= "NO ES BISIESTO"
        if(numero % 4 == 0 and numero % 100 != 0) or (numero % 400 == 0):
            resultado= "ES BISIESTO"
    except:
        print("Error al ingresar el año")
    else:
        print("El año {}, {}".format(numero, resultado))
        break
    finally:
        print("Fin de la busqueda.")