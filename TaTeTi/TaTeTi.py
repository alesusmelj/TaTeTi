tablero = [
    ["_", "_", "_"], 
    ["_", "_", "_"],
    ["_", "_", "_"]] 

#Para asignar valor a cada estado final del juego
valores = {
    "X": 1,
    "O": -1,
    "empate": 0
}

frases = {

    "X": "Perdiste :( !!",
    "O": "Ganaste !!!",
    "empate": "¡¡Empatamos!!"
}

def imprimirTablero(tablero):
    """"Imprime el estado actual del tablero"""

    print("\n------------------------------")

    for f in range (len(tablero)):
        for c in range (len(tablero)):
            print(tablero[f][c], end = " ")
        print()

    print("------------------------------\n")


def checker(tablero):
    """""Verifica si algun jugador gano, si aun se puede seguir jugando o si resulto en un empate"""

    #Vertical
    for i in range (len(tablero)):

        # Verifica los casilleros necesarios 
        if (tablero[0][i] == tablero[1][i]) and (tablero[1][i] == tablero[2][i]) and (tablero[0][i] != "_"): 

            # Checkea que jugador esta en la primer posicion de esos casilleros
            if (tablero[0][i]) == "X":
                return "X"
            elif (tablero[0][i]) == "O":
                return "O"

    #Horizontal
    for i in range(len(tablero)):

        if (tablero[i][0] == tablero[i][1]) and (tablero[i][1] == tablero[i][2]) and (tablero[i][0] != "_"):

            if (tablero[i][0]) == "X":
                return "X"
            elif (tablero[i][0]) == "O":
                return "O"

    #Diagonal arriba-abajo
    if (tablero[0][0] == tablero[1][1]) and (tablero[1][1] == tablero[2][2]) and (tablero[0][0] != "_"):

            if (tablero[0][0]) == "X":
                return "X"
            elif (tablero[0][0]) == "O":
                return "O"

    #Diagonal abajo-arriba
    if (tablero[2][0] == tablero[1][1] and tablero[1][1] == tablero[0][2]) and (tablero[2][0] != "_"):

            if (tablero[2][0]) == "X":
                return "X"
            elif (tablero[2][0]) == "O":
                return "O"

    #Si nadie gano y queda lugar en el tablero
    for fila in tablero:
        for casillero in fila:

            if (casillero == "_"):
                return "continua"

    #Si nada de lo anterior ocurrio, entonces nos encontramos frente a un empate
    return "empate"


def minimax(tablero, turnoPc):
    """"Algoritmo minimax utilizado para determinar el mejor movimiento de la computadora"""

    ganador = checker(tablero)

    if (ganador != "continua"):
        return valores[ganador]
    
    if (turnoPc): 
        score = -2               
        
        for i in range(len(tablero)):
            for j in range(len(tablero)):
                
                if (tablero[i][j]) == "_":
                    
                    tablero[i][j] = "X"
                    score_actual = minimax(tablero, False)
                    tablero[i][j] = "_"
                    score = max(score, score_actual)

        return score
        
    else:
        score =  2               

        for i in range(len(tablero)):
            for j in range(len(tablero)):
                
                if (tablero[i][j]) == "_":
                    tablero[i][j] = "O"
                    score_actual = minimax(tablero, True)
                    tablero[i][j] = "_"
                    score = min(score, score_actual)

        return score    

def movimientoPc(tablero):
    """"Envia las posiciones iniciales a minimax y compara los scores obtenidos hasta encontrar la mejor posicion"""

    score = -2               
    x = -1                    
    y = -1                    

    for i in range(len(tablero)):
        for j in range(len(tablero)):

            if (tablero[i][j]) == "_":

                tablero[i][j] = "X"
                score_actual = minimax(tablero, False)
                tablero[i][j] = "_"

                if (score_actual > score):
                    score = score_actual
                    x = i 
                    y = j

                #if (score_actual == -1):
                    #break
                
    tablero[x][y] = "X"

    return 

def movimientoHumano(tablero):
    """""Recibe el input para la posicion del jugador humano verificando si esta es valida"""

    while True:

        posicion = input("Ingrese la fila [0-2] separada por espacios y la columna [0-2] de la celda que desea elegir: ")
        posicion = posicion.strip()
        
        try:
            pos_espacio = posicion.find(" ")
            x = int(posicion[ : pos_espacio])
            y = int(posicion[pos_espacio + 1 : ])

            if (tablero[x][y] != "_") or (pos_espacio != 1):
                raise

            return x, y

        except:
            print("Error al seleccionar la posición, intente con otra.")
            print()
    
def main(tablero):

        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxx Bienvenido al TaTeTi xxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print()

        while True:

            try:
                primero = int(input("¿Quién va a jugar primero? 1: Humano - 2: Computadora  "))
                assert primero in (1,2)
                break

            except AssertionError:
                print()
                print("Opción inválida., elija entre 1 y 2.")
                print()
            except ValueError:
                print()
                print("Caracter inválido, ingrese un número.")
                print()
        print()

        if (primero == 1):

            print("Tablero inicial")
            imprimirTablero(tablero)
    
            while  (checker(tablero) == "continua"):

                x, y = movimientoHumano(tablero)
                tablero[x][y] = 'O'

                imprimirTablero(tablero)

                ganador = checker(tablero)
                if (ganador != "continua"):
                    print(frases.get(ganador))
                    break

                movimientoPc(tablero)
                imprimirTablero(tablero)

                ganador = checker(tablero)
                if (ganador != "continua"):
                    print(frases.get(ganador))
                    break

        else:

            while True:

                try:
                    elegir = int(input("¿Desea elegir en que posición iniciara la maquina? 1: No - 2: Si  "))
                    assert elegir in (1,2)
                    break

                except AssertionError:
                    print()
                    print("Opción inválida., elija entre 1 y 2.")
                    print()

                except ValueError:
                    print()
                    print("Caracter inválido, ingrese un número.")
                    print()

            print()

            if (elegir == 2):

                print("Tablero inicial")
                imprimirTablero(tablero)

                # Usamos la funcion movimientoHumano para pedirle la posicion de la computadora al usuario
                x, y = movimientoHumano(tablero)
                tablero[x][y] = 'X'
                imprimirTablero(tablero)

                while  (checker(tablero) == "continua"):
        
                    x, y = movimientoHumano(tablero)
                    tablero[x][y] = 'O'

                    imprimirTablero(tablero)

                    ganador = checker(tablero)
                    if (ganador != "continua"):
                        print(frases.get(ganador))
                        break

                    movimientoPc(tablero)
                    imprimirTablero(tablero)

                    ganador = checker(tablero)
                    if (ganador != "continua"):
                        print(frases.get(ganador))
                        break

            else:
                while  (checker(tablero) == "continua"):
                    
                    movimientoPc(tablero)
                    imprimirTablero(tablero)
                    
                    ganador = checker(tablero)
                    if (ganador != "continua"):
                        print(frases.get(ganador))
                        break
 
                    x, y = movimientoHumano(tablero)
                    tablero[x][y] = 'O'

                    imprimirTablero(tablero)

                    ganador = checker(tablero)
                    if (ganador != "continua"):
                        print(frases.get(ganador))
                        break

#Programa principal

main(tablero)