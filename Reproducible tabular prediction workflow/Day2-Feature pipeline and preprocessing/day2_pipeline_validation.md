# Day 2 — Feature Pipeline and Preprocessing

## Objective
Build a reusable preprocessing pipeline that applies consistent transformations without data leakage.

## Implementation
- Used `ColumnTransformer` to combine numeric and categorical preprocessing.
- Numeric columns: median imputation and standard scaling.
- Categorical columns: most-frequent imputation and one-hot encoding.
- Used `OneHotEncoder(handle_unknown="ignore")` to handle unseen categories.
- Split data into 80% training and 20% testing using `random_state=42` and stratification.

## Leakage Prevention
The preprocessing pipeline was fitted only on training data. The same fitted transformations were applied to testing data using `transform()`.

## Validation Evidence
- Training rows: 455
- Testing rows: 114
- Numeric features: 30
- Categorical features in the actual dataset: 0
- No missing values in the processed train or test output.
- Verified that training and testing rows do not overlap.
- Tested an unseen categorical value using a separate sample dataset.

## Limitations
The current Breast Cancer Wisconsin dataset contains only numeric features. Categorical preprocessing was validated using a separate sample. No predictive model or final model-performance evaluation is included in this preprocessing task.