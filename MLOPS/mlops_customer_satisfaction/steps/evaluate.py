import logging 
import pandas as pd
from zenml import step

@step 
def evaluate_model(df: pd.DataFrame)  -> None:
    """
    Evaluate the model on ingested data
    Args: 
        df: evaluating data
    return:
        None
    """
    pass
