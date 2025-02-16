# def application_review(applications, job_description):
#     shortlisted = []
#     for application in applications:
#         if all(skill in application['skills'] for skill in job_description['skills']):
#             shortlisted.append(application)
#     return shortlisted


def application_review(applications, job_description, threshold=0.7):
    shortlisted = []
    required_skills = set(job_description['skills'])

    for application in applications:
        applicant_skills = set(application['skills'])
        match_score = len(applicant_skills & required_skills) / len(required_skills)

        if match_score >= threshold:
            shortlisted.append(application)

    return shortlisted
