# Breast Cancer Prediction — End-to-End ML Capstone

## 1. Project Overview

This project implements a reproducible machine-learning workflow for binary classification using the Breast Cancer Wisconsin dataset.

It uses Logistic Regression with numerical preprocessing in a single scikit-learn pipeline.

**Purpose:** Educational and engineering demonstration only. This model is not intended for medical diagnosis or clinical decision-making.

## 2. Technology Stack

- Python
- pandas
- scikit-learn
- joblib
- Jupyter Notebook

## 3. Project Structure

```text
Day5-End to end ML capstone/
├── breast_cancer.csv
├── your_day5_notebook.ipynb
├── models/
│   └── breast_cancer_pipeline.joblib
├── reports/
│   ├── day5_metrics.json
│   └── day5_model_metadata.json
├── MODEL_CARD.md
└── README.md
```

Replace `your_day5_notebook.ipynb` with the actual notebook filename if it differs.

## 4. Installation

Open a terminal in this project folder and install the dependencies:

```bash
python -m pip install pandas scikit-learn joblib jupyter
```

## 5. Model Details

- Algorithm: Logistic Regression
- Preprocessing: Median imputation and StandardScaler
- Train/test split: 80% / 20%
- Random seed: 42
- Input features: 30 numerical features
- Target: `target`
- Class mapping: `0` = malignant, `1` = benign

## 6. Evaluation Results

| Metric | Score |
|---|---:|
| Accuracy | 98.25% |
| Precision | 98.61% |
| Recall | 98.61% |
| F1-score | 98.61% |

These scores are from the held-out test set and are not a guarantee of future performance.

## 7. Running Predictions

Load the saved pipeline and use a row containing all required input features:

```python
import joblib
import pandas as pd

model = joblib.load("models/breast_cancer_pipeline.joblib")
sample = pd.read_csv("breast_cancer.csv").drop(columns=["target"]).iloc[[0]]

prediction = model.predict(sample)
print("Predicted class:", prediction[0])
```

The paths above assume the code runs from the project folder.

## 8. Testing

The notebook includes checks for:

- Valid input
- Single-row prediction
- Missing required feature
- Unexpected extra feature

Run the relevant test cells in the notebook and verify that the tests pass.

## 9. Artifacts

- `models/breast_cancer_pipeline.joblib`: Trained preprocessing and prediction pipeline.
- `reports/day5_metrics.json`: Evaluation metrics.
- `reports/day5_model_metadata.json`: Model configuration and environment metadata.
- `MODEL_CARD.md`: Intended use, performance, and limitations.

## 10. Known Limitations

- The model may produce false-positive or false-negative predictions.
- Performance on new data may differ from the reported test results.
- The model has not been validated for clinical use.
- The project does not establish medical safety or suitability for patient care.

## 11. Reproducibility

The train/test split uses `random_state=42` and stratification. The preprocessing operations are included in the saved pipeline so they can be applied consistently during inference.

For review, keep the notebook, model artifact, reports, documentation, and relevant source code together under version control.
