import pandas as pd
import numpy as np
from transformers import AutoModel, BertTokenizerFast, AdamW, BertModel
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import transformers as ppb
import torch
import pickle
import torch.nn as nn
from keras import Input, Model
from keras.layers import Dense, Dropout, LSTM, Embedding, Activation
from keras.optimizers import RMSprop, Adam

tweets = pd.read_csv('../data/clean_tweets.csv')

#split into training/testing
train_text, test_text, train_label, test_label = train_test_split(tweets['Tweet'], tweets['label'], random_state=2020, test_size=0.2, stratify=tweets['label'])

# seq_len = [len(i.split()) for i in train_text]
# pd.Series(seq_len).hist(bins=30)
# plt.show()

model_class, tokenizer_class, pretrained_weights = (ppb.DistilBertModel, ppb.DistilBertTokenizer, 'distilbert-base-uncased')

# Load pretrained model/tokenizer
tokenizer = tokenizer_class.from_pretrained(pretrained_weights)
model = model_class.from_pretrained(pretrained_weights)

#tokenize tweets
#tokenized = tweets['Tweet'].apply((lambda x: tokenizer.encode(x, add_special_tokens=True)))
tokens_train = tokenizer.batch_encode_plus(tweets['Tweet'], max_length=15, padding='max_length', truncation=True)

input_ids = torch.tensor(tokens_train['input_ids'])
attention_mask = torch.tensor(tokens_train['attention_mask'])

print('Model has begun')
with torch.no_grad():
    last_hidden_states = model(input_ids, attention_mask=attention_mask)
print('Model has ended')

features = last_hidden_states[0][:,0,:].numpy()
labels = tweets['Label']

train_features, test_features, train_labels, test_labels = train_test_split(features, labels)
lr_clf = LogisticRegression(max_iter = 1000)
lr_clf.fit(train_features, train_labels)
accuracy = lr_clf.score(test_features, test_labels)
probability = lr_clf.predict_proba(test_features)
print(accuracy)
print(probability)

pickleFile = "logistic_reg.pkl"
with open(pickleFile, 'wb') as file:
    pickle.dump(lr_clf, file)

# train_features = np.reshape(train_features, (train_features.size, 1))
#
# def FFN():
#     inputs = Input(name='inputs',shape=[train_features.size])
#     layer = Dense(256,name='FC1')(inputs)
#     layer = Activation('relu')(layer)
#     layer = Dense(1,name='out_layer')(layer)
#     layer = Activation('sigmoid')(layer)
#     model = Model(inputs=inputs,outputs=layer)
#     return model
#
# model = FFN()
# model.summary()
# model.compile(loss='binary_crossentropy',optimizer=RMSprop(),metrics=['accuracy'])
#
# model.fit(train_features,train_label,batch_size=128,epochs=8, validation_split=0.2)
#
# accuracy = model.evaluate(test_features, test_label)
# print('Test set\n  Loss: {:0.3f}\n  Accuracy: {:0.3f}'.format(accuracy[0], accuracy[1]))