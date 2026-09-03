# diabetics-prediction
A Python and Streamlit undergraduate project that uses a Random Forest classifier to predict the diabetes outcome label from eight input measurements. The application combines model predictions, dataset summaries and visual comparisons in an interactive interface.

Educational prototype only. This project is not clinically validated and must not be used to diagnose, rule out or manage diabetes. The current interface uses diagnostic wording; treat its output only as a model classification.

Features

Eight sidebar sliders for entering example inputs.

Random Forest training and test-set accuracy displayed in the app.

A table showing the entered values and descriptive statistics for the dataset.

Seven scatterplots comparing the input values with the dataset, with the example highlighted in red.

Binary predictions: 0 for the non-diabetes label and 1 for the diabetes label.

Dataset

The project uses the Pima Indians Diabetes dataset, supplied as diabetes.csv. The accompanying project report identifies Kaggle as its source.

Item

Value

Records

768

Input features

8

Target column

Outcome

Non-diabetes labels (0)

500

Diabetes labels (1)

268

Training records

614

Test records

154

Inputs

CSV column

Interface input

Pregnancies

Number of pregnancies

Glucose

Glucose

BloodPressure

Blood pressure

SkinThickness

Skin thickness

Insulin

Insulin

BMI

Body mass index

DiabetesPedigreeFunction

Diabetes pedigree function

Age

Age

Method and results

Load the CSV using pandas.

Separate the eight predictors from Outcome.

Split the data into 80% training and 20% testing using random_state=0.

Fit scikit-learn's RandomForestClassifier() with default parameters.

Predict the outcome for the entered example and calculate test accuracy.

The project report records approximately 79.22% test accuracy. This is a previously reported result, not a newly reproduced benchmark. The Random Forest has no fixed random seed, so retraining can change both accuracy and individual predictions. The app retrains when the Streamlit script reruns, including after input changes.

Only Random Forest was trained. The implementation does not include cross-validation, stratification, hyperparameter tuning or comparisons with other classifiers. Precision, recall, F1, specificity and ROC-AUC were not calculated in this version. Summary statistics and scatterplots describe the data; they are not additional performance metrics or explanations of individual predictions.

Files

Place this README alongside pr.py inside the supplied prediction folder.

File or folder

Purpose

pr.py

Streamlit application, model training and evaluation

diabetes.csv

Dataset used by the application

requirements.txt

Python dependencies

prediction output/

Screenshots of the application

README.md

Project documentation

Run locally

Install Python 3, extract the project ZIP, and open a terminal in the prediction folder containing pr.py and diabetes.csv.

Create a virtual environment:

python -m venv .venv

Activate it on macOS or Linux:

source .venv/bin/activate

Or on Windows PowerShell:

.venv\Scripts\Activate.ps1

Install dependencies and start the app:

python -m pip install -r requirements.txt
python -m streamlit run pr.py

Open the local URL displayed in the terminal. Adjust the sidebar sliders to explore example predictions and plots. Use fictional example values.

Dataset not found? Run the command from the folder containing diabetes.csv; the code loads it using a relative path.

Dependencies include Streamlit, pandas, scikit-learn, matplotlib and seaborn. The requirements file also lists Plotly, although the current script does not use it. Package versions are not pinned, so an exact original software environment is not recorded.

Screenshots and demo status

The supplied prediction output folder contains nine application screenshots. These illustrate the interface and outputs. There is no public live demo currently. The application runs locally using the instructions above.

Healthcare considerations and limitations

Validation: The reported score comes from a single split of one dataset. There is no external, prospective or clinical validation, and no formal independent user study is documented.

Missed cases and false alarms: Accuracy alone does not quantify false negatives or false positives. A negative prediction cannot rule out diabetes, and a positive prediction does not establish a diagnosis.

Data quality: The supplied CSV has no blank values, but the code does not handle zero-valued clinical measurements as missing or perform imputation. Despite a preprocessing description in the project report, median replacement is not implemented in this script.

Bias and generalisability: The labels are imbalanced (500 versus 268), and the implementation uses no resampling or class weighting. Subgroup performance and fairness were not evaluated; results must not be assumed to generalise to other populations.

Explainability: Scatterplots provide descriptive comparisons. The app does not provide feature-attribution explanations such as SHAP values.

Privacy and governance: The script does not explicitly save entered values or send them to an external API. This is not a privacy audit or compliance guarantee. Use fictional inputs; any hosted version would need review of data permissions, hosting, access and logging.

Human oversight: The prototype is for demonstrating a machine-learning workflow. Clinical interpretation and decisions require qualified healthcare professionals.

Potential improvements

Handle implausible or missing measurements within a training pipeline.

Fix the model seed, pin dependency versions and avoid retraining on every interaction.

Compare baseline classifiers and use stratified cross-validation.

Report a confusion matrix, precision, recall, specificity, F1 and ROC-AUC.

Evaluate subgroup performance and validate on an independent dataset.

Add appropriate explanations and replace diagnostic wording before a public educational demo.

These are future improvements, not features already implemented.

Author

Jenifer Sapam — GitHub
