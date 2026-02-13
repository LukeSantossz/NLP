from transformers import pipeline

text = "The new restaurant downtown exceeded all my expectations. The food was absolutely delicious, the service was impeccable, and the ambiance was perfect for a romantic dinner. I highly recommend it!"

# Text Translation
translator = pipeline("translation_en_to_de", model="Helsinki-NLP/opus-mt-en-de")
outputs = translator(text, clean_up_tokenization_spaces=True)
print(outputs[0]["translation_text"])
