# Day 3 — Baseline Training and Evaluation

**Date:** Wednesday, 21 October 2026  
**Story:** Baseline training and evaluation  
**Project:** Testable ML Training and Inference Pipeline

## 1. Objective

Train at least two candidate models, compare their metrics against a Dummy Classifier, and justify a baseline selection.

## 2. Dataset and evaluation setup

- Dataset: Breast Cancer Wisconsin Diagnostic (scikit-learn)
- Records: 569
- Features: 30 numeric features
- Target: `target` (0 = malignant, 1 = benign)
- Training records: 455
- Testing records: 114
- Split: stratified 80/20
- Random state: 42

## 3. Candidate models

1. Dummy Classifier (`most_frequent`)
2. Logistic Regression
3. Random Forest (`n_estimators=200`, `random_state=42`,
   `class_weight=balanced`)

## 4. Preprocessing and leakage prevention

Median imputation and standard scaling are inside a scikit-learn
Pipeline and ColumnTransformer. The complete pipeline is fitted only
on the training data and then evaluated on the held-out test data.

## 5. Evaluation metrics

Metrics include accuracy, malignant precision, malignant recall,
malignant F1-score, and benign recall. Malignant recall receives
particular attention because class 0 represents malignant cases.

See `reports/day3_model_comparison.csv` and
`reports/day3_baseline_comparison.csv` for the measured results.

## 6. Selection rule and result

Selection rule: highest malignant recall, followed by malignant F1,
then accuracy.

Selected candidate: **Logistic Regression**

- Accuracy: 0.9825
- Malignant precision: 0.9762
- Malignant recall: 0.9762
- Malignant F1-score: 0.9762
- Benign recall: 0.9861

The selection must also be compared with the Dummy Classifier results.
This model is an educational baseline, not a clinically validated
diagnostic system.

## 7. Validation and evidence

- Valid input prediction tested.
- Single-row boundary case tested.
- Missing required feature rejected.
- Empty input rejected.
- Saved model reloaded and prediction consistency checked.

Detailed results are stored in `reports/day3_inference_tests.csv`.

## 8. Execution steps

1. Open `day3_baseline_evaluation.ipynb` in VS Code.
2. Run the notebook cells from top to bottom.
3. Review the metric table and confusion matrices.
4. Confirm the inference tests and model reload test pass.
5. Review the generated files and commit the changes to Git.

## 9. Known limitations

- Results depend on this dataset and the fixed train/test split.
- Only three candidate models were compared.
- No external validation dataset or clinical validation was used.
- The selection rule prioritizes malignant recall and may not reflect
  every real-world cost or deployment requirement.
- Results should not be interpreted as medical advice or a clinical tool.

## 10. Completion checklist

- [ ] Notebook runs successfully.
- [ ] Three candidate models compared with the Dummy Classifier.
- [ ] Metric comparison CSV generated.
- [ ] Negative/boundary tests passed.
- [ ] Selected model saved and reload verified.
- [ ] Documentation reviewed.
- [ ] Changes committed to Git.
