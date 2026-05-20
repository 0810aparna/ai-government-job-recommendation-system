import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="AI Government Job Recommendation System",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Government Job Recommendation System")

st.markdown(
    "Analyze jobs, salaries, skills, and government schemes using AI analytics."
)

# DATABASE CONNECTION
conn = sqlite3.connect("data/processed/analytics.db")

jobs_df = pd.read_sql("SELECT * FROM jobs", conn)
salaries_df = pd.read_sql("SELECT * FROM salaries", conn)
schemes_df = pd.read_sql("SELECT * FROM government_schemes", conn)

# SIDEBAR
st.sidebar.header("Navigation")

show_jobs = st.sidebar.checkbox("Show Jobs Dataset")
show_salary = st.sidebar.checkbox("Show Salary Dataset")
show_schemes = st.sidebar.checkbox("Show Government Schemes")

# METRICS
st.subheader("Project Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Jobs", len(jobs_df))
col2.metric("Salary Records", len(salaries_df))
col3.metric("Schemes", len(schemes_df))

# DATASETS
if show_jobs:
    st.subheader("Jobs Dataset")
    st.dataframe(jobs_df.head(20))

if show_salary:
    st.subheader("Salary Dataset")
    st.dataframe(salaries_df.head(20))

if show_schemes:
    st.subheader("Government Schemes")
    st.dataframe(schemes_df.head(20))

# SALARY DISTRIBUTION
st.subheader("Salary Distribution")

fig, ax = plt.subplots(figsize=(10, 5))

salaries_df["salary_in_usd"].hist(
    bins=30,
    ax=ax
)

ax.set_title("Salary Distribution")
ax.set_xlabel("Salary")
ax.set_ylabel("Frequency")

st.pyplot(fig)

# TOP JOB TITLES
st.subheader("Top Job Roles")

if "job_title" in salaries_df.columns:

    top_roles = salaries_df["job_title"].value_counts().head(10)

    fig2, ax2 = plt.subplots(figsize=(10, 5))

    top_roles.plot(kind="bar", ax=ax2)

    ax2.set_title("Top Roles")

    st.pyplot(fig2)

# SKILL SEARCH
st.subheader("AI Skill Search")

user_skill = st.text_input(
    "Enter Skill",
    placeholder="python"
)

if user_skill:

    filtered_jobs = jobs_df[
        jobs_df["extracted_skills"].str.contains(
            user_skill,
            case=False,
            na=False
        )
    ]

    st.write(f"Found {len(filtered_jobs)} matching jobs.")

    st.dataframe(filtered_jobs.head(20))

conn.close()