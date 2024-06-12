### En este archivo hay funciones que se utilizan para graficar y visualizar los datos.

# Librerías
from typing import List

import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd


def plot_churn(y_train: pd.Series, title: str, ax=None):
    """
    Función para crear un gráfico de barras de la variable 'Churn' en función de los datos de entrenamiento.

    Parameters:
    - y_train: pandas Series que contiene la variable objetivo de entrenamiento.

    Returns:
    - Gráfico de barras de la variable 'Churn'.
    """
    # Cálculo de los porcentajes de Churn Yes y No
    churn_counts = y_train.value_counts()
    churn_percentages = churn_counts / churn_counts.sum() * 100

    # Creación de los ejes si no se proporcionan
    if ax is None:
        fig, ax = plt.subplots()

    # Creación del gráfico de barras
    churn_counts.plot(kind='bar', color=['blue', 'green'], alpha=0.7, ax=ax)
    ax.set_title(title)
    ax.set_xlabel('Churn')
    ax.set_ylabel('Frecuencia')
    
    # Agregamos porcentajes en las barras
    for i, percentage in enumerate(churn_percentages):
        ax.text(i, churn_counts[i] + 0.5, f'{percentage:.2f}%', ha='center')

    # Cambio de la orientación de las etiquetas del eje X
    ax.set_xticklabels(['No', 'Yes'], rotation=0)



def plot_churn_distribution(y_train: pd.Series, title: str, ax: plt.Axes) -> None:
    """
    Función para crear un gráfico de barras que muestre la distribución de 'Churn' con anotaciones de porcentaje y conteo.
    
    Parámetros:
    y_train (pd.Series): Serie de pandas que contiene los valores de 'Churn'.
    title (str): Título del gráfico.
    ax (plt.Axes): Ejes del gráfico donde se trazará el gráfico.
    """
    # Creación del gráfico de barras
    y_train.value_counts(normalize=True).plot(kind='bar', ax=ax, color=['#1f77b4', '#ff7f0e'])

    # Obtención de los conteos y etiquetas de 'Yes' y 'No'
    conteos = y_train.value_counts().values

    # Para cada barra en el gráfico
    for i, p in enumerate(ax.patches):
        width = p.get_width()
        height = p.get_height()

        # Cálculo de porcentaje
        porcentaje = height * 100

        # Anotación de porcentaje y conteo
        ax.annotate(f'{porcentaje:.2f}% ({conteos[i]})', (p.get_x() + width / 2., p.get_height()), ha='center', va='bottom')

    # Título, etiqueta del eje x, etiqueta del eje y
    ax.set_title(title)
    ax.set_xlabel('Churn')
    ax.set_ylabel('Porcentaje')
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['No', 'Yes'], rotation=0)



def plot_all_distributions(y_trains: List[pd.Series], titles: List[str]) -> None:
    """
    Función para graficar la distribución de la variable 'Churn' para varias técnicas de oversampling.
    
    Parámetros:
    y_trains (List[pd.Series]): Lista de series de pandas que contienen los valores de 'Churn' para cada técnica.
    titles (List[str]): Lista de títulos para los gráficos.

    Devoluciones:
    None
    """
    # Cuadrícula para gráficos
    num_plots = len(y_trains)
    num_cols = 2
    num_rows = (num_plots + 1) // 2 if (num_plots + 1) % 2 == 0 else (num_plots + 1) // 2 + 1

    fig, axes = plt.subplots(num_rows, num_cols, figsize=(12, 6*num_rows))
    axes = axes.flatten()

    # Para cada eje, y_train y título
    for ax, y_train, title in zip(axes, y_trains, titles):

        # Aplicamos la función plot_churn_distribution
        plot_churn_distribution(y_train, title, ax)

        # Ajustamos la escala del eje y para todos los gráficos
        ax.set_ylim([0.0, 1.0])

    # Ocultamos cualquier gráfico vacío restante
    for j in range(num_plots, len(axes)):
        axes[j].axis('off')

    plt.tight_layout()
    plt.show()