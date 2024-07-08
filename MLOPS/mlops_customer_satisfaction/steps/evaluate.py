import logging 
import pandas as pd
from zenml import step
from sklearn.base import RegressorMixin
from src.evaluation import MSE, RMSE,R2
from typing import Tuple
from typing_extensions import Annotated
@step 
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

    mse_class =MSE()
    mse = mse_class.calculate_score(y_test, prediction)

    r2_class =R2()
    r2 = r2_class.calculate_score(y_test, prediction)

    rmse_class = RMSE()
    rmse = rmse_class.calculate_score(y_test, prediction)

    return r2, rmse
