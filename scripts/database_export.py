import sqlite3
import pandas as pd
import json
import numpy as np


def convert_value(val):

    # None / NaN safe check
    if val is None:
        return ""

    # numpy arrays
    if isinstance(val, np.ndarray):
        return json.dumps(val.tolist())

    # pandas NaN (safe scalar check)
    try:
        if pd.isna(val):
            return ""
    except:
        pass

    # list / tuple
    if isinstance(val, (list, tuple)):
        return json.dumps(list(val))

    # dict
    if isinstance(val, dict):
        return json.dumps(val)

    # everything else
    return str(val)


def make_sql_safe(df):

    df = df.copy()

    for col in df.columns:
        df[col] = df[col].apply(convert_value)

    return df


def export_to_sqlite(jobs_df, salaries_df, schemes_df):

    print("\nExporting to SQLite database...\n")

    conn = sqlite3.connect("data/processed/analytics.db")

    jobs_df = make_sql_safe(jobs_df)
    salaries_df = make_sql_safe(salaries_df)
    schemes_df = make_sql_safe(schemes_df)

    jobs_df.columns = jobs_df.columns.str.replace(" ", "_")
    salaries_df.columns = salaries_df.columns.str.replace(" ", "_")
    schemes_df.columns = schemes_df.columns.str.replace(" ", "_")

    jobs_df.to_sql("jobs", conn, if_exists="replace", index=False)
    salaries_df.to_sql("salaries", conn, if_exists="replace", index=False)
    schemes_df.to_sql("government_schemes", conn, if_exists="replace", index=False)

    conn.close()

    print("SQLite database created successfully!")