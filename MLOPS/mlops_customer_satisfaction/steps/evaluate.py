import logging 
import pandas as pd
from zenml import step
from sklearn.base import RegressorMixin
from src.evaluation import MSE, RMSE,R2
from typing import Tuple
from typing_extensions import Annotated

# without tracker

# @step 
# def evaluate_model(
#     model: RegressorMixin, 
#     X_test: pd.DataFrame,
#     y_test: pd.DataFrame
#     )  -> Tuple[
#         Annotated[float, "r2_score"],
#         Annotated[float, "rmse"]
#     ]:
#     """
#     Evaluate the model on ingested data
#     Args: 
#         df: evaluating data
#     return:
#         None
#     """
#     prediction = model.predict(X_test)

#     # mse_class =MSE()
#     # mse = mse_class.calculate_score(y_test, prediction)

#     r2_class =R2()
#     r2 = r2_class.calculate_score(y_test, prediction)

#     rmse_class = RMSE()
#     rmse = rmse_class.calculate_score(y_test, prediction)

#     return r2, rmse


# with tracker

import mlflow
from zenml.client import Client

#defining an experiment tracker object
experinment_tracker = Client().active_stack.experiment_tracker

@step(experiment_tracker=experinment_tracker.name) 
def evaluate_model(
    model: RegressorMixin, 
    X_test: pd.DataFrame,
    y_test: pd.DataFrame
    )  -> Tuple[
        Annotated[float, "r2_score"],
        Annotated[float, "rmse"]
    ]:
    """
    Evaluate the model on ingested data
    Args: 
        df: evaluating data
    return:
        None
    """
    prediction = model.predict(X_test)

    # mse_class =MSE()
    # mse = mse_class.calculate_score(y_test, prediction)

    r2_class =R2()
    r2 = r2_class.calculate_score(y_test, prediction)
    #logging the metrices
    mlflow.log_metric("R2", r2)

    rmse_class = RMSE()
    rmse = rmse_class.calculate_score(y_test, prediction)
    #logging the metrices
    mlflow.log_metric("rmse", rmse)

    return r2, rmse