"""
Autor: Villegas Ferruzca Sergio Alejandro
Programa: Craps game

Dice craps game:
- The game consists of roll a dice twice and the sum of the values will determine your game 
    - 7 or 11 = win
    - 2, 3 or 12 = lose
    - If it is not none of the above, the game will be determinated by the "point"
      that is the number that was gotten in the previous game.
        - The number in the previous game: win
        - 7: lose
"""

import random as rand

def jugada():
    tiro1 = tirarDado()
    tiro2 = tirarDado()
    resultado = sumar(tiro1, tiro2)
    print("\nSuma: " + str(resultado))
    return resultado

def tirarDado():
    input("\nRoll a dice (ENTER) ")
    dado = rand.randint(1,6)
    print("Throw: " + str(dado))
    return dado

def sumar(n1, n2):
    return n1 + n2

def ganar(resultado):
    if(resultado == 7 or resultado == 11):
        print("You have won")
    elif(resultado == 2 or resultado == 3 or resultado == 12):
        print("You have lost")
    else:
        tirada = 0
        intentos = 0
        while(resultado != tirada):
            intentos += 1
            tirada = jugada()
            if (resultado == tirada):
                print("You have won in " + str(intentos) + " tries")
            elif (tirada == 7):
                print("You have lost")

print("Dice craps game: \n- The game consists of roll a dice twice and the sum of the values will determine your game" 
      + "\t\n- 7 or 11 = win \t\n- 2, 3 or 12 = lose \t\n- If it is not none of the above, the game will be determinated by the \"point\""
      + "\t\n  that is the number that was gotten in the previous game.\t\n    - The number in the previous game: win \t\n    - 7: lose")

resultado = jugada()
ganar(resultado)
