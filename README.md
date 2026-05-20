# AI Government Job & Skill Recommendation System

An end-to-end Data Science project that analyzes job market trends, extracts skills using NLP, predicts salaries using Machine Learning, and recommends jobs based on user skill profiles.

---

## Project Overview

This system helps users:
- Understand in-demand skills in the job market
- Get personalized job recommendations
- Identify skill gaps
- Predict expected salary using ML models
- Explore government job schemes and employment insights

---

## Key Features

### Data Processing
- Cleaned and standardized real-world job + salary datasets
- Structured government scheme dataset integration

### NLP Skill Extraction
- Extracts skills from job descriptions using rule-based NLP
- Converts unstructured text into structured skill data

### Recommendation Engine
- TF-IDF + Cosine Similarity based job matching
- Personalized job recommendations
- Skill gap detection system

### Machine Learning Model
- Random Forest Regression for salary prediction
- Feature engineering on job attributes
- Model evaluation using MAE and R² Score

### Database Layer
- SQLite database integration
- SQL-ready structured tables for analytics

### Visualization
- Skill demand analysis
- Salary distribution graphs
- Model prediction visualization

---

## Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib
- NLP (TF-IDF)
- SQLite
- Jupyter Notebook

---

## ML Model Performance

- Model: Random Forest Regressor
- Evaluation: MAE + R² Score
- Output: Salary Prediction System

---

## How to Run

```bash
pip install -r requirements.txt
python main.py


