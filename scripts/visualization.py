import matplotlib.pyplot as plt

import pandas as pd


def generate_skill_visualization(jobs_df):

    print("\nGenerating skill demand visualization...\n")

    skill_counts = {}

    for row in jobs_df["extracted_skills"]:

        skills = str(row).replace(
            "[",
            ""
        ).replace(
            "]",
            ""
        )

        skills = skills.split(",")

        for skill in skills:

            skill = skill.strip().replace(
                "'",
                ""
            )

            if skill != "":

                skill_counts[skill] = (
                    skill_counts.get(skill, 0) + 1
                )

    sorted_skills = sorted(
        skill_counts.items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]

    skills = [x[0] for x in sorted_skills]

    counts = [x[1] for x in sorted_skills]

    plt.figure(figsize=(12, 6))

    plt.bar(skills, counts)

    plt.xticks(rotation=45)

    plt.xlabel("Skills")

    plt.ylabel("Demand Count")

    plt.title("Top In-Demand Skills")

    plt.tight_layout()

    plt.savefig(
        "screenshots/top_skills.png"
    )

    print("Top skills visualization saved.")


def salary_distribution_visualization(
    salaries_df
):

    print("\nGenerating salary distribution...\n")

    plt.figure(figsize=(10, 6))

    salaries_df["salary_in_usd"].hist(
        bins=30
    )

    plt.xlabel("Salary in USD")

    plt.ylabel("Frequency")

    plt.title("Salary Distribution")

    plt.tight_layout()

    plt.savefig(
        "screenshots/salary_distribution.png"
    )

    print("Salary distribution saved.")