from pipelines.training_pipeline import train_pipeline

from zenml.client import Client



if __name__ == "__main__":
    # run the pipeline
    print(Client().active_stack.experiment_tracker.get_tracking_uri())
    train_pipeline(data_path = "data/olist_customers_dataset.csv")

# mlflow ui --backend-store-uri "file:/Users/vivek/Library/Application Support/zenml/local_stores/576cb7f7-2c2a-4200-83ca-ea14fbff9a33/mlruns"

