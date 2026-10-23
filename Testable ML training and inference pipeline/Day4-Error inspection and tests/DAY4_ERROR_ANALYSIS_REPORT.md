# Day 4 — Error Inspection and Tests

## 1. Project overview
- Dataset: Breast Cancer Wisconsin dataset
- Total records: 569
- Features: 30
- Model: Pipeline
- Training records: 455
- Test records: 114
- Split: 80% training / 20% testing
- Random state: 42
- Stratified split: Yes

## 2. Evaluation results
- Test accuracy: 0.9825 (98.25%)
- Incorrect predictions: 2
- False positives for malignant class: 1
- False negatives for malignant class: 1

A false positive means a benign case predicted as malignant.
A false negative means a malignant case predicted as benign.

### Confusion matrix
Rows are actual labels; columns are predicted labels.
Label order: 0 = malignant, 1 = benign.

    [[41  1]
     [ 1 71]]

### Classification report
```text
              precision    recall  f1-score   support

   malignant       0.98      0.98      0.98        42
      benign       0.99      0.99      0.99        72

    accuracy                           0.98       114
   macro avg       0.98      0.98      0.98       114
weighted avg       0.98      0.98      0.98       114
```

## 3. Input validation
All 8 automated tests passed:
- Valid input accepted
- Reordered columns handled
- Missing feature rejected
- Extra feature rejected
- Empty input rejected
- Duplicate columns rejected
- Non-numeric feature rejected
- Non-DataFrame input rejected

## 4. Reproducibility
- Dataset: scikit-learn Breast Cancer Wisconsin dataset
- Test size: 0.20
- Random state: 42
- Stratification: enabled
- Python version: 3.10.9

## 5. Limitations
- This is a public demonstration dataset, not company data.
- Test-set results alone do not establish real-world clinical performance.
- Numeric type validation does not ensure values are realistic.
- This model must not be used for medical decisions.

## 6. Output files
- models/day4_model_metadata.json
- models/day4_model_bundle.joblib
- reports/day4_error_analysis.csv
- reports/day4_error_summary.csv
- DAY4_ERROR_ANALYSIS_REPORT.md
