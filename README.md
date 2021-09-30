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
The AutoML notebook uses the Python SDK to train a range of models and arrive at the best metric.
### Results
The AutoML run trained a number of models and gave a best accuracy of 88% by the Voting Ensemble classifier (the best model). The parameters are experiment timeout of 30 minutes with max concurrent iterations at 5. Since the dataset passes tests of bias and is balanced, there don't seem to be any needs for improvement as such.
![automl](https://github.com/sukanto-m/mlazure-capstone/blob/main/Capstone_Screenshots/Screenshot%202021-09-30%20at%208.18.25%20AM.png)
![automl](https://github.com/sukanto-m/mlazure-capstone/blob/main/Capstone_Screenshots/Screenshot%202021-09-30%20at%208.33.06%20AM.png)
![automl](https://github.com/sukanto-m/mlazure-capstone/blob/main/Capstone_Screenshots/Screenshot%202021-09-30%20at%209.57.54%20AM.png)
![automl](https://github.com/sukanto-m/mlazure-capstone/blob/main/Capstone_Screenshots/Screenshot%202021-09-30%20at%2010.38.38%20AM.png)

## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
