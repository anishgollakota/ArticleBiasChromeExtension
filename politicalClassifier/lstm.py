import pandas as pd
import numpy as np
from keras_preprocessing import sequence
from keras_preprocessing.text import Tokenizer
from transformers import AutoModel, BertTokenizerFast, AdamW, BertModel
from sklearn.model_selection import train_test_split
from keras import Input, Model
from keras.layers import Dense, Dropout, LSTM, Embedding, Activation
from keras.optimizers import RMSprop, Adam
from keras.callbacks import EarlyStopping, ModelCheckpoint
import pickle

def RNN():
    inputs = Input(name='inputs',shape=[max_len])
    layer = Embedding(max_words,50,input_length=max_len)(inputs)
    layer = LSTM(32)(layer)
    layer = Dense(256,name='FC1')(layer)
    layer = Activation('relu')(layer)
    layer = Dropout(0.3)(layer)
    layer = Dense(16)(layer)
    layer = Dense(1,name='out_layer')(layer)
    layer = Activation('sigmoid')(layer)
    model = Model(inputs=inputs,outputs=layer)
    return model

tweets = pd.read_csv('../data/clean_tweets.csv')

#split into training/testing
train_text, test_text, train_label, test_label = train_test_split(tweets['Tweet'], tweets['label'], random_state=2020, test_size=0.25, stratify=tweets['label'])

max_words = 10000
max_len = 15
tok = Tokenizer(num_words=max_words)
tok.fit_on_texts(train_text)
sequences = tok.texts_to_sequences(train_text)
sequences_matrix = sequence.pad_sequences(sequences,maxlen=max_len)

model = RNN()
model.summary()
model.compile(loss='binary_crossentropy',optimizer= Adam(),metrics=['accuracy'])

#model.fit(sequences_matrix,train_label,batch_size=128,epochs=10,
          #validation_split=0.2,callbacks=[EarlyStopping(monitor='val_loss',min_delta=0.0001)])

checkpoint = ModelCheckpoint("simple_model.h5", monitor="val_acc", save_best_only=True, mode='max', verbose=1)
model.fit(sequences_matrix,train_label,batch_size=128,epochs=8, callbacks=[checkpoint], validation_split=0.2)

sequences_test = tok.texts_to_sequences(test_text)
sequences_matrix_test = sequence.pad_sequences(sequences_test,maxlen=max_len)

accuracy = model.evaluate(sequences_matrix_test, test_label)
print('Test set\n  Loss: {:0.3f}\n  Accuracy: {:0.3f}'.format(accuracy[0], accuracy[1]))

model.save("lstm_model")

with open('tokenizer.pickle', 'wb') as handle:
    pickle.dump(tok, handle, protocol=pickle.HIGHEST_PROTOCOL)