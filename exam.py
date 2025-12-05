# %%
import nltk
nltk.download('opinion_lexicon')
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.corpus import opinion_lexicon
import string

pos_words = set(opinion_lexicon.positive())
neg_words = set(opinion_lexicon.negative())

# %%
with open("/Users/Mizu1/Nibel/Uni/Magistrale/Coding/Exam/sotu_52.txt", "r") as sotu52:
    text = sotu52.read()

for p in string.punctuation:
    text = text.replace(p, "")

words = text.split()

pos_52 = 0
neg_52 = 0

for w in words:
    if w in pos_words:
        pos_52 += 1
    elif w in neg_words:
        neg_52 += 1

sentiment_52 = pos_52 - neg_52

print("Positive words in the 1952 State of the Union speech:", pos_52)
print("Negative words in the 1952 State of the Union speech:", neg_52)
print("Sentiment score of the 1952 State of the Union speech:", sentiment_52) 
# %%