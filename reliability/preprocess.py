import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Flatten,Dense,Embedding,LSTM,Dropout
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.preprocessing.sequence import pad_sequences

df = pd.read_csv("train.csv")
print(df.head())

df = df.dropna()

out = df['label']
inp = df.drop('label', axis = 1)

messages = inp.copy()
messages.reset_index(inplace=True)

ps = PorterStemmer()
corpus = []
for x in range(0, len(messages)):
    result = re.sub('[^a-zA-Z]', ' ', messages['title'][x])
    result = result.lower()
    result = result.split()
    result = [ps.stem(word) for word in result if not word in stopwords.words("english")]
    result = " ".join(result)
    corpus.append(result)

#Convert to one hot encoding
vocab = 5000
onehot = [one_hot(word, vocab) for word in corpus]

sentence_length = 20
padded = pad_sequences(onehot, padding='pre', maxlen=sentence_length)

inp_fin = np.array(padded)
out_fin = np.array(out)
