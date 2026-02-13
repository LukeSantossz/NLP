from transformers import pipeline

text = "The new restaurant downtown exceeded all my expectations. The food was absolutely delicious, the service was impeccable, and the ambiance was perfect for a romantic dinner. I highly recommend it!"

# Summarization text
summarizer = pipeline("summarization")
outputs = summarizer(text, max_length=45, clean_up_tokenization_spaces=True)
print(outputs[0]["summary_text"])
