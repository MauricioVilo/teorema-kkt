# OptimizadorKKT

## Problema 
eres un agricultor y tienes 2400 metros cuadrados de tierra. Quieres plantar dos tipos de cultivos: maíz y frijoles. Cada hectárea de maíz requiere 2 horas de trabajo por día y cada hectárea de frijoles requiere 4 horas de trabajo por día. Tienes un total de 320 horas de trabajo disponibles. Si el beneficio por hectárea de maíz es de $200 y el beneficio por hectárea de frijoles es de $300, ¿cuántas hectáreas de cada cultivo deberías plantar para maximizar tus beneficios?

### Maximizar:
f(x,y)=200x+300y
### Sujeto a:
g1​(x,y)=x+y≤2400

Este proyecto implementa un optimizador basado en el método de Karush-Kuhn-Tucker (KKT) para resolver problemas de optimización con restricciones. Utiliza las bibliotecas numpy, scipy.optimize, y matplotlib.pyplot para la optimización numérica y la visualización de los resultados.

## Requisitos
Python 3.7 o superior
Numpy
Scipy
Matplotlib
## Instalación
Para instalar las dependencias necesarias, ejecute el siguiente comando:

pip install virtualenv
python -m venv venv
./venv/bin/activate
pip install numpy scipy matplotlib

## Uso
El script principal utiliza una función objetivo y un conjunto de restricciones para optimizar un problema de programación lineal. A continuación, se muestra un ejemplo de cómo utilizar el optimizador:
Este script define una función objetivo y un conjunto de restricciones, luego utiliza el optimizador para encontrar la solución óptima. Finalmente, visualiza la función objetivo y las restricciones junto con la solución óptima encontrada.
