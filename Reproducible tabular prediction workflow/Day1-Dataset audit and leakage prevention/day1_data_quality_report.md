# Day 1 — Dataset Audit and Leakage Prevention

## 1. Dataset Overview
- **Dataset:** Breast Cancer Wisconsin dataset from scikit-learn
- **Task:** Binary classification
- **Total records:** 569
- **Input features:** 30
- **Target column:** `target`
- **Target mapping:** 0 = Malignant, 1 = Benign

## 2. Data Quality Checks
| Check | Result |
|---|---:|
| Missing values | 0 |
| Exact duplicate rows | 0 |
| Missing target values | 0 |
| Features identical to target | 0 |

The initial data quality checks passed. Additional checks may be required to detect related records or other potential leakage.

## 3. Target Distribution
| Target | Class | Records | Percentage |
|---|---|---:|---:|
| 0 | Malignant | 212 | 37.26% |
| 1 | Benign | 357 | 62.74% |
| **Total** | | **569** | **100%** |

The target classes are imbalanced. Model evaluation should include precision, recall, F1-score, and a confusion matrix in addition to accuracy.

## 4. Train-Test Split
- **Training records:** 455 (approximately 80%)
- **Testing records:** 114 (approximately 20%)
- **Random state:** 42
- **Stratification:** Enabled

Stratification preserves approximately the same target-class proportions in both sets.

## 5. Reproducibility
The train-test split was repeated using the same settings. All four comparisons returned `True`:
- Training features
- Testing features
- Training labels
- Testing labels

This confirms that the split is reproducible with the current dataset and configuration.

## 6. Leakage Prevention
The target column was separated from the input features. An exact-copy check found no feature identical to the target.

This is only an initial leakage check. Feature meanings and data provenance must also be reviewed to identify suspicious or unavailable-at-prediction-time information.

The test set must remain separate from model training. Preprocessing steps that learn from data must be fitted on the training set only.

## 7. Output Artifacts
- `notebooks/day1_dataset_audit.ipynb`
- `reports/baseline_split_summary.csv`
- `reports/day1_data_quality_report.md`

## 8. Limitations and Next Steps
This is an initial audit using a public practice dataset. Confirm whether the official assignment requires a company-provided dataset. Next, review feature meanings, investigate potential leakage, and follow the agreed evaluation plan.