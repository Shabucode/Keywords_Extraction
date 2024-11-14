from keybert import KeyBERT

# Initialize KeyBERT model
kw_model = KeyBERT()

#text
text = "Spacetime is a mathematical model that combines space and time into a single continuum."

# Extract keywords
keywords = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words="english", top_n=5)

# Print keywords and their scores
print(keywords)
