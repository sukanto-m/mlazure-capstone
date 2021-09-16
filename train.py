from sklearn.linear_model import LogisticRegression
import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.model_selection import train_test_split
import pandas as pd
from azureml.core.run import Run
from azureml.dataset_factory import TabularDatasetFactory as tdf

#loading the data

file = 'heart_failure_clinical_records_dataset.csv'

df = pd.read_csv(file)

#data preprocessing

def clean_data(data):
    x_df = drop.na()

    #separating the target variable

    y_df = x_df.pop('DEATH_EVENT')

    return x_df, y_df

#call the clean_data function on dataset
x, y = clean_data(df)

#split dataset into train and test sets

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

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
    joblib.dump(value=model, filename='outputs/model_hf01.pkl')

if __name__ == '__main__':
    main()    
