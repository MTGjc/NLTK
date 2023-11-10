import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

text = """Deliverables:A write-up (max 2 pages long) introducing your idea while touching upon all the criteria mentioned above
A 4min presentation (powerpoint/keynote) of your proposal. Be prepared to present it in class.
A portrait video, based on the ’52 Portraits’ project by Jonathan Burrows. """

stop_words = set(stopwords.words('english'))
# print (stop_words)
tokenized_words = word_tokenize(text)

#remove punctuations
#define p
punctuations_to_remove = [',', '.', ' ', ':', ';', '’', '(', ')', '[', ']', '{', '}']
words = [word for word in tokenized_words if word not in punctuations_to_remove and word.isalpha()]

#store keywords into array
keywords = []

for w in words:
    if w not in stop_words:
        keywords.append(w)
#stopwords:
the_stopword = set(words)- set(keywords)
print ("keywords include:", keywords)

print ("stopwords include:", the_stopword)