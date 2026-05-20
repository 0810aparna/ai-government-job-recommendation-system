import pandas as pd

import joblib

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestRegressor

from sklearn.preprocessing import LabelEncoder

from sklearn.metrics import (
    mean_absolute_error,
    r2_score
)

import matplotlib.pyplot as plt


def train_salary_model(salaries_df):

    print("\nStarting salary prediction model training...\n")

    # CREATE COPY
    df = salaries_df.copy()

    # STANDARDIZE COLUMN NAMES
    df.columns = df.columns.str.lower().str.strip()

    # REQUIRED COLUMNS
    required_columns = [
        "experience_level",
        "employment_type",
        "remote_ratio",
        "salary_in_usd"
    ]

    # CHECK COLUMNS
    for col in required_columns:

        if col not in df.columns:

            print(f"ERROR: Missing column -> {col}")

            return None

    # LABEL ENCODING
    encoder = LabelEncoder()

    df["experience_level"] = encoder.fit_transform(
        df["experience_level"]
    )

    df["employment_type"] = encoder.fit_transform(
        df["employment_type"]
    )

    # FEATURES
    X = df[
        [
            "experience_level",
            "employment_type",
            "remote_ratio"
        ]
    ]

    # TARGET
    y = df["salary_in_usd"]

    # TRAIN TEST SPLIT
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # MODEL
    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    # TRAIN MODEL
    model.fit(X_train, y_train)

    # PREDICTIONS
    predictions = model.predict(X_test)

    # EVALUATION
    mae = mean_absolute_error(
        y_test,
        predictions
    )

    r2 = r2_score(
        y_test,
        predictions
    )

    print(f"Mean Absolute Error: {round(mae, 2)}")

    print(f"R2 Score: {round(r2, 2)}")

    # SAVE MODEL
    joblib.dump(
        model,
        "models/salary_model.pkl"
    )

    print("\nModel saved successfully.")

    # VISUALIZATION
    plt.figure(figsize=(8, 6))

    plt.scatter(
        y_test,
        predictions
    )

    plt.xlabel("Actual Salary")

    plt.ylabel("Predicted Salary")

    plt.title("Actual vs Predicted Salary")

    plt.tight_layout()

    plt.savefig(
        "screenshots/salary_prediction_results.png"
    )

    print("Prediction visualization saved.")

    return model