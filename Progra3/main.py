from generadorHilera import *
import utilitario



def main():
    salir = False



    while salir == False:
        global HileraBase
        global repeat

        print("1. Cargar hilera")
        print("2. Generar hilera Random")
        print("3. Generar hilera Bases desiguales")
        print("4. Generar Repeat")
        print("5. Generar Repeat Sistema")
        print("6. Insertar Repeat en la Hilera")
        print("7. Alineamiento Con Función de Afin de Costo por Gap")
        print("8. Alineamiento Global con Espacio Lineal")
        opc = str(input(">>"))
        if opc == "1":
            hileraBase = utilitario.cargarHilera()
            print(hileraBase)
        elif opc == "2":
            tamano=int(input("Ingrese el tamano de la hilera"))
            hileraBase = generarRandom(tamano)
            print(hileraBase)
        elif opc == "3":
            baseA = float(input("Ingrese el valor para la base A"))
            baseG = float(input("Ingrese el valor para la base G"))
            baseT = float(input("Ingrese el valor para la base T"))
            baseC = float(input("Ingrese el valor para la base C"))
            tamano = float(input("Ingrese el tamano de la hilera"))
            hileraBase=generarBases(baseA,baseG,baseT,baseC,tamano)
            print(hileraBase)

        elif opc == "4":
            repeat=utilitario.cargarHilera()
            print(repeat)

        elif opc == "5":
            k = int(input("Ingrese el tamaño del repeat"))
            print(hileraBase)
            repeat=fuenteRepeatRandom(hileraBase,k)
            print(repeat)

        elif opc == "6":
            posRepeat = int(input("Ingrese el la posicion donde iniciará el repeat"))
            distancia = int(input("Ingrese el la distancia entre los repeat"))
            cantidadRepeat = int(input("Ingrese el la cantidad de repeat"))
            hileraResultado=insertarRepeatUser(hileraBase, repeat, posRepeat, distancia, cantidadRepeat)
            print("Hilera Base: "+ hileraBase)
            print("Hilera Repeat: " + repeat )
            print("Resultado: "+hileraResultado)
        elif opc == "#salir":
            salir = True


main();