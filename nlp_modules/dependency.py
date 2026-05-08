import stanza

# English pipeline
nlp_en = stanza.Pipeline(lang='en')

# Hindi pipeline
nlp_hi = stanza.Pipeline(lang='hi')


def parse_sentence(text, lang='en'):

    # choose language pipeline
    if lang == 'hi':
        doc = nlp_hi(text)
    else:
        doc = nlp_en(text)

    result = []

    for sentence in doc.sentences:
        for word in sentence.words:

            head = "ROOT" if word.head == 0 else sentence.words[word.head - 1].text

            result.append({
                "word": word.text,
                "dep": word.deprel,
                "head": head
            })

    return result