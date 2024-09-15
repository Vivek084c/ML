import numpy as np
import pandas as pd
from materializer.custom_materializer import cs_materializer
from steps.clean_data import clean_data
from steps.evaluation import evaluation
from steps.ingest_data import ingest_data
from steps.model_train import train_model
from zenml import pipeline, step
from zenml.config import DockerSettings
from zenml.constants import DEFAULT_SERVICE_START_STOP_TIMEOUT
from zenml.integrations.constants import MLFLOW, TENSORFLOW
from zenml.integrations.mlflow.model_deployers.mlflow_model_deployer import (
    MLFlowModelDeployer,
)
from zenml.integrations.mlflow.services import MLFlowDeploymentService
from zenml.integrations.mlflow.steps import mlflow_model_deployer_step
from zenml.steps import BaseParameters, Output

from steps.clean_data import clean_df
from steps.evaluate import evaluate_model
from steps.ingest_data import ingest_df
from steps.model_train import train_model

docker_settings = DockerSettings(required_integrations= [MLFLOW])

class DeploynmentTreiggerConfig(BaseParameters):
    """Deplonemnt parameter congig"""
    min_accuracy = 0.92

@step
def deploynemnt_trigger(
    accuracy: float,
    config: DeploynmentTreiggerConfig,
):
    """implenments simple deploynment trigger taht looks at tha input model accuaray and looks if it is good to be deployed or not"""
    return accuracy>config.min_accuracy


@pipeline(enable_cache=True, settings={"docker_settings": docker_settings})
def continious_deploynment_pipeline(
    min_accuracy : float = 0.92,
    workers : int =1,
    timeout : int = DEFAULT_SERVICE_START_STOP_TIMEOUT,
):
    df =ingest_df()
    X_train, X_test, y_train, y_test = clean_df(df)
    model =train_model(X_train, X_test, y_train, y_test)
    r2_score, rmse = evaluate_model(model, X_test, y_test)
    deploynment_decision = deploynemnt_trigger(r2_score)
    mlflow_model_deployer_step(
        model = model,
        deploynment_decision = deploynment_decision,
        workers = workers,
        timeout  = timeout,
    )
    
