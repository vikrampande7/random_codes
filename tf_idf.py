"""
TF-IDF from Scratch
- Term Frequency - Inverse term Frequency
- Used to find the frequency of the word in the sentence

Term Frequency TF = count of word(t) in doc / total words in doc
Document Frequency = Occurrence of word(term) in document
Inverse Document Frequency = Measures the informativeness of word(t) = N/df = log(N/(df+1))
"""
from nltk.tokenize import word_tokenize
from collections import Counter
import numpy as np


def compute_tf_idf(corpus):
    n = len(corpus)
    tokenized_corpus = [word_tokenize(doc.lower()) for doc in corpus]
    """
        Compute Term Frequency
    """
    tf = []
    for doc in tokenized_corpus:
        f = Counter(doc)
        for key in f:
            f[key] /= float(len(doc))
        tf.append(f)
    """
    Compute Inverse Document Frequency
    """
    idf = {}
    for doc in tokenized_corpus:
        for token in set(doc):
            if token not in idf:
                n_docs_with_tokens = sum(1 for d in tokenized_corpus if token in d)
                idf[token] = np.log(n/float(n_docs_with_tokens))

    tf_idf = []
    for doc_freqs in tf:
        doc_tf_idfs = {}
        for term, freq in doc_freqs.items():
            doc_tf_idfs[term] = freq * idf[term]
        tf_idf.append(doc_tf_idfs)

    return tf_idf


documents = [
    "This is the first document.",
    "This is the second second document.",
    "And the third one.",
    "Is this the first document?"
]

print(compute_tf_idf(documents))

"""
    Output:
        [{'this': 0.04794701207529681, 'is': 0.04794701207529681, 'the': 0.0, 'first': 0.11552453009332421, 
        'document': 0.04794701207529681, '.': 0.04794701207529681}, {'this': 0.04109743892168297,
         'is': 0.04109743892168297, 'the': 0.0, 'second': 0.39608410317711157, 'document': 0.04109743892168297, 
         '.': 0.04109743892168297}, {'and': 0.2772588722239781, 'the': 0.0, 'third': 0.2772588722239781, 
         'one': 0.2772588722239781, '.': 0.05753641449035617}, {'is': 0.04794701207529681, 'this': 0.04794701207529681, 
         'the': 0.0, 'first': 0.11552453009332421, 'document': 0.04794701207529681, '?': 0.23104906018664842}]
"""