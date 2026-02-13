from transformers import pipeline
import pandas as pd

text = "Apple was founded by Steve Jobs in California, i've always liked the MacBooks computers."

# Named Entity Recognition
ner_tagger = pipeline("ner", aggregation_strategy="simple")
outputs = ner_tagger(text)
df = pd.DataFrame(outputs)
print(df)
