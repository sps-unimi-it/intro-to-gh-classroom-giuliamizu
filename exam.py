import nltk
nltk.download('opinion_lexicon')
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.corpus import opinion_lexicon

pos_words = set(opinion_lexicon.positive())
neg_words = set(opinion_lexicon.negative())

with open("/Users/Mizu1/Nibel/Uni/Magistrale/Coding/Exam/sotu_52.txt", "r") as sotu52:
    text = sotu52.read()

words = text.split()
print(words)