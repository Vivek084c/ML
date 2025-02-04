import mlflow
import mlflow.sklearn
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import os        

#setting the mlflow tracking uri
mlflow.set_tracking_uri("http://127.0.0.1:5000") 

#loading the dataset
wine = load_wine()
x = wine.data
y = wine.target

#train test split
xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.10, random_state=42)

#defining the parameteres fro the model
max_depth = 10
n_estimators = 10


#mlflow
with mlflow.start_run():
   # Training the model
    rf = RandomForestClassifier(max_depth=max_depth, n_estimators=n_estimators, random_state=42)
    rf.fit(xtrain, ytrain)

    # Making predictions
    ypred = rf.predict(xtest)

    # Calculating accuracy
    acc = accuracy_score(ytest, ypred)
    print(f"Model Accuracy: {acc}")

    # Logging metrics and parameters
    mlflow.log_metric("accuracy", acc)
    mlflow.log_param("max_depth", max_depth)
    mlflow.log_param("n_estimators", n_estimators)

    # Creating and saving the confusion matrix plot
    cm = confusion_matrix(ytest, ypred)
    plt.figure(figsize=(6, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=wine.target_names, yticklabels=wine.target_names)
    plt.ylabel("Actual")
    plt.xlabel("Predicted")
    
    # Save the confusion matrix plot
    cm_plot_path = "confusion_matrix.png"
    plt.savefig(cm_plot_path)
    plt.close()

    # Logging artifacts
    mlflow.log_artifact(cm_plot_path)  # Log the confusion matrix plot

    # Optional: Log the script (works if run as a script, not interactively)
    script_path = os.path.abspath(__file__) if "__file__" in globals() else None
    if script_path:
        mlflow.log_artifact(script_path)