### En este archivo hay funciones que se utilizan para calcular las métricas de un modelo.

# Processing
import pandas as pd
import numpy as np
from typing import Union

# Metrics
from sklearn.metrics import (
    recall_score, 
    precision_score,  
    roc_auc_score, 
    f1_score,  
    accuracy_score, 
    roc_auc_score,
    fbeta_score,
    make_scorer
)



def calculate_time(start_time: float, end_time: float, total_techniques: int, idx: int) -> Union[float, int]:
    """
    Calcula el tiempo transcurrido y las técnicas restantes.

    Args:
        start_time (float): Tiempo de inicio.
        end_time (float): Tiempo de finalización.
        total_techniques (int): Total de técnicas.
        idx (int): Índice actual de la técnica.

    Returns:
        Union[float, int]: Tiempo transcurrido en minutos y técnicas restantes.
    """
    # Cálculo del tiempo transcurrido
    elapsed_time_seconds = end_time - start_time

    # Convertir el tiempo transcurrido a minutos
    elapsed_time_minutes = elapsed_time_seconds / 60

    # Calcular técnicas restantes
    remaining_techniques = total_techniques - idx

    return elapsed_time_minutes, remaining_techniques



def get_metrics(
        y_true: pd.DataFrame, 
        y_pred: pd.DataFrame, 
        y_prob: pd.DataFrame
) -> dict[str, float]:
    
    """Función para calcular las métricas de un modelo.

    Args:
        y_true (pd.DataFrame): conjunto de datos con los valores reales.
        y_pred (pd.DataFrame): conjunto de datos con los valores predichos.
        y_prob (pd.DataFrame): conjunto de datos con las probabilidades predichas.

    Returns:
        dict[str, float]: diccionario con las métricas calculadas.
    """    
    return {
        'accuracy': round(accuracy_score(y_true, y_pred), 4),
        'precision': round(precision_score(y_true, y_pred, pos_label='Yes'), 4),
        'recall': round(recall_score(y_true, y_pred, pos_label='Yes'), 4),
        'f1_score': round(f1_score(y_true, y_pred, pos_label='Yes'), 4),
        'f2_score': round(fbeta_score(y_true, y_pred, beta=2, pos_label='Yes'), 4),
        'ROC_0': round(roc_auc_score(y_true, y_prob[:,0]), 4),
        'ROC_1': round(roc_auc_score(y_true, y_prob[:,1]), 4)
    }



def get_train_metrics(
        y_train: pd.DataFrame, 
        y_pred_train: pd.DataFrame, 
        y_pred_proba_train: pd.DataFrame
) -> dict[str, float]:
    
    """Función para calcular las métricas de un modelo sobre el conjunto de entrenamiento.

    Args:
        y_train (pd.DataFrame): conjunto de datos con los valores de entrenmiento reales.
        y_pred_train (pd.DataFrame): conjunto de datos con los valores predichos sobre el train.
        y_pred_proba_train (pd.DataFrame): conjunto de datos con las probabilidades predichas sobre el train.

    Returns:
        dict[str, float]: diccionario con las métricas calculadas sobre el conjunto de entrenamiento.
    """    
    return {
        'train_accuracy': round(accuracy_score(y_train, y_pred_train), 4),
        'train_recall': round(recall_score(y_train, y_pred_train, pos_label='Yes'), 4),
        'train_precision': round(precision_score(y_train, y_pred_train, pos_label='Yes'), 4),
        'train_f1': round(f1_score(y_train, y_pred_train, pos_label='Yes'), 4),
        'train_roc_auc': round(roc_auc_score(y_train, y_pred_proba_train), 4),
        'train_f2': round(fbeta_score(y_train, y_pred_train, beta=2, pos_label='Yes'), 4)
    }



def get_test_metrics(
        y_test: pd.DataFrame, 
        y_pred_test: pd.DataFrame, 
        y_pred_proba_test: pd.DataFrame
) -> dict[str, float]:
    
    """Función para calcular las métricas de un modelo sobre el conjunto de test.

    Args:
        y_test (pd.DataFrame): conjunto de datos con los valores de test reales.
        y_pred_test (pd.DataFrame): conjunto de datos con los valores predichos sobre el test.
        y_pred_proba_train (pd.DataFrame): conjunto de datos con las probabilidades predichas sobre el test.

    Returns:
        dict[str, float]: diccionario con las métricas calculadas sobre el conjunto de test.
    """    
    return {
        'test_accuracy': round(accuracy_score(y_test, y_pred_test), 4),
        'test_recall': round(recall_score(y_test, y_pred_test, pos_label='Yes'), 4),
        'test_precision': round(precision_score(y_test, y_pred_test, pos_label='Yes'), 4),
        'test_f1': round(f1_score(y_test, y_pred_test, pos_label='Yes'), 4),
        'test_roc_auc': round(roc_auc_score(y_test, y_pred_proba_test), 4),
        'test_f2': round(fbeta_score(y_test, y_pred_test, beta=2, pos_label='Yes'), 4)
    }



def f2_func(y_true: np.array, y_pred: np.array) -> float: 
    """
    Calcula el puntaje F2 para un conjunto de etiquetas verdaderas y predichas.

    Parameters:
        y_true (array-like): Etiquetas verdaderas.
        y_pred (array-like): Etiquetas predichas.

    Returns:
        float: Puntaje F2.
    """

    f2_score = fbeta_score(y_true, y_pred, beta=2, pos_label='Yes')
    return f2_score



def my_f2_scorer() -> callable: 
    """
    Crea un objeto de función personalizado para utilizar el puntaje F2 como métrica de puntuación.

    Returns:
        callable: Objeto de función que calcula el puntaje F2.
    """
    return make_scorer(f2_func)
