import unittest
from candidate_follow_up_agent.applicant_initiation import applicant_initiation
from candidate_follow_up_agent.job_description_assistance import job_description_assistance
from candidate_follow_up_agent.application_review import application_review
from candidate_follow_up_agent.schedule_interview import schedule_interview
from candidate_follow_up_agent.feedback_loop import feedback_loop
from candidate_follow_up_agent.resume_parsing import parse_resume
from candidate_follow_up_agent.candidate_ranking import rank_candidates

class TestCandidateFollowUpAgent(unittest.TestCase):
    def test_applicant_initiation(self):
        status = applicant_initiation("John Doe", "john.doe@example.com")
        self.assertIn("Email sent to John Doe", status)

    def test_job_description_assistance(self):
        job_desc = job_description_assistance("Data Scientist", ["Python", "NLP", "Machine Learning"])
        self.assertIn("Data Scientist", job_desc)
        self.assertIn("Python", job_desc)

    def test_application_review(self):
        applications = [
            {"name": "John Doe", "skills": ["Python", "NLP", "Machine Learning"]},
            {"name": "Jane Smith", "skills": ["Python", "Data Science"]}
        ]
        job_description = {"skills": ["Python", "NLP", "Machine Learning"]}
        shortlisted_candidates = application_review(applications, job_description)
        self.assertEqual(len(shortlisted_candidates), 1)
        self.assertEqual(shortlisted_candidates[0]['name'], "John Doe")

    def test_schedule_interview(self):
        status = schedule_interview("John Doe", "Jane Smith", "2025-02-20T10:00:00Z")
        self.assertIn("Interview scheduled for John Doe", status)

    def test_feedback_loop(self):
        feedback = ["Great candidate!", "Strong technical skills."]
        feedback_summary = feedback_loop(feedback)
        self.assertIn("Great candidate!", feedback_summary)
        self.assertIn("Strong technical skills.", feedback_summary)

    def test_resume_parsing(self):
        resume_text = "John Doe is a Data Scientist with skills in Python, NLP, and Machine Learning."
        parsed_skills = parse_resume(resume_text)
        self.assertIn("Python", parsed_skills)
        self.assertIn("NLP", parsed_skills)
        self.assertIn("Machine Learning", parsed_skills)

    def test_candidate_ranking(self):
        candidates = [
            {"name": "John Doe", "skills": ["Python", "NLP", "Machine Learning"]},
            {"name": "Jane Smith", "skills": ["Python", "Data Science"]}
        ]
        job_description = {"skills": ["Python", "NLP", "Machine Learning"]}
        ranked_candidates = rank_candidates(candidates, job_description)
        self.assertEqual(ranked_candidates[0]['name'], "John Doe")

if __name__ == '__main__':
    unittest.main()