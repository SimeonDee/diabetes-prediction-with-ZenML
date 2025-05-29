# diabetes-prediction-with-ZenML
End-to-end ML Workflow using ZenML, MLFlow and other integrations for Diabetes Prediction.

## Contacts
`Adedoyin Adeyemi` | [LinkedIn](https://www.linkedin.com/in/adedoyin-adeyemi-a7827b160/)

## Dataset Description
- **Data Source:** [Kaggle - Diabetes Prediction Dataset](https://www.kaggle.com/datasets/marshalpatel3558/diabetes-prediction-dataset-legit-dataset)
The provided dataset appears to be related to diabetes and contains various biomedical measurements and patient characteristics. Here's a detailed description of the dataset columns:

ID: A unique identifier for each record in the dataset.
No_Pation: Another identifier for the patient. It might be a patient number or record ID.
Gender: The gender of the patient (F for Female, M for Male).
AGE: The age of the patient in years.
Urea: Urea level in the blood (likely measured in mg/dL or mmol/L). Urea is a waste product of protein metabolism and can indicate kidney function.
Cr: Creatinine level in the blood (likely measured in mg/dL or µmol/L). Creatinine is another waste product that indicates kidney function.
HbA1c: Glycated hemoglobin, a measure of average blood sugar levels over the past 2-3 months (expressed as a percentage).
Chol: Cholesterol level in the blood (likely measured in mg/dL or mmol/L). This typically refers to total cholesterol.
TG: Triglycerides level in the blood (likely measured in mg/dL or mmol/L). Triglycerides are a type of fat in the blood.
HDL: High-density lipoprotein cholesterol level (often called "good" cholesterol, measured in mg/dL or mmol/L).
LDL: Low-density lipoprotein cholesterol level (often called "bad" cholesterol, measured in mg/dL or mmol/L).
VLDL: Very low-density lipoprotein cholesterol level (measured in mg/dL or mmol/L).
BMI: Body Mass Index, a measure of body fat based on height and weight (calculated as weight in kilograms divided by height in meters squared).
CLASS: The class label indicating the diabetes status of the patient. The possible values seem to be:
N: Non-diabetic
P: Prediabetic
Y: Diabetic

## Tools used
- Pandas and Numpy (Data ingestion, exploration and preprocessing)
- Scikit-learn (for data transformation (encoding, normalization), data segmentation, model training, and evaluation)
- ZenML (End-to-end ML workflow)
- MLFlow (for model experimentation, logging and monitoring)
- Python

## Setup
- Create and activate a virtual environment
- Install dependencies
```bash
(venv) ~$ pip install -r requirements.txt
```

- Run the ZenML Pipeline locally
```bash
(venv) ~$ zenml up --port 5382
```

- Visit the provided link to access the dashboard.
