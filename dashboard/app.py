import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Government Job Recommendation System",
    page_icon="📊",
    layout="wide"
)

# ---------------- LOAD DATA ---------------- #

jobs_df = pd.read_csv("data/sample_jobs.csv")

# ---------------- TITLE ---------------- #

st.title("AI-Powered Government Job Recommendation System")

st.markdown(
    "Interactive NLP & ML-based dashboard for job recommendations and skill analytics."
)

# ---------------- SIDEBAR ---------------- #

st.sidebar.header("Filter Jobs")

selected_location = st.sidebar.selectbox(
    "Select Location",
    ["All"] + list(jobs_df["location"].unique())
)

# ---------------- FILTER DATA ---------------- #

filtered_df = jobs_df.copy()

if selected_location != "All":
    filtered_df = filtered_df[
        filtered_df["location"] == selected_location
    ]

# ---------------- DISPLAY DATA ---------------- #

st.subheader("Available Jobs")

st.dataframe(filtered_df)

# ---------------- SALARY ANALYSIS ---------------- #

st.subheader("Salary Distribution")

fig, ax = plt.subplots(figsize=(8, 4))

ax.bar(
    filtered_df["job_title"],
    filtered_df["salary"]
)

plt.xticks(rotation=45)

st.pyplot(fig)

# ---------------- SKILLS ---------------- #

st.subheader("Skills Overview")

all_skills = []

for skills in filtered_df["skills"]:
    skill_list = skills.split(",")
    all_skills.extend([s.strip() for s in skill_list])

skill_counts = pd.Series(all_skills).value_counts()

st.bar_chart(skill_counts)

# ---------------- FOOTER ---------------- #

st.markdown("---")

st.markdown(
    "Built using Python, Streamlit, NLP, and Machine Learning concepts."
)