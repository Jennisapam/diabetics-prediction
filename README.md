# Diabetes Prediction System

An interactive machine-learning application built with Python and Streamlit that predicts a diabetes outcome label from eight user inputs.

I developed this undergraduate project to practise the complete machine-learning workflow: preparing data, training a classifier, evaluating predictions and building an interface.

Educational project only: This application is not clinically validated and should not be used to diagnose or rule out diabetes.

# What the application does

Users enter example health measurements through eight sidebar sliders. The application then:
1.Displays a prediction from a Random Forest classifier.
2.Shows the entered values and dataset summary statistics.
3.Visualises how the example inputs compare with the dataset.
4.Displays the model’s test accuracy.

# Technologies used
1.Python — application and model development
2.Streamlit — interactive interface
3.pandas — data loading and analysis
4.scikit-learn — model training and evaluation
5.Matplotlib and Seaborn — visualisations

# Dataset

The project uses the Pima Indians Diabetes dataset, stored in diabetes.csv.

-Dataset detail	Value
-Total records	768
-Input features	8

Target variable	Outcome:
-Non-diabetes records	500
-Diabetes records	268
-Training records	614
-Testing records	154

# The eight inputs are:
1.Number of pregnancies
2.Glucose
3.Blood pressure
4.Skin thickness
5.Insulin
6.Body mass index (BMI)
7.Diabetes pedigree function
8.Age

The target is encoded as 0 for non-diabetes and 1 for diabetes.

# Model and approach

The application uses a Random Forest classifier, which combines predictions from multiple decision trees.

The workflow is:

1.Load the dataset using pandas.
2.Separate the eight input features from the target.
3.Create an 80/20 train–test split, using random_state=0.
4.Train the Random Forest model.
5.Evaluate its accuracy on the test set.
6.Generate a prediction for the values entered in the interface.

Random Forest was the only classifier implemented in this version.

# Results

The project report recorded approximately 79.22% test accuracy.

The train–test split is fixed, but the Random Forest model does not have a fixed random seed. As a result, accuracy and predictions may vary when the application retrains.

This version evaluated accuracy only. Precision, recall, F1-score, specificity and ROC-AUC were not calculated, and cross-validation was not performed.

Project files
File or folder	Description
pr.py	Streamlit application and model code
diabetes.csv	Dataset
requirements.txt	Required Python packages
prediction output/	Application screenshots
README.md	Project overview and setup instructions

# How to run the application
1. Download the project

Download or clone the repository. Open a terminal in the folder containing pr.py, diabetes.csv and requirements.txt.

2. Create a virtual environment
python -m venv .venv

Activate it on macOS or Linux:

source .venv/bin/activate

Activate it on Windows PowerShell:

.venv\Scripts\Activate.ps1

3. Install the dependencies
python -m pip install -r requirements.txt

4. Start the application
python -m streamlit run pr.py

Open the local link displayed in the terminal. Use the sidebar sliders to enter fictional example values and explore the predictions.

If the dataset cannot be found: Check that diabetes.csv is in the current working folder when you start the application.

Screenshots and demo

Screenshots are available in the prediction output folder.

The application currently runs locally. A public live demo has not been deployed.

# Limitations and healthcare considerations

This project demonstrates a machine-learning application, but its results do not establish clinical reliability.

Limited validation: Evaluation used one train–test split. The model has not been tested in a clinical setting or validated on an independent dataset.

False negatives and false positives: Accuracy alone does not show how many diabetes cases were missed or how many non-diabetes cases were incorrectly flagged.

Data quality: The current code does not replace potentially invalid zero-valued measurements or perform missing-value imputation.

Class imbalance and bias: The dataset contains more non-diabetes records than diabetes records. No balancing method or subgroup fairness evaluation was implemented.

Explainability: The scatterplots describe the data but do not explain why the model made a particular prediction.

Reproducibility: The model retrains when the application reruns, and its random seed is not fixed.

Privacy: Use fictional inputs when demonstrating the application. The current script does not explicitly save entered values, but no formal 
privacy assessment has been completed.

Human oversight: The interface currently uses wording such as “You are diabetic.” This should be understood only as a model output, not a diagnosis.

# Future improvements
Compare Random Forest with other classifiers.
Add stratified cross-validation and more evaluation metrics.
Improve handling of missing and implausible measurements.
Fix the model seed and save the trained model.
Add explanations for individual predictions.
Evaluate performance across patient subgroups.
Replace diagnostic wording with clear educational messaging.
Prepare a public demonstration using fictional cases.

# Author

Jenifer Sapam
