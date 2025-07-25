import re
import numpy as np
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.preprocessing.sequence import pad_sequences
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

ps=PorterStemmer()
stop_words=set(stopwords.words('english'))
voc_size=5000
max_length=30

def preprocess_text(text):
    review=re.sub('[^a-zA-Z0-9]',' ',text)
    review=review.lower()
    reveiw=review.split()
    review=[ps.stem(word) for word in review if word not in stop_words]
    review=' '.join(review)
    one_hot_repr=one_hot(review,voc_size)
    padded_text=pad_sequences([one_hot_repr],maxlen=max_length,padding='pre')
    return padded_text
