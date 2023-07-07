import numpy as np

# Crear un arreglo de números del 0 al 9
arr = np.arange(10)
print("Arreglo original:", arr)

# Calcular el cuadrado de cada elemento del arreglo
arr_cuadrado = np.square(arr)
print("Cuadrado de cada elemento:", arr_cuadrado)

# Calcular la suma de todos los elementos del arreglo
suma = np.sum(arr)
print("Suma de todos los elementos:", suma)

# Redimensionar el arreglo a una matriz de 2 filas y 5 columnas
matriz = arr.reshape(2, 5)
print("Matriz resultante:\n", matriz)

# Calcular la media de cada columna de la matriz
media_columnas = np.mean(matriz, axis=0)
print("Media de cada columna:", media_columnas)

# Generar un arreglo de números aleatorios entre 0 y 1 de forma (2, 3)
aleatorios = np.random.random((2, 3))
print("Arreglo de números aleatorios:\n", aleatorios)
