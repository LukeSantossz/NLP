from transformers import pipeline
import pandas as pd
import torch

text = "Apple was founded by Steve Jobs in California, i've always liked the MacBooks computers."

# Text Classification
# classifier = pipeline("text-classification")
# outputs = classifier(text)
# df = pd.DataFrame(outputs)
# print(df)

# Named Entity Recognition
# ner_tagger = pipeline("ner", aggregation_strategy="simple")
# outputs = ner_tagger(text)
# df = pd.DataFrame(outputs)
# print(df)

# Question Answering
# reader = pipeline("question-answering")
# question = "What does the customer want?"
# outputs = reader(question=question, context=text)
# df = pd.DataFrame([outputs])
# print(df)

