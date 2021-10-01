# Heart Failure Prediction

This is the capstone project for the Machine Learning Engineer with Microsoft Azure Nanodegree, for which I chose to use the [heart failure prediction dataset](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data) available from Kaggle. World Heart Day was observed recently, and cardiovascular diseases (CVDs) are a leading cause of death globally. The COVID-19 pandemic puts CVD patients at greater risk with co-morbidity. People with cardiovascular disease or who are at high cardiovascular risk (due to the presence of one or more risk factors such as hypertension, diabetes, hyperlipidaemia or already established disease) need early detection and management wherein a machine learning model can be of great help.

I utilised this dataset to perform a classification task viz 'DEATH EVENT' occurs or not for the patients suffering from heart failure. I used two approaches for this - Automated ML and Hyperdrive runs in ML Azure Studio. The first approach uses the Python SDK in Azure and automatically featurises and trains the data on a number of classifier models to arrive at the best possible accuracy. In the second approach, a couple of hyperparameters (details below) are tuned and the model is trained via a training script using SKLearn's Losgistic Regression to arrive at the best accuracy rate. The best models from both runs are saved and registered. The best model from AutoML gave a slightly better accuracy so it was deployed as a webservice via the Azure Container Instance (ACI) and it can be consumed by sending input data as a JSON payload. The webservice sends binary variable (not fatal: 0 or fatal:1 responses) to predict mortality. A standard CPU compute cluster with maximum 6 nodes is used for both runs.

## Dataset

### Overview
The dataset, downloaded from Kaggle, contains medical data of patients of various ages and both sexes. There are 12 features, and the other predictor variables apart from age and sex include anaemia (categorical: 0 or 1), creatinine phosphate (numeric: Level of the CPK enzyme in the blood (mcg/L)) and ejection fraction (numeric: Percentage of blood leaving the heart at each contraction). These variables are used to predict whether the patient will survive the heart failure or not (Death Event: 0 (no) or 1(yes)).


### Task
This is a classification task to predict mortality by heart failure, expressed by the DEATH_EVENT variable with a binary (0 or 1) outcome

### Access
The dataset is uploaded and registered in tabular form on the ML Azure workspaceblobstore. The dataset URL or datastore path can be used to access the data in the Jupyter notebooks used for model training. The screenshots below show the data stored in the workspace and its URL/path.

![data](https://github.com/sukanto-m/mlazure-capstone/blob/main/Screenshots/Screenshot%202021-10-01%20at%208.16.49%20AM.png)
![data](https://github.com/sukanto-m/mlazure-capstone/blob/main/Screenshots/Screenshot%202021-10-01%20at%208.18.01%20AM.png)


## Automated ML
The AutoML notebook uses the Python SDK to train a range of models and arrive at the best metric. The AutoML mode runs by training the data on a number of classifier models like decision trees, ensemble learning etc. The experiment timeout is set at 30 minutes in order to optimise on costs while the maximum number of concurrent iterations is set at 5. The task is classification with the primary metric as accuracy. The compute cluster as described above is used. I've also enabled ONNX compatibility should deep learning
be used as an alternative.
### Results
The AutoML run trained a number of models and gave a best accuracy of nearly 88% by the Voting Ensemble classifier (the best model). This ensemble is a family of classifiers with weight intialisations at 0.1 for each sub-classifier. In terms of features this model ranks the 'time' variable of highest importance. The dataset as such passes the bias tests so data integrity is likely not a factor for improvement, but the experiment timeout can be increased and GPU-based high priority compute clusters can be instantiated if costs are not an issue. A GPU cluster would also enable deep learning tasks using frameworks like TensorFlow or Pytorch, though that does not gurantee significantly better results.

The following screenshots show the AutoML run through the RunDetails widget and on the Experiments page of ML Azure Studio. 
![automl](https://github.com/sukanto-m/mlazure-capstone/blob/main/Screenshots/Screenshot%202021-10-01%20at%208.23.05%20AM.png)
![automl](https://github.com/sukanto-m/mlazure-capstone/blob/main/Screenshots/Screenshot%202021-10-01%20at%209.22.31%20AM.png)
![automl](https://github.com/sukanto-m/mlazure-capstone/blob/main/Screenshots/Screenshot%202021-10-01%20at%209.22.51%20AM.png)
![automl](https://github.com/sukanto-m/mlazure-capstone/blob/main/Screenshots/Screenshot%202021-10-01%20at%208.23.35%20AM.png)

The screenshots below show the best AutoML model and its metrics
![bestauto](https://github.com/sukanto-m/mlazure-capstone/blob/main/Screenshots/Screenshot%202021-10-01%20at%209.23.07%20AM.png)
![bestauto](https://github.com/sukanto-m/mlazure-capstone/blob/main/Screenshots/Screenshot%202021-10-01%20at%208.44.55%20AM.png)
![bestauto](https://github.com/sukanto-m/mlazure-capstone/blob/main/Screenshots/Screenshot%202021-10-01%20at%208.45.23%20AM.png)
![bestauto](https://github.com/sukanto-m/mlazure-capstone/blob/main/Screenshots/Screenshot%202021-10-01%20at%209.55.39%20AM.png)


## Hyperparameter Tuning
For the hyperparameter tuning using Hyperdrive, I used SKLearn's Logistic Regression since this is a classification task. I tuned the following 
two hyperparameters:

* C - inverse of regularisation strength, ie higher C indicates lower regularisation strength. I used C values in a uniform rangeof 0.1-1
* Max iterations - Maximum number of training iterations per child run. I used values in the 50,75,100 and 125 range to optimise run time.

The parameters were sampled using Random Sampling, with Bandit Policy for an early termination.

### Results
The best model outputs an accuracy of 87.7%, with a regularisation strength of 0.7. Since this accuracy is lower than that of the AutoMl model, training 
with decision trees/random forest with gradient boosting may be considered for improvement.

The following screenshots show the progress of the Hyperdrive run via RunDetails and Experiments as well as the metrics of the best model and its registration.

![hyper](https://github.com/sukanto-m/mlazure-capstone/blob/main/Screenshots/Screenshot%202021-10-01%20at%208.54.17%20AM.png)
![hyper](https://github.com/sukanto-m/mlazure-capstone/blob/main/Screenshots/Screenshot%202021-10-01%20at%208.55.08%20AM.png)
![hyper](https://github.com/sukanto-m/mlazure-capstone/blob/main/Screenshots/Screenshot%202021-10-01%20at%209.11.45%20AM.png)
![hyper](https://github.com/sukanto-m/mlazure-capstone/blob/main/Screenshots/Screenshot%202021-10-01%20at%209.12.11%20AM.png)
![hyper](https://github.com/sukanto-m/mlazure-capstone/blob/main/Screenshots/Screenshot%202021-10-01%20at%209.12.30%20AM.png)
![hyper](https://github.com/sukanto-m/mlazure-capstone/blob/main/Screenshots/Screenshot%202021-10-01%20at%209.23.24%20AM.png)


## Model Deployment
I deployed the best model from the AutoMl as it had a higher accuracy, even if only marginal. The best model was registered and its scoring file was retrieved as a script file from its outputs folder. The ID of the best model was stored in an AutoMLRun object. These two in turn were used to instantiate an InferenceConfig object in the ACIWebService module. This configuration was deployed as an ACI webservice.
For consumption of the deployed model via the scoring_uri, I used the JSON and requests modules to construct sample input data payload and post HTTP requests to the webservice. The inference requests sent to the scoring_uri of the deokoyed model return 0 or 1 outputs based on the data input.

The following screenshots show the deployed model with 'Healthy' state and a demo of the model with HTTP requests sent to it and the responses

![model](https://github.com/sukanto-m/mlazure-capstone/blob/main/Screenshots/Screenshot%202021-10-01%20at%209.32.09%20AM.png)
![model](https://github.com/sukanto-m/mlazure-capstone/blob/main/Screenshots/Screenshot%202021-10-01%20at%209.32.23%20AM.png)
![model](https://github.com/sukanto-m/mlazure-capstone/blob/main/Screenshots/Screenshot%202021-10-01%20at%209.39.16%20AM.png)
![model](https://github.com/sukanto-m/mlazure-capstone/blob/main/Screenshots/Screenshot%202021-10-01%20at%209.39.27%20AM.png)


## Screen Recording
https://youtu.be/1iw5Y7tqEGM
