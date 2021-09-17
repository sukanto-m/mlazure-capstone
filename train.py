from sklearn.linear_model import LogisticRegression
import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.model_selection import train_test_split
import pandas as pd
from azureml.core.run import Run
from azureml.core import Workspace, Dataset, Datastore 
from azureml.data.dataset_factory import TabularDatasetFactory as tdf

#loading the data

path = 'https://raw.githubusercontent.com/sukanto-m/mlazure-capstone/main/heart_failure_clinical_records_dataset.csv'


#data preprocessing
def clean_data(df):
    y = df.pop('DEATH_EVENT')
    x = df
    return x,y




data = tdf.from_delimited_files(path=path)
data = data.to_pandas_dataframe()
x,y = clean_data(data)

#datastore_name = 'workspaceblobstore'
#datastore = Datastore.get(ws, datastore_name)
#datastore_path = [(datastore, 'UI/09-16-2021_114439_UTC/heart_failure_clinical_records_dataset.csv')]
#train = pd.concat([x_train, y_train], axis=1)

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3)
run = Run.get_context()

def main():
    #add arguments
    parser = argparse.ArgumentParser()

    parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge")

    args = parser.parse_args()

    run.log("Regularisation strength: ", np.float(args.C))
    run.log("Max iterations: ", np.int(args.max_iter))

    model = LogisticRegression(C=args.C, max_iter=args.max_iter).fit(x_train, y_train)

    accuracy = model.score(x_test, y_test)
    run.log("Accuracy", np.float(accuracy))

    os.makedirs('outputs', exist_ok=True)
    joblib.dump(value=model, filename='outputs/model.joblib')

if __name__ == '__main__':
    main()    
