from pipelines.deploynment_pipeline import deploynment_pipline, inference_pipeline
import click

DEOPLOY = "deploy"
PREDICT = "predict"
DEPLOY_AND_PREDICT = "deploy_and_predict" 

@click.command()
@click.option(
    "--config",
    "-c",
    type = click.Choice([DEOPLOY, PREDICT, DEPLOY_AND_PREDICT]),
    default = DEPLOY_AND_PREDICT,
    help = "Optionally you can chosse to run only deploynemnt  "
    "pipeline to train and deploy the model ('deploy'), or to "
    "only run a prediction against the deploynment model"
    "('predict'). By default both will be run "
    "('deploy_and_predict').",
)
@click.option(
    "--min-accuracy",
    default = 0.92,
    help = "Minimum accuracy required to deploy the model"
)

def run_deploynment(config: str, min_accuracy: float):
    if deploy:
        deploynment_pipline(min_accuracy)
    if predict:
        inference_pipeline(min_accuracy)
