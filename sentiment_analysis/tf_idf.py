from math import log10
# t is token
# d is document == tokens
def f(t, d):
    return d.count(t)
def tf(t, d):
    return 0.5 + 0.5*f(t,d)/max([f(w,d) for w in d])
    
def idf(t, D):
    # D is documents
    numerator = len(D)
    denominator = 1 + len([True for d in D if t in d])
    return log10(numerator/denominator)

def tfidf(t, d, D):
    return tf(t, d)*idf(t, D)