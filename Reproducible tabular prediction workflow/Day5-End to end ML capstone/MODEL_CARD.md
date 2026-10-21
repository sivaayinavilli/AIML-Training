# Model Card: Breast Cancer Prediction

## 1. Model Overview

- **Project:** Breast Cancer Prediction
- **Model:** Logistic Regression
- **Problem type:** Binary classification
- **Dataset:** Breast Cancer Wisconsin dataset
- **Target column:** `target`

## 2. Intended Use

This model is an educational machine-learning project for demonstrating a reproducible tabular prediction workflow.

It is not intended for clinical use, medical diagnosis, or treatment decisions.

## 3. Dataset and Preprocessing

- Input: 30 numerical features.
- Target: `0` = malignant, `1` = benign.
- Missing numerical values are imputed using the median.
- Features are standardized using `StandardScaler`.
- Train/test split: 80% training and 20% testing.
- Random seed: `42`.
- Stratified splitting preserves approximate class proportions.

## 4. Evaluation Results

| Metric | Result |
|---|---:|
| Accuracy | 98.25% |
| Precision | 98.61% |
| Recall | 98.61% |
| F1-score | 98.61% |

These results apply to the held-out test set from this project. They do not guarantee performance on new or real-world data.

## 5. Testing

The following tests passed:

- Valid input produces a prediction.
- Single-row input is supported.
- Missing required features are rejected.
- Unexpected extra features are rejected.

## 6. Limitations and Risks

- Performance may change on data from different populations or collection methods.
- The model may make false-positive and false-negative predictions.
- Test-set performance alone does not establish clinical safety.
- The model has not been validated for real-world medical use.

## 7. Reproducibility

- Random seed: `42`
- Model artifact: `models/breast_cancer_pipeline.joblib`
- Metrics: `reports/day5_metrics.json`
- Metadata: `reports/day5_model_metadata.json`

## 8. Conclusion

This project demonstrates a packaged classification pipeline with saved metrics, model metadata, and basic input-validation tests. It is intended for learning and engineering review only.