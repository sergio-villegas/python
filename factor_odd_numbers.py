"""
Author: Sergio Alejandro Villegas Ferruzca
Program: Giving a number, the pattern is that this number can be represented
as a sum of each odd number in order using for 1 -> 1 number, for 5 -> the 5 next
odd numbers and finally giving the answer of each operation.
"""

# Determino mi N
n = int(input("Insert a number: "))
# Declaro una variable impar para subar 2 en 2 cuando haga una iteracion
impar = 1

print("N = " + str(n) + "\n")
# Recorro todos los numeros hasta mi N
for x in range(n):
    # Saco el resultado del numero al cubo
    resultado = pow((x + 1),3)
    print(str(x + 1) + "^3 = ", end="")
    # Recorro todos los numeros del numero analizado
    for y in range(x+1):
        # Imprimo mi numero impar
        print(str(impar), end="")
        # Si no es el ultimo elemento imprimir +
        if (y != x):
            print(" + ", end="")
        # Si ese es el ultimo elemento imprime =
        else:
            # Imprimo el resultado calculado
            print(" = " + str(resultado))
        # Cada que haga una iteracion sumo 2 a mi variable
        impar += 2
