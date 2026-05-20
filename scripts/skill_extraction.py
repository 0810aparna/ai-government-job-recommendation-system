import pandas as pd
import os

SKILLS = [
    "python", "sql", "excel", "power bi", "tableau",
    "machine learning", "deep learning", "nlp",
    "statistics", "data analysis", "java", "tensorflow",
    "pandas", "numpy", "scikit-learn", "communication",
    "leadership", "cloud", "aws", "spark"
]


def extract_skills(text):
    text = str(text).lower()
    return [skill for skill in SKILLS if skill in text]


def process_job_skills(jobs_df):

    print("\nExtracting skills from job descriptions...\n")

    possible_columns = ["job description", "description", "skills"]

    desc_col = None

    for col in possible_columns:
        if col in jobs_df.columns:
            desc_col = col
            break

    if desc_col is None:
        print("No description column found.")
        return jobs_df

    jobs_df["extracted_skills"] = jobs_df[desc_col].apply(extract_skills)

    os.makedirs("data/processed", exist_ok=True)

    jobs_df.to_csv(
        "data/processed/jobs_with_skills.csv",
        index=False
    )

    print("Skill extraction completed successfully.\n")

    return jobs_df