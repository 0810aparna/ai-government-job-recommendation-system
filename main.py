from scripts.data_cleaning import clean_datasets

from scripts.skill_extraction import process_job_skills

from scripts.visualization import (
    generate_skill_visualization,
    salary_distribution_visualization
)

from scripts.recommendation_engine import (
    recommend_jobs,
    detect_skill_gap,
    calculate_employability_score
)

from scripts.salary_prediction import train_salary_model

from scripts.database_export import export_to_sqlite


print("=" * 70)
print("AI GOVERNMENT JOB & SKILL RECOMMENDATION SYSTEM")
print("=" * 70)

# STEP 1 — CLEAN DATA
jobs_df, salaries_df, schemes_df = clean_datasets()

# STEP 2 — NLP PROCESSING
jobs_df = process_job_skills(jobs_df)

# STEP 3 — VISUALIZATIONS
generate_skill_visualization(jobs_df)

salary_distribution_visualization(
    salaries_df
)

# STEP 4 — USER SKILLS
user_skills = (
    "python sql power bi machine learning"
)

# STEP 5 — RECOMMEND JOBS
recommend_jobs(
    user_skills,
    jobs_df
)

# STEP 6 — SKILL GAP ANALYSIS
detect_skill_gap(
    user_skills,
    jobs_df
)

# STEP 7 — EMPLOYABILITY SCORE
calculate_employability_score(
    user_skills,
    jobs_df
)

# STEP 8 — MACHINE LEARNING MODEL
train_salary_model(
    salaries_df
)

print("\nPHASE 4 COMPLETED SUCCESSFULLY.")

export_to_sqlite(
    jobs_df,
    salaries_df,
    schemes_df
)