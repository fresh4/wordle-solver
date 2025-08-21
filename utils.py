import string
from english_words import english_words_lower_set as words

def set_wordles():
    wordles = words.copy()
    for word in words:
        if(len(word) != 5):
            wordles.remove(word)
    return wordles

def set_letter_score():
    wordles = set_wordles()
    alphabet = list(string.ascii_lowercase)
    score = list()
    for letter in alphabet:
        score.append(0)
    alphabet_score = dict()

    for word in wordles:
        for letter in alphabet:
            if letter in word:
                score[alphabet.index(letter)] += 1
    
    for letter in alphabet:
        alphabet_score[letter] = score[alphabet.index(letter)]
        
    alphabet_score = dict(
        sorted(
            alphabet_score.items(), 
            key=lambda x: x[1], 
            reverse=True))

    return alphabet_score

def set_likely_words(wordles, alphabet_score):
    best_words = dict()
    for word in wordles:
        best_words[word] = 0

    for word in wordles:
        for i in range(8):
            if list(alphabet_score)[i] in word:
                best_words[word] += 1
        
    best_words = dict(
            sorted(
                best_words.items(), 
                key=lambda x: x[1], 
                reverse=True))
    return best_words

