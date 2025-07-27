# ner_utils.py

import spacy

# Load transformer-based spaCy model (uses RoBERTa under the hood)
nlp = spacy.load("en_core_web_trf")

def extract_entities(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]
