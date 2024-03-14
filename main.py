import numpy as np
from scipy.optimize import minimize

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

punto_inicio = np.array([0, 0])  # Punto de inicio
x, valor_funcion = optimizador.optimizar(punto_inicio)



np.set_printoptions(precision=4, suppress=True)
print(f"La solución óptima es x = {x} con una ganancia de = {valor_funcion}")

