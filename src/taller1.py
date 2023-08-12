# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: title,-all
#     formats: py:percent,ipynb
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.0
# ---

# %% [markdown]
# # Métricas de Desempeño
# ---
#
# - **Taller 1**: machine learning.
# - **Fecha de entrega**: 5 de septiembre de 2023.
# - **Enlace de entrega**: https://forms.gle/F9ABUkVPyjgNdyEa9
#
# Importamos librerías:

# %% [code]
import numpy as np
import matplotlib.pyplot as plt
from numpy.typing import ArrayLike
from typing import Self
from sklearn.base import BaseEstimator

# %% [markdown]
# ## 1. Carga de Datos
# ---
#
# En este punto deberá crear un conjunto de datos con las siguientes especificaciones:
#
# - Debe utilizar la función `make_circles` de `sklearn`.
# - El conjunto de datos debe ser generado con 10.000 muestras.
# - Debe utilizar un factor de 0.3 entre el radio de los dos circulos.
# - Debe agregar un nivel de ruido de 0.2.
#
# Para esto, debe implementar la función `make_data`, la cual debe retornar la matriz de caracteristicas de los datos y sus etiquetas.

# %% [code]
def make_data() -> ArrayLike:
    # Agregue su código acá
    ...

# %% [code]
features = make_data()

# %% [markdown]
# ## 2. Modelo
# ---
#
# Revise el funcionamiento del algoritmo de [K-Nearest Neighbors (KNN)](https://www.ibm.com/topics/knn). Escriba un párrafo resumiendo el funcionamiento de este algoritmo de clasificación:

# %% [markdown]
# **Agregue texto acá**

# %% [markdown]
# ## 3. Implementación
# ---
#
# Implemente la clase `KNN` con el algoritmo de vecinos más cercanos, esta clase debe cumplir lo siguiente:
#
# - El método `fit` debe almacenar la matriz de características y las etiquetas.
# - El método `predict` debe generar una predicción para nuevas muestras siguiendo el algoritmo de KNN.

# %% [code]
class KNN(BaseEstimator):
    def __init__(self, k: int):
        self.k = k

    def fit(self, X: ArrayLike, y: ArrayLike) -> Self:
        # Agregue su código acá
        ...

    def predict(self, X: ArrayLike) -> ArrayLike:
        # Agregue su código acá
        ...

# %% [markdown]
# ## 4. Aplicación
# ---
#
# Entrene el modelo utilizando los datos y genere una gráfica mostrando las [regiones de decisión](https://scikit-learn.org/stable/auto_examples/ensemble/plot_voting_decision_regions.html) del modelo.
#
# Ajuste el valor del hiper-parámetro `k` y discuta los resultados.

# %% [code]
# Agregue su código acá
