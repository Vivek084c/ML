import mlflow
import mlflow.sklearn
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

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
    rt = RandomForestClassifier(max_depth=max_depth, n_estimators=n_estimators, random_state=42)
    rt.fit(xtrain, ytrain)

    ypred = rt.predict(xtest)

    acc = accuracy_score(ytest, ypred)

    mlflow.log_metric('accuracy', acc)
    mlflow.log_param('max_depth', max_depth)
    mlflow.log_param('n_estimators', n_estimators)

    print(acc)