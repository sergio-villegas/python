import pandas as pd
import matplotlib.pyplot as plt
import numpy
from sklearn.metrics import r2_score

"""
Author: Villegas Ferruzca Sergio Alejandro
Using https://gist.github.com/ryanorsinger/cb1222e506c1266b9cc808143ddbab82 
Apply machine learning tools from scikit-learn to find patterns that can
classify and predict new elements that can fit to the data base. 
Using polynomial regresion.
"""

# Cargar el archivo CSV
data = pd.read_csv('mall_customers.csv')
x = data['age']
y = data['annual_income']

# Realizamos una regresión polinomial
mymodel = numpy.poly1d(numpy.polyfit(x, y, 20))
myline = numpy.linspace(20, 70, 100)

spending_score_predict = mymodel(80)
print(spending_score_predict)

# Crear el gráfico
plt.scatter(x, y)
plt.plot(myline, mymodel(myline))

# Agregar etiquetas y título
plt.xlabel('age')
plt.ylabel('annual_income')
plt.title('Gráfico')

# Mostrar el gráfico
plt.show()
