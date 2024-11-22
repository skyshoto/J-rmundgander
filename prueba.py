import numpy as np
import matplotlib.pyplot as plt

# Ecuación del plano: -3x + 2y - 5z = 9
# Recta: P(-3, -1, 9) + t * (-3, 2, -5)

# Punto de la recta
punto_recta = np.array([-3, -1, 9])
direccion_recta = np.array([-3, 2, -5])

# Encontrar t usando la ecuación del plano
# Sustituimos x, y, z de la recta en el plano
# -3(x) + 2(y) - 5(z) = 9

t = 47 / 38  # Calculado previamente

# Coordenadas del punto de intersección
interseccion = punto_recta + t * direccion_recta

# Visualización en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar el plano
x = np.linspace(-10, 10, 10)
y = np.linspace(-10, 10, 10)
X, Y = np.meshgrid(x, y)
Z = (9 + 3*X - 2*Y) / 5

ax.plot_surface(X, Y, Z, alpha=0.5, color='blue', label="Plano")

# Graficar la recta
t_vals = np.linspace(-10, 10, 100)
recta_x = punto_recta[0] + direccion_recta[0] * t_vals
recta_y = punto_recta[1] + direccion_recta[1] * t_vals
recta_z = punto_recta[2] + direccion_recta[2] * t_vals
ax.plot(recta_x, recta_y, recta_z, color='red', label="Recta")

# Marcar el punto de intersección
ax.scatter(interseccion[0], interseccion[1], interseccion[2], color='green', label="Intersección", s=50)

# Configuración del gráfico
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()
