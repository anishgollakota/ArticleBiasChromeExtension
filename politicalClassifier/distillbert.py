import pandas as pd
import numpy as np
from transformers import AutoModel, BertTokenizerFast, AdamW, BertModel
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import transformers as ppb
import torch

tweets = pd.read_csv('../data/clean_tweets.csv')

#split into training/testing
#train_text, test_text, train_label, test_label = train_test_split(tweets['Tweet'], tweets['label'], random_state=2020, test_size=0.25, stratify=tweets['label'])

# seq_len = [len(i.split()) for i in train_text]
# pd.Series(seq_len).hist(bins=30)
# plt.show()

model_class, tokenizer_class, pretrained_weights = (ppb.BertModel, ppb.BertTokenizer, 'bert-base-uncased')

# Load pretrained model/tokenizer
tokenizer = tokenizer_class.from_pretrained(pretrained_weights)
model = model_class.from_pretrained(pretrained_weights)

#tokenize tweets
#tokenized = tweets['Tweet'].apply((lambda x: tokenizer.encode(x, add_special_tokens=True)))
tokens_train = tokenizer.batch_encode_plus(tweets['Tweet'].tolist(), max_length=15, padding='max_length', truncation=True)

max_len = 15

padded = np.array([i + [0]*(max_len-len(i)) for i in tokens_train['input_ids']])

attention_mask = np.where(padded != 0, 1, 0)
input_ids = torch.tensor(padded)
print(input_ids)
attention_mask = torch.tensor(attention_mask)

with torch.no_grad():
    last_hidden_states = model(input_ids, attention_mask=attention_mask)

features = last_hidden_states[0][:,0,:].numpy()
labels = tweets[1]

train_features, test_features, train_labels, test_labels = train_test_split(features, labels)

lr_clf = LogisticRegression()
lr_clf.fit(train_features, train_labels)

lr_clf.score(test_features, test_labels)
