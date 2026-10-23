# Day 2 Report — Preprocessing and Leakage-Safe Pipeline

**Project:** Testable ML Training and Inference Pipeline  
**Story:** Preprocessing and Leakage-Safe Pipeline  
**Date:** Tuesday, 20 October 2026

## 1. Objective

Implement a machine learning pipeline using scikit-learn that applies consistent preprocessing during training and inference, prevents data leakage, and validates input schemas before generating predictions.

## 2. Work Completed

- Loaded the Breast Cancer Wisconsin Diagnostic dataset.
- Split the dataset into training and testing sets using stratified sampling.
- Implemented preprocessing using `Pipeline` and `ColumnTransformer`.
- Applied median imputation and standard scaling to numerical features.
- Integrated Logistic Regression as the classification model.
- Evaluated the model using accuracy, precision, recall, F1-score, and a confusion matrix.
- Implemented inference-time schema validation.
- Saved and reloaded the trained pipeline.
- Prepared inference test evidence and implementation documentation.

## 3. Dataset Details

| Item | Result |
|---|---|
| Total records | 569 |
| Input features | 30 |
| Target column | `target` |
| Training records | 455 |
| Testing records | 114 |
| Split strategy | Stratified train-test split |
| Random state | 42 |

## 4. Preprocessing Implementation

The preprocessing workflow includes:

1. **SimpleImputer:** Replaces missing numerical values using the median learned from the training data.
2. **StandardScaler:** Standardizes numerical features using statistics learned from the training data.
3. **Logistic Regression:** Performs binary classification using the preprocessed features.

All preprocessing steps are included in a single scikit-learn pipeline, ensuring that the same fitted transformations are used during training and inference.

## 5. Data Leakage Prevention

- Split the dataset before fitting preprocessing transformations.
- Fit preprocessing only through the training pipeline.
- Keep the target column separate from the input features.
- Apply the same fitted preprocessing steps during inference.
- Avoid fitting transformations independently on test data.

## 6. Inference Schema Validation

The schema validator checks the following conditions:

- All required feature columns are present.
- Unexpected extra columns are rejected.
- Duplicate column names are rejected.
- Non-numeric feature columns are rejected.
- Feature columns are reordered to match the training schema.
- Empty inputs and invalid data are rejected.

## 7. Testing and Validation

The following tests are included in the implementation:

| Test case | Expected behavior |
|---|---|
| Valid input | Prediction succeeds |
| Single-row input | One prediction is returned |
| Missing feature | Input is rejected |
| Extra feature | Input is rejected |
| Reordered columns | Correct feature order is restored |
| Model reload | Prediction matches the original pipeline |

**Note:** Mark these tests as passed in the final report only after the corresponding notebook cells execute successfully.

## 8. Model Evaluation

The model is evaluated on the held-out test set using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

The actual metric values are recorded in `reports/day2_model_metrics.csv`. They should be taken from the executed notebook rather than estimated or hardcoded.

## 9. Generated Artifacts

- `day2_preprocessing_pipeline.ipynb`
- `models/day2_ml_pipeline.joblib`
- `models/day2_schema.json`
- `reports/day2_model_metrics.csv`
- `reports/day2_inference_tests.csv`
- `DAY2_PIPELINE_NOTES.md`

## 10. Known Limitations

- The dataset is intended for machine-learning practice and is not a production clinical dataset.
- Schema validation checks column structure and numeric types but does not enforce domain-specific measurement ranges.
- Missing feature values are handled by the pipeline during transformation, while missing feature columns are rejected at inference.
- Model performance must be assessed using the actual test results.
- The test set should not be used repeatedly for model tuning.

## 11. Conclusion

The Day 2 implementation establishes a reusable machine learning pipeline with integrated preprocessing, leakage-aware training, inference-time schema validation, and model persistence. Successful execution of the notebook and verification of the saved artifacts provide evidence that the pipeline behaves consistently across training and inference.

## 12. Completion Criteria

- [ ] Pipeline implementation runs successfully.
- [ ] Model evaluation metrics are generated.
- [ ] Valid input and negative/boundary tests pass.
- [ ] Saved pipeline reloads successfully.
- [ ] Documentation and evidence files are saved.
- [ ] Changes are committed to Git.
