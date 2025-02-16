# import spacy

# # Load NLP model
# nlp = spacy.load("en_core_web_sm")

# def parse_resume(resume_text):
#     doc = nlp(resume_text)
#     skills = [ent.text for ent in doc.ents if ent.label_ == "SKILL"]
#     return skills

# # Example usage
# resume_text = "John Doe is a Data Scientist with skills in Python, NLP, and Machine Learning."
# parsed_skills = parse_resume(resume_text)
# print(parsed_skills)

import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")

# Custom Skill List
skill_phrases = ["Python", "Machine Learning", "NLP", "Data Science", "Deep Learning"]
matcher = PhraseMatcher(nlp.vocab)
patterns = [nlp.make_doc(skill) for skill in skill_phrases]
matcher.add("SKILLS", patterns)

def parse_resume(resume_text):
    doc = nlp(resume_text)
    matches = matcher(doc)
    skills = [doc[start:end].text for match_id, start, end in matches]
    return skills

# Example usage
resume_text = "John is an expert in Python and Machine Learning."
parsed_skills = parse_resume(resume_text)
print("Extracted Skills:", parsed_skills)
