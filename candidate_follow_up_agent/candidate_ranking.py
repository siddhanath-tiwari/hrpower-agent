# def rank_candidates(candidates, job_description):
#     ranked_candidates = sorted(candidates, key=lambda x: len(set(x['skills']) & set(job_description['skills'])), reverse=True)
#     return ranked_candidates

# # Example usage
# candidates = [
#     {"name": "John Doe", "skills": ["Python", "NLP", "Machine Learning"]},
#     {"name": "Jane Smith", "skills": ["Python", "Data Science"]}
# ]
# job_description = {"skills": ["Python", "NLP", "Machine Learning"]}
# ranked_candidates = rank_candidates(candidates, job_description)
# for candidate in ranked_candidates:
#     print(f"Ranked: {candidate['name']}")



def rank_candidates(candidates, job_description):
    required_skills = set(job_description['skills'])

    def score(candidate):
        candidate_skills = set(candidate['skills'])
        match_score = len(candidate_skills & required_skills) / len(required_skills)
        return match_score

    ranked_candidates = sorted(candidates, key=score, reverse=True)
    return ranked_candidates

# Example usage
candidates = [
    {"name": "John Doe", "skills": ["Python", "NLP", "Machine Learning"]},
    {"name": "Jane Smith", "skills": ["Python", "Data Science"]},
    {"name": "Alice Brown", "skills": ["NLP", "Deep Learning", "Python"]}
]

job_description = {"skills": ["Python", "NLP", "Machine Learning"]}

ranked_candidates = rank_candidates(candidates, job_description)
for i, candidate in enumerate(ranked_candidates, start=1):
    print(f"Rank {i}: {candidate['name']}")
