from sklearn.linear_model import LogisticRegression
import argparse
import os
import numpy as np
from sklearn.metrics import mean_swuared_error
import joblib
from sklearn.model_selection import train_test_split
import pandas as pd
from azureml.core.run import Run
from azureml.dataset_factory import TabularDatasetFactory as tdf

file = 'heart_failure_clinical_records_dataset.csv'

df = pd.read_csv(file)

def clean_data(data):
    x_df = drop.na()
   