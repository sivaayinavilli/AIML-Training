# Day 3 — Model Comparison and Metrics

## Objective
Compare Logistic Regression and Random Forest using cross-validation and a fixed holdout test set.

## Dataset and Evaluation
- Dataset: Breast Cancer Wisconsin
- Total records: 569
- Training records: 455
- Test records: 114
- Split: 80:20 stratified split
- Random state: 42
- Cross-validation: 5-fold StratifiedKFold

## Models
1. Logistic Regression — a simple classification baseline.
2. Random Forest — a tree-based baseline capable of learning nonlinear patterns.

Both models use preprocessing inside a pipeline to prevent preprocessing leakage across cross-validation folds.

## Metric Rationale
- Accuracy: overall correctness.
- Balanced accuracy: accounts for performance across both classes.
- Malignant recall: measures detection of malignant cases.
- Cross-validation standard deviation: indicates variation across folds.

## Results
Insert the actual results from:
- `day3_cross_validation_results.csv`
- `day3_test_results.csv`

## Negative Test
A prediction request with a required feature removed was expected to fail. Record the actual output after running the test.

## Caveats and Limitations
- Results come from a public practice dataset, not company-provided data.
- The test set is relatively small, so individual predictions can affect the metrics.
- Cross-validation standard deviation describes fold-to-fold variation; it is not a formal confidence interval.
- The better baseline is not necessarily suitable for real clinical use.
- No hyperparameter tuning or external validation is included.

## Execution
Run `notebooks/day3_model_comparison.ipynb` from top to bottom. Confirm that both result CSV files are generated and review the notebook outputs before committing the changes.