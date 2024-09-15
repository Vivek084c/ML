from abc import ABC, abstractmethod
import logging
from sklearn.linear_model import LinearRegression


class Model(ABC):
    """
    abstract class for all models
    """
    @abstractmethod
    def train(self, X_train, y_train):
        """
        Train all the model
        Args: 
            X_train: Training data
            y_train: Training label
        Returns:
            None
        """
        pass

class LinearRegressionModel(Model):
    """"
    Linear Regression Model
    """
    def train(self, X_train, y_train, **kwargs):
        """
        Train the model
        Args:
            X_train: Training data
            y_train: Training labels
        Returns:
            None
        """
        try:
            reg = LinearRegression(**kwargs)
            reg.fit(X_train, y_train)
            logging.info("Model training compleate")
            return reg
        except Exception as e:
            logging.error("Error in Model training: {}".format(e))
            raise e
        




