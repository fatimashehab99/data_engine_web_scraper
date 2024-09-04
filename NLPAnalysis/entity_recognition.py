import spacy
from markdown_it.common.entities import entities

# Load the pre-trained model
nlp = spacy.load("en_core_web_sm")


def entity_recognition(text):
    entities = []
    # Process the text with spaCy
    doc = nlp(text)
    # Extract and print named entities
    for ent in doc.ents:
        entities.append({"text": ent.text, "label": ent.label_})
    return entities


