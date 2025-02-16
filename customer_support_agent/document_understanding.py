# document_understanding.py
# import spacy
# nlp = spacy.load("C:/Users/HP/.conda/envs/hr_agent/lib/site-packages/spacy/data/en_core_web_sm")

# def document_understanding(document):
#     nlp = spacy.load("en_core_web_sm")
#     doc = nlp(document)
#     return doc



import spacy

# Load spaCy model once (outside the function)
nlp = spacy.load("en_core_web_sm")

def document_understanding(document):
    doc = nlp(document)  # Use the already loaded model
    return doc
