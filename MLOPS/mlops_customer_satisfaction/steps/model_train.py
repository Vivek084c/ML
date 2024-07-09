import logging
import pandas as pd
from zenml import step
from src.model_dev import LinearRegressionModel
from sklearn.base import RegressorMixin
from .config import ModelNameConfig

@step 
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
        if config.model_name == "lightgbm":
            model = LinearRegressionModel()
            Trained_model = model.train(X_train, y_train)
            return Trained_model
        else:
            raise ValueError("Model {} not supported".format(config.model_name))
    except Exception as e:
        logging.error("Error in training the model: {}".format(e))
        raise e

        
