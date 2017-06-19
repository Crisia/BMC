from random import randrange
from numpy.random import choice
from random import randint

#Generador de hileras de ADN
def generarRandom(tamano):
    basesADN = ['A', 'G', 'T', 'C']
    weights = [0.25, 0.25, 0.25, 0.25]
    hileraResultado=""
    cont =0
    if tamano > 0:
        while (cont< tamano):
            hileraResultado =hileraResultado +choice(basesADN, p=weights)
            cont = cont +1
    return hileraResultado

def generarBases(pA,pG,pT,pC, tamano):
    sumaProbabilidades= pA+pG+pT+pC
    hileraResultado = ""
    cont = 0
    if sumaProbabilidades == 1.0 and tamano > 0:
        basesADN = ['A', 'G', 'T', 'C']
        weights = [pA, pG, pT, pC]
        if tamano > 0:
            while (cont < tamano):
                hileraResultado = hileraResultado + choice(basesADN, p=weights)
                cont = cont + 1

        print("El valor de la base A: "+str(pA)+", base G: "+str(pG) +", base T: "+str(pT)+", base C: "+str(pC))
        return hileraResultado
    else:
        return ("Verificar probabilidades ya que deben de sumar 1")

def fuenteRepeatUser(hileraBase,hileraRepeat):
    if len(hileraRepeat) < len(hileraBase):
        return True
    else:
        print("La subHilera debe de ser menor a "+ str(len(hileraBase)))
        return False

def fuenteRepeatRandom(hileraBase,tamano):
    if len(hileraBase) > tamano:
        posicionRandom=randint(0, len(hileraBase)-1)
        nuevahilera=hileraBase[posicionRandom::]
        if tamano <= len(nuevahilera):
            nuevahileraRepeat = nuevahilera[:tamano]
            return nuevahileraRepeat
        else:
            return fuenteRepeatRandom(hileraBase, tamano)
    else:
        return "El tamano" + str(tamano)+ "debe ser menor a:" + str(len(hileraBase))
##En este caso es el usurio el que inserta el repeat
def insertarRepeatUser(hileraBase,repeat):
    print("Recordar que este viene x un archivo")


def insertarRepeatUser(hilera, repeat, posRepeat,distancia,cantidadRepeat):
    cont=0
    suma=0
    hileraAux= hilera
    tamanoRepeat=len(repeat)
    hileraResultado=""
    while cont < cantidadRepeat:
        if cont==0 and distancia <len(hilera):
            suma = posRepeat+distancia+tamanoRepeat-1
            hileraValoresFuturos=hileraAux[posRepeat-1::]
            hileraValoresAnteriores=hileraAux[:posRepeat-1]
            hileraResultado=hileraValoresAnteriores+repeat+hileraValoresFuturos
            cont = cont+1
        elif len(hileraResultado)>suma:
            hileraValoresFuturos = hileraResultado[suma::]
            hileraValoresAnteriores = hileraResultado[:suma]
            hileraResultado = hileraValoresAnteriores + repeat + hileraValoresFuturos
            suma = suma + tamanoRepeat + distancia
            cont = cont + 1
        else:
            break
    return hileraResultado




print(fuenteRepeatRandom("ABCCCCGTTTT",3))
insertarRepeatUser("ABCDEFGH", "000", 4,3,6)


def distanciaRepeatRandom(hileraBase):
    numRandom = randint(1, 10)
    if len(hileraBase) > numRandom:
        return numRandom
    else :
        return distanciaRepeatRandom(hileraBase)



