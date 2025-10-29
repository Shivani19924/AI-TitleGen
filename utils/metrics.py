from nltk import ngrams

def distinct_n(candidates, n=3):
    all_ngrams = []
    for text in candidates:
        all_ngrams += list(ngrams(text.split(), n))
    total = len(all_ngrams)
    unique = len(set(all_ngrams))
    return unique / total if total > 0 else 0
