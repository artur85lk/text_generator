from nltk.tokenize import WhitespaceTokenizer
from collections import defaultdict, Counter
import nltk
import random

whitespace_tokenizer = WhitespaceTokenizer()
f = input()

with open(f"{f}", "r", encoding="utf-8") as file:
    text = file.read()
    tokens = whitespace_tokenizer.tokenize(text)
    trigrams = list(nltk.trigrams(tokens))
    tri_clean = []

    for one_trigram in range(len(trigrams)):
        tri_clean += [(' '.join(trigrams[one_trigram][0:2]), trigrams[one_trigram][2])]

    frequency_dict = defaultdict(Counter)

    for head, tail in tri_clean:
        frequency_dict[head][tail] += 1

    heads = [' '.join(trigrams[i][0:2]) for i in range(len(trigrams) - 2)]

    punctuation = ['.', '?', '!']
    initials = ['-', ',', ';', '_', "/", "\\", '?', '!', '.']

    for one_sentence in range(10):

        while True:
            initial_word = random.choice(heads)

            if initial_word[0].isupper() and initial_word[0] not in punctuation \
                and initial_word[-1][-1] not in punctuation and initial_word.split()[0][-1] not in punctuation \
                    and initial_word[0] not in initials:
                break

        sentence = [initial_word]

        while True:

            tails = [T for T in frequency_dict[initial_word]]
            word_weights = [weights for weights in frequency_dict[initial_word].values()]
            next_word = Counter(random.choices(tails, weights=word_weights)).most_common(1)[0][0]
            sentence.append(next_word)
            last_word = sentence[-1]

            if len(sentence) > 3 and last_word[-1] in punctuation:
                break

            try:
                initial_word = sentence[-2].split()[1] + ' ' + sentence[-1]
            except IndexError:
                initial_word = sentence[-2] + ' ' + sentence[-1]

        print(' '.join(sentence))