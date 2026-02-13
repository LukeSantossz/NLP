from transformers import pipeline
import pandas as pd

text = "Apple was founded by Steve Jobs in California, i've always liked the MacBooks computers."

# Question Answering
reader = pipeline("question-answering")
question = "Who founded Apple?"
outputs = reader(question=question, context=text)
df = pd.DataFrame([outputs])
print(df)
