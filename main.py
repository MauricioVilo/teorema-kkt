import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
class OptimizadorKKT:
    def __init__(self, funcion_objetivo, restricciones):
        self.funcion_objetivo = funcion_objetivo
        self.restricciones = restricciones

    def optimizar(self, punto_inicio):
        resultado = minimize(self.funcion_objetivo, punto_inicio, constraints=self.restricciones)
        return resultado.x, resultado.fun

funcion_objetivo = lambda x: -(200*x[0] + 300*x[1])

restricciones = ({"type": "ineq", "fun": lambda x: 2400 - x[0] - x[1]},
                 {"type": "ineq", "fun": lambda x: 320 - 2*x[0] - 4*x[1]},
                 {"type": "ineq", "fun": lambda x: x[0]},
                 {"type": "ineq", "fun": lambda x: x[1]})

optimizador = OptimizadorKKT(funcion_objetivo, restricciones)

punto_inicio = np.array([0, 0])
x, valor_funcion = optimizador.optimizar(punto_inicio)

np.set_printoptions(precision=4, suppress=True)
print(f"La solución óptima es x = {x} con una ganancia de = {valor_funcion}")


# Definición de las restricciones
x = np.linspace(0, 100, 400)
y1 = 2400 - x  # x1 + x2 <= 2400
y2 = 80 - 0.5*x  # 2x1 + 4x2 <= 320
y3 = np.zeros_like(x)  # x1 >= 0
y4 = np.zeros_like(x)  # x2 >= 0

# Función objetivo
x_vals = np.array([0, 100])
y_vals = (-200*x_vals)/300  # -200x1 -300x2 = cte

# Visualización de las restricciones
plt.plot(x, y1, label=r'$x_1 + x_2 \leq 2400$')
plt.plot(x, y2, label=r'$2x_1 + 4x_2 \leq 320$')
plt.fill_between(x, np.maximum.reduce([y4, y3, y2]), y1, alpha=0.3)

# Función objetivo
plt.plot(x_vals, y_vals, label=r'$-200x_1 -300x_2 = cte$')

# Punto óptimo
plt.scatter(x[0], y1[0], color='red', label='Punto óptimo')

plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.xlim((0, 1000))
plt.ylim((0, 1000))
plt.legend()
plt.show()
