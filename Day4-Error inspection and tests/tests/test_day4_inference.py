
import pandas as pd
import pytest
from sklearn.datasets import load_breast_cancer

from day4_inference import validate_input


@pytest.fixture
def sample_data():
    dataset = load_breast_cancer(as_frame=True)
    return dataset.data.iloc[[0]].copy(), dataset.data.columns.tolist()


def test_valid_input(sample_data):
    row, features = sample_data
    result = validate_input(row, features)
    assert result.shape == (1, len(features))


def test_reordered_columns(sample_data):
    row, features = sample_data
    result = validate_input(row[features[::-1]], features)
    assert result.columns.tolist() == features


def test_missing_feature_rejected(sample_data):
    row, features = sample_data
    row = row.drop(columns=[features[0]])
    with pytest.raises(ValueError, match="Missing required features"):
        validate_input(row, features)


def test_extra_feature_rejected(sample_data):
    row, features = sample_data
    row["unexpected_feature"] = 1
    with pytest.raises(ValueError, match="Unexpected features"):
        validate_input(row, features)


def test_empty_input_rejected(sample_data):
    row, features = sample_data
    with pytest.raises(ValueError, match="at least one row"):
        validate_input(row.iloc[0:0], features)


def test_duplicate_columns_rejected(sample_data):
    row, features = sample_data
    row.columns = features[:-1] + [features[0]]
    with pytest.raises(ValueError, match="Duplicate feature columns"):
        validate_input(row, features)


def test_nonnumeric_feature_rejected(sample_data):
    row, features = sample_data
    row[features[0]] = "not-a-number"
    with pytest.raises(TypeError, match="must be numeric"):
        validate_input(row, features)


def test_non_dataframe_rejected(sample_data):
    _, features = sample_data
    with pytest.raises(TypeError, match="pandas DataFrame"):
        validate_input([[1, 2, 3]], features)
