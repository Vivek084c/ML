import logging
import pandas as pd
from zenml import step

from src.data_cleaning import DataClearning, DataDivideStratergy, DataPreProcessStatergy
from typing_extensions import Annotated
from typing import Tuple


@step
def clean_df(df: pd.DataFrame) -> Tuple[
    Annotated[pd.DataFrame, "X_train"],
    Annotated[pd.DataFrame, "X_test"],
    Annotated[pd.Series, "y_train"],
    Annotated[pd.Series, "y_test"]
]:
    """
    Cleans data and divides it into train and test
    Args:
        df: Raw data
    Returns:
        X_train: training data
        X_test: test data
        y_train: training data
        y_test: test data
    """
    try:
        process_statergy = DataPreProcessStatergy()
        data_cleaning = DataClearning(df, process_statergy)
        processed_data= data_cleaning.handle_data()

        divide_statergy = DataDivideStratergy()
        data_cleaning = DataClearning(processed_data, divide_statergy)
        X_train, X_test, y_train, y_test = data_cleaning.handle_data()
        logging.info("Data Cleaning Compleated")
        X_train, X_test, y_train, y_test
    except Exception as e:
        logging.error("Error in cleaning the data: {}".format(e))
        raise e