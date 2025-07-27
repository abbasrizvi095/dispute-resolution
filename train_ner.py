# train_ner.py

import spacy
from spacy.tokens import DocBin
from banking_ner_training_data import TRAIN_DATA

nlp = spacy.blank("en")
ner = nlp.add_pipe("ner")

for _, annotations in TRAIN_DATA:
    for ent in annotations["entities"]:
        ner.add_label(ent[2])

doc_bin = DocBin()
skipped = 0

for text, annotations in TRAIN_DATA:
    doc = nlp.make_doc(text)
    ents = []
    for start, end, label in annotations["entities"]:
        span = doc.char_span(start, end, label=label)
        if span is None:
            print(f"⚠️ Skipping misaligned entity: {text[start:end]}")
            continue
        ents.append(span)
    if ents:
        doc.ents = ents
        doc_bin.add(doc)
    else:
        skipped += 1

doc_bin.to_disk("train.spacy")

print(f"✅ Training examples saved. Skipped {skipped} due to misalignment.")

# Train the model
nlp.begin_training()
for i in range(20):
    losses = {}
    batches = spacy.util.minibatch(TRAIN_DATA, size=2)
    for batch in batches:
        texts, annotations = zip(*batch)
        examples = [spacy.training.Example.from_dict(nlp.make_doc(text), ann)
                    for text, ann in zip(texts, annotations)]
        nlp.update(examples, losses=losses)
    print(f"Iteration {i + 1} - Losses: {losses}")

nlp.to_disk("custom_ner_model")
print("✅ Model trained and saved to custom_ner_model/")
