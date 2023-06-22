"""
Author: Sergio Alejandro Villegas Ferruzca 
Exercise: Roll two dices 10,000 times and calculate the average, standard deviation y and graph it up
as a graph bar.
"""

import random
import numpy as np
import matplotlib.pyplot as plt

NUM_TIRADAS = 10000
numeros = []
contador = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print("Rolling the dice 10,000 times.")
for x in range(NUM_TIRADAS):
    randNum1 = random.randint(1,6)
    randNum2 = random.randint(1,6)
    numeros.append(randNum1 + randNum2)

    if randNum1 + randNum2 == 2:
        contador[0] += 1
    elif randNum1 + randNum2 == 3:
        contador[1] += 1
    elif randNum1 + randNum2 == 4:
        contador[2] += 1
    elif randNum1 + randNum2 == 5:
        contador[3] += 1
    elif randNum1 + randNum2 == 6:
        contador[4] += 1
    elif randNum1 + randNum2 == 7:
        contador[5] += 1
    elif randNum1 + randNum2 == 8:
        contador[6] += 1
    elif randNum1 + randNum2 == 9:
        contador[7] += 1
    elif randNum1 + randNum2 == 10:
        contador[8] += 1
    elif randNum1+ randNum2 == 11:
        contador[9] += 1
    elif randNum1 + randNum2 == 12:
        contador[10] +=1


print("\nAverage: " + str(np.mean(numeros)))
print("\nStandard deviation: " + str(np.std(numeros)))

enteros = np.array(["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"])
valores = np.array([contador[0], contador[1], contador[2], contador[3], contador[4], contador[5],
                    contador[6], contador[7], contador[8], contador[9], contador[10]])

plt.bar(enteros, valores)
plt.show()
