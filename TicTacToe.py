"""
    Programa: Tic Tac Toe en Python
    
    Judador vs Maquina 
    
    Autor: Sergio Alejandro Villegas Ferruzca
"""
from enum import Enum
from operator import index

# Clase Enum para definir el contenido posible de una celda en el tablero
class ContenidoCelda(Enum):
    CIRCULO = "O"
    EQUIS = "X"
    VACIO = " "

# Verifica si alguien ya gano
def ganador(tablero, contenido):
    # Primera vertical
    if(tablero[8] == contenido and tablero[5] == contenido and tablero[2] == contenido):
        return True
    if(tablero[8] == contenido and tablero[2] == contenido and tablero[5] == contenido):
        return True
    if(tablero[5] == contenido and tablero[2] == contenido and tablero[8] == contenido):
        return True
    # Segunda vertical
    if(tablero[7] == contenido and tablero[4] == contenido and tablero[1] == contenido):
        return True
    if(tablero[7] == contenido and tablero[1] == contenido and tablero[4] == contenido):
        return True
    if(tablero[4] == contenido and tablero[1] == contenido and tablero[7] == contenido):
        return True
    # Tercera vertical
    if(tablero[6] == contenido and tablero[3] == contenido and tablero[0] == contenido):
        return True
    if(tablero[6] == contenido and tablero[0] == contenido and tablero[3] == contenido):
        return True
    if(tablero[3] == contenido and tablero[0] == contenido and tablero[6] == contenido):
        return True
    # Primera horizontal
    if(tablero[8] == contenido and tablero[7] == contenido and tablero[6] == contenido):
        return True
    if(tablero[8] == contenido and tablero[6] == contenido and tablero[7] == contenido):
        return True
    if(tablero[7] == contenido and tablero[6] == contenido and tablero[8] == contenido):
        return True
    # Segunda horizontal
    if(tablero[5] == contenido and tablero[4] == contenido and tablero[3] == contenido):
        return True
    if(tablero[5] == contenido and tablero[3] == contenido and tablero[4] == contenido):
        return True
    if(tablero[4] == contenido and tablero[3] == contenido and tablero[5] == contenido):
        return True
    # Tercera horizontal
    if(tablero[2] == contenido and tablero[1] == contenido and tablero[0] == contenido):
        return True
    if(tablero[2] == contenido and tablero[0] == contenido and tablero[1] == contenido):
        return True
    if(tablero[1] == contenido and tablero[0] == contenido and tablero[2] == contenido):
        return True
    # Diagonal
    if(tablero[8] == contenido and tablero[4] == contenido and tablero[0] == contenido):
        return True
    if(tablero[8] == contenido and tablero[0] == contenido and tablero[4] == contenido):
        return True
    if(tablero[4] == contenido and tablero[0] == contenido and tablero[8] == contenido):
        return True
    # Diagonal invertida
    if(tablero[6] == contenido and tablero[4] == contenido and tablero[2] == contenido):
        return True
    if(tablero[6] == contenido and tablero[2] == contenido and tablero[4] == contenido):
        return True
    if(tablero[4] == contenido and tablero[2] == contenido and tablero[6] == contenido):
        return True
    # Como 0 representa 1 en el tablero, 10 representa a que no va a ninguna
    # posicion el ganador
    return False

# Función para ingresar Enum:ContenidoCelda.VACIO en celdas
def inicioTablero(tablero):
    for x in range(NUMERO_CELDAS):
        tablero.append(ContenidoCelda.VACIO.value)

# Función para imprimir el tablero con formato
def imprimirTablero(tablero):
    # tablero.reverse()
    for x in range(NUMERO_CELDAS):
        if((x % 3) == 0):
            print("\n")
        print(" |" + tablero[x] + "| ", end = "")
    print("\n")
    # tablero.reverse()

# Asigna el contenido a la celda vacia con input
def go(tablero, contenido):
    jugada = int(input("\nCelda a jugar: "))
    if(tablero[jugada - 1] == ContenidoCelda.VACIO.value):
        tablero[jugada - 1] = contenido
        imprimirTablero(tablero)
    else:
        print("\nCelda ocupada por " + tablero[jugada - 1] + ", ingresa otra celda disponible.")
        go(tablero, contenido)
    
# return 10 si no puede ganar nadie, return n != 10 en la posicion donde tirar para bloquear
def posswin(tablero, contenido):
    VACIO = ContenidoCelda.VACIO.value
    # Primera vertical
    if(tablero[8] == contenido and tablero[5] == contenido and tablero[2] == VACIO):
        return 2
    if(tablero[8] == contenido and tablero[2] == contenido and tablero[5] == VACIO):
        return 5
    if(tablero[5] == contenido and tablero[2] == contenido and tablero[8] == VACIO):
        return 8
    # Segunda vertical
    if(tablero[7] == contenido and tablero[4] == contenido and tablero[1] == VACIO):
        return 1
    if(tablero[7] == contenido and tablero[1] == contenido and tablero[4] == VACIO):
        return 4
    if(tablero[4] == contenido and tablero[1] == contenido and tablero[7] == VACIO):
        return 7
    # Tercera vertical
    if(tablero[6] == contenido and tablero[3] == contenido and tablero[0] == VACIO):
        return 0
    if(tablero[6] == contenido and tablero[0] == contenido and tablero[3] == VACIO):
        return 3
    if(tablero[3] == contenido and tablero[0] == contenido and tablero[6] == VACIO):
        return 6
    # Primera horizontal
    if(tablero[8] == contenido and tablero[7] == contenido and tablero[6] == VACIO):
        return 6
    if(tablero[8] == contenido and tablero[6] == contenido and tablero[7] == VACIO):
        return 7
    if(tablero[7] == contenido and tablero[6] == contenido and tablero[8] == VACIO):
        return 8
    # Segunda horizontal
    if(tablero[5] == contenido and tablero[4] == contenido and tablero[3] == VACIO):
        return 3
    if(tablero[5] == contenido and tablero[3] == contenido and tablero[4] == VACIO):
        return 4
    if(tablero[4] == contenido and tablero[3] == contenido and tablero[5] == VACIO):
        return 5
    # Tercera horizontal
    if(tablero[2] == contenido and tablero[1] == contenido and tablero[0] == VACIO):
        return 0
    if(tablero[2] == contenido and tablero[0] == contenido and tablero[1] == VACIO):
        return 1
    if(tablero[1] == contenido and tablero[0] == contenido and tablero[2] == VACIO):
        return 2
    # Diagonal
    if(tablero[8] == contenido and tablero[4] == contenido and tablero[0] == VACIO):
        return 0
    if(tablero[8] == contenido and tablero[0] == contenido and tablero[4] == VACIO):
        return 4
    if(tablero[4] == contenido and tablero[0] == contenido and tablero[8] == VACIO):
        return 8
    # Diagonal invertida
    if(tablero[6] == contenido and tablero[4] == contenido and tablero[2] == VACIO):
        return 2
    if(tablero[6] == contenido and tablero[2] == contenido and tablero[4] == VACIO):
        return 4
    if(tablero[4] == contenido and tablero[2] == contenido and tablero[6] == VACIO):
        return 6
    # Como 0 representa 1 en el tablero, 10 representa a que no va a ninguna
    # posicion el ganador
    return 10

def make(tablero, contenido):
    VACIO = ContenidoCelda.VACIO.value
    jugadoMaquina = "\nJugada de maquina"

    if(tablero[7] == VACIO):
        tablero[7] = contenido
        print(jugadoMaquina)
        imprimirTablero(tablero)
    elif(tablero[1] == VACIO):
        tablero[1] = contenido
        print(jugadoMaquina)
        imprimirTablero(tablero)
    elif(tablero[5] == VACIO):
        tablero[5] = contenido
        print(jugadoMaquina)
        imprimirTablero(tablero)
    elif(tablero[3] == VACIO):
        tablero[3] = contenido
        print(jugadoMaquina)
        imprimirTablero(tablero)
    else:
        # si no esta disponible niguna no esquina, busco y pongo donde este vacio
        contador = 0
        for x in tablero:
            if(x == VACIO):
                if(contador < 1):    
                    index = tablero.index(VACIO)
                    tablero[index] = contenido
                    print(jugadoMaquina)
                    imprimirTablero(tablero)
                    contador = contador + 1

# Algoritmo de inicio al comienzo de la partida
def inicioJugador(tablero):
    EQUIS = ContenidoCelda.EQUIS.value
    CIRCULO = ContenidoCelda.CIRCULO.value
    VACIO = ContenidoCelda.VACIO.value
    jugadoMaquina = "\nJugada de maquina"
    print("\nJuegas con " + EQUIS)
    
    # Primer paso jugador X
    go(tablero, EQUIS)

    # Segundo paso maquina O
    if(tablero[4] == VACIO):
        tablero[4] = CIRCULO
        print(jugadoMaquina)
        imprimirTablero(tablero)
    else:
        tablero[8] = CIRCULO
        print(jugadoMaquina)
        imprimirTablero(tablero)
    
    # Tercer paso jugador X
    go(tablero, EQUIS)

    # Cuarto paso maquina O
    tapar = posswin(tablero, EQUIS)
    if(tapar == 10):
        make(tablero, CIRCULO)
    else:
        tablero[tapar] = CIRCULO
        print(jugadoMaquina)
        imprimirTablero(tablero)
    ganarCirculo = ganador(tablero, CIRCULO)
    if(ganarCirculo == True):
        return print("\n\nGanan circulos")

    # Quinto paso jugador X
    go(tablero, EQUIS)
    ganarCirculo = ganador(tablero, CIRCULO)
    if(ganarCirculo == True):
        return print("\n\nGanan circulos")

    # Sexto paso maquina O
    taparCirculo = posswin(tablero, CIRCULO)
    taparEquis = posswin(tablero, EQUIS)
    
    if(taparCirculo != 10):
        tablero[taparCirculo] = CIRCULO
        print(jugadoMaquina)
        imprimirTablero(tablero)
    elif(taparEquis != 10):
        tablero[taparEquis] = CIRCULO
        print(jugadoMaquina)
        imprimirTablero(tablero)
    else:
        make(tablero, CIRCULO)
    ganarCirculo = ganador(tablero, CIRCULO)
    if(ganarCirculo == True):
        return print("\n\nGanan circulos\n\n")
    
    # Septimo paso jugador X
    go(tablero, EQUIS)
    ganarCirculo = ganador(tablero, CIRCULO)
    if(ganarCirculo == True):
        return print("\n\nGanan circulos\n\n")

    # Octavo paso maquina O
    taparCirculo = posswin(tablero, CIRCULO)
    taparEquis = posswin(tablero, EQUIS)

    if(taparCirculo != 10):
        tablero[taparCirculo] = CIRCULO
        print(jugadoMaquina)
        imprimirTablero(tablero)
    elif(taparEquis != 10):
        tablero[taparEquis] = CIRCULO
        print(jugadoMaquina)
        imprimirTablero(tablero)
    else:
        make(tablero, CIRCULO)
    ganarCirculo = ganador(tablero, CIRCULO)
    if(ganarCirculo == True):
        return print("\n\nGanan circulos\n\n")

    # Noveno paso jugador X
    go(tablero, EQUIS)
    ganarCirculo = ganador(tablero, CIRCULO)
    if(ganarCirculo == True):
        return print("\n\nGanan circulos\n\n")
    else:
        return print("\n\nNadie gana, empate\n\n")
    
# Definimos una vector "tablero" que si lo vemos como una matriz será como
# un teclado numerico:
"""
1   2   3
4   5   6
7   8   9
"""
tablero = []
NUMERO_CELDAS = 9
inicioTablero(tablero)  
imprimirTablero(tablero)
inicioJugador(tablero)
