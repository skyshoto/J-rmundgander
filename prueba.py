import numpy as np
import matplotlib.pyplot as plt

# Función de la familia de curvas
def familia_curvas(x, y, k):
    return (x + 1) * (y**2 + x**2) - k + x**2

# Campo de direcciones (Ecuación diferencial)
def campo_direcciones(x, y):
    return (-(x + 1) * (2 * x) - (y**2 + x**2) - 2 * x) / (2 * (x + 1) * y)

# Rango de valores
x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x, y)

# Valores de la familia de curvas (k = 3, 6, 9)
k_values = [3, 6, 9]

# Gráfica de las curvas
plt.figure(figsize=(10, 6))
for k in k_values:
    plt.contour(X, Y, familia_curvas(X, Y, k), levels=[0], label=f'k={k}')
plt.title('Familia de Curvas')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid()
plt.legend(['k=3', 'k=6', 'k=9'])
plt.show()

# Campo de direcciones
U = 1  # Componente x constante (unidad)
V = campo_direcciones(X, Y)

# Normalizar el campo
magnitude = np.sqrt(U**2 + V**2)
U = U / magnitude
V = V / magnitude

plt.figure(figsize=(10, 6))
plt.quiver(X, Y, U, V, color='blue', alpha=0.6)
plt.title('Campo de Direcciones')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid()
plt.show()
