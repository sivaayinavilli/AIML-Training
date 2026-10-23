# Day 5 — Capstone and Reproducibility

## Project
Testable ML Training and Inference Pipeline

## Dataset and configuration
- Dataset: Breast Cancer Wisconsin (scikit-learn)
- Total records: 569
- Features: 30
- Model: Logistic Regression
- Training records: 455
- Test records: 114
- Test size: 0.2
- Random state: 42
- Stratified split: Yes

## Evaluation results
- Accuracy: 0.9825
- Weighted precision: 0.9825
- Weighted recall: 0.9825
- Weighted F1: 0.9825
- Incorrect predictions: 2

## Error analysis
- Incorrect predictions saved: 2
- Error analysis file: reports/capstone_error_analysis.csv

## Validation evidence
- Dataset validation: passed
- Valid inference input: passed
- Missing-feature negative test: passed

## Reproducibility
- Random state: 42
- Python version: 3.10.9
- pandas version: 2.3.3
- scikit-learn version: 1.7.2

## How to run
Run all cells in Day5_Capstone_Reproducibility.ipynb from top to bottom.

## Limitations
- The dataset is public demonstration data, not company data.
- Results may differ on new data.
- The model is not intended for medical diagnosis or treatment decisions.
