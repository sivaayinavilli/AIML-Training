# Day 1 — Problem Definition and Data Quality

## 1. Project Overview
**Project:** Testable ML Training and Inference Pipeline

**Dataset:** Breast Cancer Wisconsin dataset

**Objective:** Build a reliable machine learning pipeline with data validation, leakage prevention, model evaluation, and prediction testing.

## 2. Problem Definition
- **Problem type:** Binary classification
- **Target column:** `target`
- **Input features:** 30 numerical features describing cell nuclei
- **Population:** Diagnostic samples represented in the dataset
- **Evaluation strategy:** Stratified train-test split

## 3. Data Quality Results
- Total records: 569
- Total columns: 31
- Missing values: 0
- Duplicate records: 0
- Missing target values: 0
- Class 0: 212 records
- Class 1: 357 records

## 4. Train-Test Split
- Training records: 455
- Testing records: 114
- Stratification: Enabled
- Feature-target overlap: None detected

## 5. Validation and Leakage Prevention
Verified that the training and testing datasets were created separately and that no feature column exactly matches the target column.

An exact-match check does not detect every possible form of data leakage. Further leakage prevention is required during preprocessing and model training.

## 6. Known Limitations
- The dataset is a benchmark dataset and may not represent every real-world population.
- Class distribution is imbalanced.
- Data-quality checks alone do not establish model performance or clinical usefulness.

## 7. Completion Evidence
Record the commands or notebook cells used for data-quality checks, split verification, and validation tests. Keep the relevant output and commit the project changes to Git.