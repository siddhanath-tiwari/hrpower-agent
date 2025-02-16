import spacy

# Load pre-trained NER model
nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Example usage
text = "John Doe applied for a leave starting from 2025-02-20."
entities = extract_entities(text)
print(entities)