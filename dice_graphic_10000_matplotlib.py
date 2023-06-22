"""
Author: Sergio Alejandro Villegas Ferruzca
Exercise: Roll a dice 10,000 times and calculate the average, standard deviation y and graph it up
as a graph bar.
"""

import random
import numpy as np
import matplotlib.pyplot as plt

NUM_TIRADAS = 10000
numeros = []
contador = [0, 0, 0, 0, 0, 0]

print("Rolling the dice 10,000 times.")
for x in range(NUM_TIRADAS):
    randNum = random.randint(1,6)
    numeros.append(randNum)

    if randNum == 1:
        contador[0] += 1
    elif randNum == 2:
        contador[1] += 1
    elif randNum == 3:
        contador[2] += 1
    elif randNum == 4:
        contador[3] += 1
    elif randNum == 5:
        contador[4] += 1
    elif randNum == 6:
        contador[5] += 1

print("\nAverage: " + str(np.mean(numeros)))
print("\nStandard deviation: " + str(np.std(numeros)))

enteros = np.array(["1", "2", "3", "4", "5", "6"])
valores = np.array([contador[0], contador[1], contador[2], contador[3], contador[4], contador[5]])

plt.bar(enteros, valores)
plt.show()
