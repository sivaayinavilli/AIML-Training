
import pandas as pd

def validate_input(data, feature_columns):
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    if data.empty:
        raise ValueError("Input must contain at least one row.")

    if data.columns.duplicated().any():
        raise ValueError("Duplicate feature columns are not allowed.")

    missing = set(feature_columns) - set(data.columns)
    extra = set(data.columns) - set(feature_columns)

    if missing:
        raise ValueError(f"Missing required features: {sorted(missing)}")

    if extra:
        raise ValueError(f"Unexpected features: {sorted(extra)}")

    if not all(
        pd.api.types.is_numeric_dtype(data[col])
        for col in feature_columns
    ):
        raise TypeError("All features must be numeric.")

    return data[feature_columns]
