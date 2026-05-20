from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity

import pandas as pd


def prepare_skill_text(skill_column):

    return " ".join(skill_column)


def recommend_jobs(user_skills, jobs_df):

    print("\nGenerating AI job recommendations...\n")

    # CONVERT SKILLS LIST TO TEXT
    jobs_df["skills_text"] = jobs_df[
        "extracted_skills"
    ].apply(lambda x: " ".join(eval(str(x))))

    # CREATE CORPUS
    corpus = jobs_df["skills_text"].tolist()

    corpus.append(user_skills.lower())

    # TF-IDF VECTORIZATION
    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(corpus)

    # COSINE SIMILARITY
    similarity_scores = cosine_similarity(
        vectors[-1],
        vectors[:-1]
    )

    jobs_df["match_score"] = similarity_scores.flatten()

    # SORT RECOMMENDATIONS
    recommendations = jobs_df.sort_values(
        by="match_score",
        ascending=False
    )

    print("TOP JOB MATCHES:\n")

    # DETECT JOB TITLE COLUMN
    possible_title_columns = [
        "job title",
        "title",
        "job_title"
    ]

    title_column = None

    for col in possible_title_columns:

        if col in recommendations.columns:

            title_column = col

            break

    if title_column is None:

        title_column = recommendations.columns[0]

    # SHOW TOP RECOMMENDATIONS
    top_recommendations = recommendations[
        [title_column, "match_score"]
    ].head(5)

    print(top_recommendations)

    return recommendations

def detect_skill_gap(user_skills, jobs_df):

    print("\nPerforming skill gap analysis...\n")

    user_skill_set = set(user_skills.lower().split())

    market_skills = set()

    for row in jobs_df["extracted_skills"]:

        extracted = eval(str(row))

        for skill in extracted:

            market_skills.add(skill.lower())

    missing_skills = market_skills - user_skill_set

    top_missing = list(missing_skills)[:10]

    print("TOP MISSING SKILLS:\n")

    for skill in top_missing:

        print(f"- {skill}")

    return top_missing

def calculate_employability_score(user_skills, jobs_df):

    print("\nCalculating employability score...\n")

    user_skill_set = set(user_skills.lower().split())

    market_skills = set()

    for row in jobs_df["extracted_skills"]:

        extracted = eval(str(row))

        for skill in extracted:

            market_skills.add(skill.lower())

    matched_skills = user_skill_set.intersection(
        market_skills
    )

    score = (
        len(matched_skills)
        /
        len(market_skills)
    ) * 100

    score = round(score, 2)

    print(f"EMPLOYABILITY SCORE: {score}%")

    return score