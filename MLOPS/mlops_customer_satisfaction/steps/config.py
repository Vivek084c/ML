# from zenml.steps import BaseParameters


# class ModelNameConfig(BaseParameters):
#     """
#     Model Config
#     """
#     model_name : str = "Linear_Regression"
    

from zenml.steps import BaseParameters


class ModelNameConfig(BaseParameters):
    """Model Configurations"""

    model_name: str = "lightgbm"
    # fine_tuning: bool = False
