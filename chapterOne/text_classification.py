from transformers import pipeline
import pandas as pd

text = "Apple was founded by Steve Jobs in California, i've always liked the MacBooks computers."

# Text Classification
classifier = pipeline("text-classification")
outputs = classifier(text)
df = pd.DataFrame(outputs)
print(df)
