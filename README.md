# Heart Failure Prediction

This is the capstone project for the Machine Learning Engineer with Microsoft Azure Nanodegree, for which I chose to use the [heart failure prediction dataset](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data) available from Kaggle. World Heart Day was observed recently, and cardiovascular diseases (CVDs) are a leading cause of death globally. The COVID-19 pandemic puts CVD patients at greater risk with co-morbidity. People with cardiovascular disease or who are at high cardiovascular risk (due to the presence of one or more risk factors such as hypertension, diabetes, hyperlipidaemia or already established disease) need early detection and management wherein a machine learning model can be of great help.

## Dataset

### Overview
The dataset, downloaded from Kaggle, contains medical data of patients of various ages and both sexes. There are 12 features, and the other predictor variables apart from age and sex include anaemia (categorical: 0 or 1), creatinine phosphate (numeric: Level of the CPK enzyme in the blood (mcg/L)) and ejection fraction (numeric: Percentage of blood leaving the heart at each contraction). These variables are used to predict whether the patient will survive the heart failure or not (Death Event: 0 (no) or 1(yes)).


### Task
This is a classification task to predict mortality by heart failure, expressed by the DEATH_EVENT variable with a binary (0 or 1) outcome

### Access
The dataset is uploaded and registered in tabular form on the ML Azure workspaceblobstore. The dataset URL or datastore path can be used to access the data in the Jupyter notebooks used for model training.


## Automated ML
The AutoML notebook uses the Python SDK to train a range of models and arrive at the best metric. A standard CPU-based compute cluster with 1+5 nodes is used.
### Results
The AutoML run trained a number of models and gave a best accuracy of 88% by the Voting Ensemble classifier (the best model). The parameters are experiment timeout of 30 minutes with max concurrent iterations at 5. Since the dataset passes tests of bias and AutoML uses various gradient boosting ensembles to arrive at the best metric, there don't seem to be any needs for improvement as such.
![automl](https://github.com/sukanto-m/mlazure-capstone/blob/main/Capstone_Screenshots/Screenshot%202021-09-30%20at%208.18.25%20AM.png)
![automl](https://github.com/sukanto-m/mlazure-capstone/blob/main/Capstone_Screenshots/Screenshot%202021-09-30%20at%208.33.06%20AM.png)
![automl](https://github.com/sukanto-m/mlazure-capstone/blob/main/Capstone_Screenshots/Screenshot%202021-09-30%20at%209.57.54%20AM.png)
![automl](https://github.com/sukanto-m/mlazure-capstone/blob/main/Capstone_Screenshots/Screenshot%202021-09-30%20at%2010.38.38%20AM.png)

## Hyperparameter Tuning
For the hyperparameter tuning using Hyperdrive, I used SKLearn's Logistic Regression since this is a classification task. I tuned the following 
two hyperparameters:

* C - inverse of regularisation strength, ie higher C indicates lower regularisation strength. I used C values in a uniform rangeof 0.1-1
* Max iterations - Maximum number of training iterations per child run. I used values in the 50,75,100 and 125 range to optimise run time.

The parameters were sampled using Random Sampling, with Bandit Policy for an early termination.

### Results
The best model outputs an accuracy of 87.8%, with a regularisation strength of 0.26. Since this accuracy is lower than that of the AutoMl model, training 
with decision trees/random forest with gradient boosting may be considered for improvement.

![hyper](https://github.com/sukanto-m/mlazure-capstone/blob/main/Capstone_Screenshots/Screenshot%202021-09-30%20at%204.04.29%20PM.png)
![hyper](https://github.com/sukanto-m/mlazure-capstone/blob/main/Capstone_Screenshots/Screenshot%202021-09-30%20at%204.04.40%20PM.png)
![hyper](https://github.com/sukanto-m/mlazure-capstone/blob/main/Capstone_Screenshots/Screenshot%202021-09-30%20at%204.14.04%20PM.png)
![hyper](https://github.com/sukanto-m/mlazure-capstone/blob/main/Capstone_Screenshots/Screenshot%202021-09-30%20at%204.21.16%20PM.png)


## Model Deployment
I deployed the best model from the AutoMl as it had a higher accuracy. The model was registered and deployed as an Azure Container Instance (ACI) webservice, with insights enabled. I used a Python endpoint.py script to send some sample data to the deployed webservice in JSON format and retrive the results.

![model](https://github.com/sukanto-m/mlazure-capstone/blob/main/Capstone_Screenshots/Screenshot%202021-09-30%20at%2010.29.10%20AM.png)
![model](https://github.com/sukanto-m/mlazure-capstone/blob/main/Capstone_Screenshots/Screenshot%202021-09-30%20at%2010.28.59%20AM.png)


## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
