### En este script tenemos las funciones que se utilizan para realizar varias tareas de MLFlow.

# Librerías
from sklearn.pipeline import Pipeline
from typing import List, Any
import mlflow

# Funciones propias
from src.metrics import get_train_metrics, get_test_metrics



def mlflow_run(pipeline_sampling: Pipeline, 
               technique_name: Any,
               y_train_resampled, 
               y_pred_train, 
               y_pred_proba_train, 
               y_test, 
               y_pred_test, 
               y_pred_proba_test, 
               experiment_id: int) -> None:
    """
    Ejecuta una run de MLflow para una técnica de balanceo específica.

    Args:
        pipeline_sampling (Pipeline): Pipeline completo que incluye preprocesamiento, balanceo y modelo.
        technique_name (Any): Nombre de la técnica de balanceo.
        X_train: Datos de entrenamiento.
        y_train: Etiquetas de entrenamiento.
        y_pred_train: Predicciones del modelo en los datos de entrenamiento.
        y_pred_proba_train: Probabilidades de predicción del modelo en los datos de entrenamiento.
        y_test: Datos de prueba.
        y_pred_test: Predicciones del modelo en los datos de prueba.
        y_pred_proba_test: Probabilidades de predicción del modelo en los datos de prueba.
        experiment_id (int): ID del experimento de MLflow.

    Returns:
        None

    La función ejecuta una corrida de MLflow para una técnica de balanceo específica, registrando los siguientes elementos:
    - Datos de entrenamiento.
    - Parámetros del modelo.
    - Métricas de desempeño en los datos de entrenamiento y prueba.
    - El modelo entrenado.
    """
    with mlflow.start_run(nested=True, 
                          experiment_id=experiment_id, 
                          run_name=f'{technique_name}_model'
                          ):
        
        # Obtención del nombre e id de la run
        run_name = mlflow.active_run().info.run_name
        run_id = mlflow.active_run().info.run_id

        # Log y_train
        mlflow.log_input(mlflow.data.from_pandas(y_train_resampled, name=f"y_training_{technique_name}_dataset"))

        # Guardar parámetros
        params = pipeline_sampling.get_params(deep=True)
        mlflow.log_params(params)

        # Métricas en train
        for key, value in get_train_metrics(y_train_resampled, y_pred_train, y_pred_proba_train[:, 1]).items():
            mlflow.log_metric(key, value)

        # Métricas en test
        for key, value in get_test_metrics(y_test, y_pred_test, y_pred_proba_test[:, 1]).items():
            mlflow.log_metric(key, value)

        # Guadado del modelo
        mlflow.sklearn.log_model(pipeline_sampling, f"{technique_name}_model")
        mlflow.sklearn.save_model(pipeline_sampling, f"models/{run_name}/{run_id}")

        mlflow.end_run()



def mlflow_finetuned_run(grid_searched_pipeline: Pipeline, 
               technique_name: Any,
               y_train_resampled, 
               y_pred_train, 
               y_pred_proba_train, 
               y_test, 
               y_pred_test, 
               y_pred_proba_test, 
               experiment_id: int) -> None:
    """
    Ejecuta una run de MLflow para una técnica de balanceo específica.

    Args:
        pipeline_sampling (Pipeline): Pipeline completo que incluye preprocesamiento, balanceo y modelo.
        technique_name (Any): Nombre de la técnica de balanceo.
        X_train: Datos de entrenamiento.
        y_train: Etiquetas de entrenamiento.
        y_pred_train: Predicciones del modelo en los datos de entrenamiento.
        y_pred_proba_train: Probabilidades de predicción del modelo en los datos de entrenamiento.
        y_test: Datos de prueba.
        y_pred_test: Predicciones del modelo en los datos de prueba.
        y_pred_proba_test: Probabilidades de predicción del modelo en los datos de prueba.
        experiment_id (int): ID del experimento de MLflow.

    Returns:
        None

    La función ejecuta una corrida de MLflow para una técnica de balanceo específica, registrando los siguientes elementos:
    - Datos de entrenamiento.
    - Parámetros del modelo.
    - Métricas de desempeño en los datos de entrenamiento y prueba.
    - El modelo entrenado.
    """
    with mlflow.start_run(nested=True, 
                          experiment_id=experiment_id, 
                          run_name=f'{technique_name}_model_FT'
                          ):
        
        # Obtención del nombre e id de la run
        run_name = mlflow.active_run().info.run_name
        run_id = mlflow.active_run().info.run_id

        # Log X_train e y_train
        mlflow.log_input(mlflow.data.from_pandas(y_train_resampled, name=f"y_training_{technique_name}_dataset"))

        # Guardar parámetros
        params = grid_searched_pipeline.get_params(deep=True)
        mlflow.log_params(params)

        # Métricas en train
        for key, value in get_train_metrics(y_train_resampled, y_pred_train, y_pred_proba_train[:, 1]).items():
            mlflow.log_metric(key, value)

        # Métricas en test
        for key, value in get_test_metrics(y_test, y_pred_test, y_pred_proba_test[:, 1]).items():
            mlflow.log_metric(key, value)

        # Guadado del modelo
        mlflow.sklearn.log_model(grid_searched_pipeline, f"{technique_name}_model_FT")
        mlflow.sklearn.save_model(grid_searched_pipeline, f"models/{run_name}/{run_id}")

        mlflow.end_run()