import stanza

# download model (only first time)


# load pipeline
nlp = stanza.Pipeline(lang='en')
# test sentence
text = "Siri eats mango"

doc = nlp(text)

for sentence in doc.sentences:
    for word in sentence.words:
        head = "ROOT" if word.head == 0 else sentence.words[word.head - 1].text
        print(word.text, "→", word.deprel, "→", head)