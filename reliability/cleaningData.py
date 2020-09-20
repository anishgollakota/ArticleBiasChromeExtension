import pandas as pd
from pandas import DataFrame
import re
from nltk.corpus import stopwords
import nltk

article = pd.read_csv('../data/train.csv')
article.drop(['id', 'title', 'author'], axis = 1, inplace = True)
#print(tweets.Tweet[0])


# for d in article['text']:
# #     print(d)
# #     print(type(d))

stopwords = stopwords.words('english')
#add some unnecessary word to stopwords list
stopwords.append("rt")
stopwords.append("u")
stopwords.append("amp")
stopwords.append("w")
stopwords.append("th")

clean_democrat = []
count = 0
for d in article['text']:
    #d = re.sub(r'https\S+', '', d)
    if d ==d:
        print(count)
        count+=1
        d = re.sub("[^a-zA-Z]", " ", d)
        d = d.lower()
        d = nltk.word_tokenize(d)
        d = [word for word in d if not word in set(stopwords)]
        lemma = nltk.WordNetLemmatizer()
        d = [lemma.lemmatize(word) for word in d]
        d = " ".join(d)
        if d != "":
            clean_democrat.append(d)


df_dem = DataFrame(clean_democrat, columns=['Text'])
df_dem['label'] = article['label']
df_dem.to_csv('../data/clean_tweets.csv')