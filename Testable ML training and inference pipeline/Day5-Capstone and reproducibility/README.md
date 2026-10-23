readme = """# Day 5 — ML Capstone and Reproducibility

## Project overview
This project demonstrates a reproducible machine-learning workflow using
the Breast Cancer Wisconsin dataset included with scikit-learn.

The workflow validates the data, creates a reproducible train/test split,
trains a Logistic Regression pipeline, evaluates predictions, and saves
the model, metadata, metrics, error analysis, and report.

## Technology
- Python
- pandas
- NumPy
- scikit-learn
- joblib
- Jupyter Notebook

## Dataset
- Source: scikit-learn Breast Cancer Wisconsin dataset
- Records: 569
- Features: 30 numeric features
- Target: `target`
- Class 0: malignant
- Class 1: benign

## Reproducibility
- Test size: 20%
- Random state: 42
- Stratified train/test split
- Preprocessing is fitted on training data through a scikit-learn Pipeline

## How to run
1. Open `Day5_Capstone_Reproducibility.ipynb` in VS Code.
2. Select the Python environment containing the required libraries.
3. Run all notebook cells from top to bottom.
4. Confirm that the validation and negative tests pass.
5. Review the generated files in the `models` and `reports` folders.

Install dependencies if required:

```bash
python -m pip install pandas numpy scikit-learn joblib jupyter