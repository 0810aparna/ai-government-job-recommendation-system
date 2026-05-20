import pandas as pd


def clean_datasets():

    print("\nLoading datasets...\n")

    # LOAD DATASETS
    jobs_df = pd.read_csv("data/raw/job_descriptions.csv")

    salaries_df = pd.read_csv("data/raw/ds_salaries.csv")

    schemes_df = pd.read_csv("data/raw/government_schemes.csv")

    print("Datasets loaded successfully.\n")

    # STANDARDIZE COLUMN NAMES
    jobs_df.columns = jobs_df.columns.str.lower().str.strip()

    salaries_df.columns = salaries_df.columns.str.lower().str.strip()

    schemes_df.columns = schemes_df.columns.str.lower().str.strip()

    print("Column names standardized.\n")

    # REMOVE DUPLICATES
    jobs_df.drop_duplicates(inplace=True)

    salaries_df.drop_duplicates(inplace=True)

    schemes_df.drop_duplicates(inplace=True)

    # HANDLE MISSING VALUES
    jobs_df.fillna("Not Specified", inplace=True)

    salaries_df.fillna(0, inplace=True)

    schemes_df.fillna("Not Available", inplace=True)

    print("Missing values handled.\n")

    # SAVE CLEANED DATASETS
    jobs_df.to_csv(
        "data/processed/cleaned_jobs.csv",
        index=False
    )

    salaries_df.to_csv(
        "data/processed/cleaned_salaries.csv",
        index=False
    )

    schemes_df.to_csv(
        "data/processed/cleaned_schemes.csv",
        index=False
    )

    print("Cleaned datasets saved successfully.\n")

    return jobs_df, salaries_df, schemes_df