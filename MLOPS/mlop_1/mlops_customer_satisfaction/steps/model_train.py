import logging
import pandas as pd
from zenml import step
from src.model_dev import LinearRegressionModel
from sklearn.base import RegressorMixin
from .config import ModelNameConfig



# Before uisng experinment tracker--------

# @step 
# def train_model(
#     X_train: pd.DataFrame,
#     X_test: pd.DataFrame,
#     y_train: pd.Series,
#     y_test: pd.Series,
#     config: ModelNameConfig
# ) -> RegressorMixin:
#     """
#     Traing the model on ingested data
#     Args:
#         X_train: pd.DataFrame,
#         X_test: pd.DataFrame,
#         y_train: pd.Series,
#         y_test: pd.Series,
#         config: ModelNameConfig
#     """ 
#     try:
#         model = None
#         if config.model_name == "LinearRegression":
#             model = LinearRegressionModel()
#             Trained_model = model.train(X_train, y_train)
#             return Trained_model
#         else:
#             raise ValueError("Model {} not supported".format(config.model_name))
#     except Exception as e:
#         logging.error("Error in training the model: {}".format(e))
#         raise e


# After using experinmet tracker

import mlflow
from zenml.client import Client

#defining an experiment tracker object
experinment_tracker = Client().active_stack.experiment_tracker

@step(experiment_tracker=experinment_tracker.name) 
def train_model(
    X_train: pd.DataFrame,
    X_test: pd.DataFrame,
    y_train: pd.Series,
    y_test: pd.Series,
    config: ModelNameConfig
) -> RegressorMixin:
    """
    Traing the model on ingested data
    Args:
        X_train: pd.DataFrame,
        X_test: pd.DataFrame,
        y_train: pd.Series,
        y_test: pd.Series,
        config: ModelNameConfig
    """ 
    try:
        model = None
        if config.model_name == "LinearRegression":
            # autologin model score and every other parameter using sklearn class
            mlflow.sklearn.autolog()
            model = LinearRegressionModel()
            Trained_model = model.train(X_train, y_train)
            return Trained_model
        else:
            raise ValueError("Model {} not supported".format(config.model_name))
    except Exception as e:
        logging.error("Error in training the model: {}".format(e))
        raise e
        
