import pandas as pd
from pandas import DataFrame
import re
from nltk.corpus import stopwords
import nltk

tweets = pd.read_csv('../data/ExtractedTweets.csv')
#print(tweets.Tweet[0])

democrat = tweets[tweets.Party == 'Democrat']
republican = tweets[tweets.Party == 'Republican']

stopwords = stopwords.words('english')
#add some unnecessary word to stopwords list
stopwords.append("rt")
stopwords.append("u")
stopwords.append("amp")
stopwords.append("w")
stopwords.append("th")

clean_democrat = []
for d in democrat.Tweet:
    d = re.sub(r'https\S+', '', d)
    d = re.sub("[^a-zA-Z]", " ", d)
    d = d.lower()
    d = nltk.word_tokenize(d)
    d = [word for word in d if not word in set(stopwords)]
    lemma = nltk.WordNetLemmatizer()
    d = [lemma.lemmatize(word) for word in d]
    d = " ".join(d)
    clean_democrat.append(d)

clean_republican = []
for r in republican.Tweet:
    r = re.sub(r'https\S+', '', r)
    r = re.sub("[^a-zA-Z]", " ", r)
    r = r.lower()
    r = nltk.word_tokenize(r)
    r = [word for word in r if not word in set(stopwords)]
    lemma = nltk.WordNetLemmatizer()
    r = [lemma.lemmatize(word) for word in r]
    r = " ".join(r)
    clean_republican.append(r)


df_dem = DataFrame(clean_democrat, columns=['Tweet'])
df_dem['label'] = 0
df_rp = DataFrame(clean_republican, columns=['Tweet'])
df_rp['label'] = 1
complete_data = pd.concat([df_dem, df_rp], axis=0)
complete_data.to_csv('../data/clean_tweets.csv')