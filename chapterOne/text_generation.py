from transformers import pipeline

text = "Apple was founded by Steve Jobs in California, i've always liked the MacBooks computers."

# Text Generation
generator = pipeline("text-generation")
response = "Dear customer, we are happy to hear such a good feedback."
prompt = text + "\n\nCustomer service response:\n" + response
outputs = generator(prompt, max_length=200)
print(outputs[0]["generated_text"])
