# Day 4 — Experiment Tracking and Error Analysis

## Objective
Record model experiment settings and investigate prediction errors, threshold trade-offs, class imbalance and probability calibration.

## Experiment Configuration
- Dataset: Breast Cancer Wisconsin
- Train/test split: 80:20
- Random seed: 42
- Cross-validation from Day 3: 5-fold stratified cross-validation
- Models: Logistic Regression and Random Forest
- Preprocessing: median imputation, standard scaling and categorical encoding inside the model pipeline

## Experiment Tracking
The JSON experiment log records model parameters, Python and library versions, split sizes and test metrics.

## Error Analysis
The misclassified-cases CSV records each model's incorrect predictions and distinguishes missed malignant cases from benign cases incorrectly predicted malignant.

## Threshold Analysis
The threshold analysis CSV compares accuracy, malignant recall, malignant precision, malignant F1 and missed malignant cases at six malignant-probability thresholds.

Lower thresholds may increase malignant recall while also increasing false positives. Threshold selection requires considering both types of errors.

## Class Imbalance
The dataset contains 212 malignant and 357 benign records. Stratified splitting maintains approximate class proportions. Accuracy is therefore reported alongside balanced accuracy and malignant recall.

## Probability Calibration
The Brier score was calculated for Logistic Regression's malignant-class probabilities. It is a summary measure, not a complete calibration assessment. The small holdout set limits confidence in conclusions.

## Negative and Boundary Tests
The threshold helper accepted valid boundary values of 0 and 1 and rejected an invalid threshold of 1.5 with a ValueError.

## Limitations
- The dataset is public and used for practice, not company-provided data.
- The fixed test set contains only 114 records.
- Threshold results are exploratory and can vary with the dataset.
- No formal confidence intervals or detailed calibration curve analysis were performed.
- Results do not establish clinical suitability.

## Execution
Run `notebooks/day4_experiment_tracking.ipynb` from top to bottom. Verify the experiment log, misclassified cases, threshold analysis and this report before committing the changes.