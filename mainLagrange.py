#   Codigo que implementa la interpolacion de Lagrange 
#   para ajustar un conjunto de datos
#   
#
#           Autor:
#   
#   
#   Fecha: 
#   Version: 1.01


# Interpolación de Lagrange para estimar la temperatura en un motor
# Datos del ejercicio: Temperatura a distintas profundidades
# Autor: Adaptado por ChatGPT (basado en código de Gilbert Alexander Méndez Cervera)
# Fecha de adaptación: 2025-04-08
# Versión: 1.0

import numpy as np
import matplotlib.pyplot as plt

# Datos: Altitud (km) y Consumo (kg/h)
x_points = np.array([2.0, 4.0, 6.0, 8.0])  # Altitud
y_points = np.array([2500, 2300, 2150, 2050])  # Consumo

# Función para realizar interpolación de Lagrange
def lagrange_interpolation(x, x_points, y_points):
    """
    Calcula el valor interpolado en x utilizando el método de Lagrange.
    x: valor donde se desea interpolar
    x_points: puntos conocidos del eje x (altitud)
    y_points: puntos conocidos del eje y (consumo)
    """
    n = len(x_points)
    result = 0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

# a) Estimar el consumo a una altitud de 5 km
x_estimar = 5.0
y_estimada = lagrange_interpolation(x_estimar, x_points, y_points)
print(f"Consumo estimado a {x_estimar:.1f} km de altitud: {y_estimada:.2f} kg/h")

# b) Representar gráficamente los datos y la curva de interpolación
x_vals = np.linspace(min(x_points), max(x_points), 200)
y_vals = [lagrange_interpolation(x, x_points, y_points) for x in x_vals]

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label="Interpolación de Lagrange", color="blue")
plt.scatter(x_points, y_points, color="red", label="Datos originales")
plt.scatter(x_estimar, y_estimada, color="green", label=f"Estimación (5 km)\n{y_estimada:.2f} kg/h")
plt.xlabel("Altitud (km)")
plt.ylabel("Consumo de combustible (kg/h)")
plt.title("Interpolación de Lagrange - Consumo vs Altitud")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("consumo_avion_lagrange.png")
plt.show()



"""#EJERCICIO #1
# Definición de los puntos de interpolación
x_points = np.array([0.5, 1.0, 1.5, 2.0])
y_points = np.array([1.2,2.3,3.7,5.2])



# Función de interpolación de Lagrange
def lagrange_interpolation(x, x_points, y_points):
    n = len(x_points)
    result = 0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

# Puntos para graficar la interpolación
# Calcular el valor interpolado en x = 1.25
x_interpolado = 1.25
y_interpolado = lagrange_interpolation(x_interpolado, x_points, y_points)
print(f"La deformación esperada en x = {x_interpolado} m es aproximadamente {y_interpolado:.3f} mm")

# Puntos para graficar la interpolación
x_values = np.linspace(min(x_points), max(x_points), 100)
y_values = [lagrange_interpolation(x, x_points, y_points) for x in x_values]

# Graficar los puntos y la interpolación
plt.figure(figsize=(6, 4))
plt.plot(x_values, y_values, label="Interpolación de Lagrange", color="blue")
plt.scatter(x_points, y_points, color="red", label="Puntos dados")
plt.scatter(x_interpolado, y_interpolado, color="green", marker="o", label=f"Interpolado ({x_interpolado}, {y_interpolado:.2f})")
plt.xlabel("Posición (m)")
plt.ylabel("Deformación (mm)")
plt.title("Interpolación de Lagrange - Deformación en una viga")
plt.legend()
plt.grid(True)
plt.show()  """

"""EJERCICIO #2
# Datos: Profundidades (cm) y Temperaturas (°C)
x_points = np.array([1.0, 2.5, 4.0, 5.5])  # profundidades
y_points = np.array([85, 78, 69, 60])     # temperaturas

# Función para realizar interpolación de Lagrange
def lagrange_interpolation(x, x_points, y_points):
    
    Calcula el valor interpolado en x utilizando el método de Lagrange.
    x: valor donde se desea interpolar
    x_points: puntos conocidos del eje x (profundidad)
    y_points: puntos conocidos del eje y (temperatura)
    n = len(x_points)
    result = 0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

# a) Estimar la temperatura a una profundidad de 3.0 cm
x_estimar = 3.0
y_estimada = lagrange_interpolation(x_estimar, x_points, y_points)
print(f"Temperatura estimada a {x_estimar:.1f} cm de profundidad: {y_estimada:.2f} °C")
"""

"""
Ejercicio 3

"""