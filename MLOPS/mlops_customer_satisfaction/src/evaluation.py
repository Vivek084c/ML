import logging]
from abc import ABC, abstractmethod
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score,

class Evaluation(ABC):
    """
    Abstract class defing statery for evaluation
    """

    @abstractmethod
    def calculate_score(self, y_true: np.ndarray, y_pred: np.ndarray):
        pass

class MSE(Evaluation):
    """
    Evaluation statergy that use Mean Square Error 
    """

    def calculate_score(self, y_true: np.ndarray, y_pred: np.ndarray):
        try:
            logging("Calculating MSE")
            mse = mean_squared_error(y_true, y_pred)
            logging("MSE: {}".format(mse))
            return mse
        except Exception as e:
            logging.error("Error in calculating mse: {}".format(e))
            raise e

class R2(Evaluation):
    """
    Evaluation statergy that uses R2 score
    """

    def calculate_score(self, y_true: np.ndarray, y_pred: np.ndarray):
        try:
            logging.info("Calcuating R2 Score")
            r2 = r2_score(y_true, y_pred)
            logging.info("R2 Score: {}".format(r2))
            return r2
        except Exception as e:
            logging.error("Error in calculating the R2 score: {}".format(e))
            raise e
        
class RMSE(Evaluation):
    """
    Evaluation statergy that uses root mean square
    """
    def calculate_score(self, y_true: np.ndarray, y_pred: np.ndarray):
        try:
            logging.info("Calcuating RMSE")
            rmse = mean_squared_error(y_true, y_pred)
            logging.info("RMSE: {}".format(rmse))
            return rmse
        except Exception as e:
            logging.error("Error in calculating RMSE: {}".format(e))
            raise e
        
