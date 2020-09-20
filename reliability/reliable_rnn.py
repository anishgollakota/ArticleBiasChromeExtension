import pandas as pd
import pickle
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.models import Model
from keras.layers import LSTM, Activation, Dense, Dropout, Input, Embedding
from keras.optimizers import RMSprop
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
from keras.utils import to_categorical
from keras.callbacks import EarlyStopping, ModelCheckpoint

df = pd.read_csv('train.csv')
df.drop(['id', 'title', 'author'], axis = 1, inplace = True)

print(df.head())

x_train, x_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, stratify=df['label'])

max_words = 600
max_length = 200

tokenizer = Tokenizer(num_words=max_words)
tokenizer.fit_on_texts(x_train)
sequences = tokenizer.texts_to_sequences(x_train)
padded_sequences = sequence.pad_sequences(sequences, maxlen=max_length)

with open('tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

def RNN():
    inputs = Input(name='inputs',shape=[max_length])
    layer = Embedding(max_words,50,input_length=max_length)(inputs)
    layer = LSTM(64)(layer)
    layer = Dense(256,name='FC1')(layer)
    layer = Activation('relu')(layer)
    layer = Dropout(0.3)(layer)
    layer = Dense(1,name='out_layer')(layer)
    layer = Activation('sigmoid')(layer)
    model = Model(inputs=inputs,outputs=layer)
    return model

checkpoint = ModelCheckpoint(
    "reliable_model.h5",
    monitor="val_acc",
    save_best_only=True,
    mode='max',
    verbose=1
)

callbacks = [checkpoint]

model = RNN()
model.summary()
model.compile(loss='binary_crossentropy',optimizer=RMSprop(),metrics=['accuracy'])

history = model.fit(padded_sequences, y_train, batch_size = 64, epochs = 10,
                    validation_split=0.2, callbacks=callbacks)

model.save('reliable_model.h5')

test_sequences = tokenizer.texts_to_sequences(x_test)
test_sequences_padded = sequence.pad_sequences(test_sequences, maxlen=max_length)

accr = model.evaluate(test_sequences_padded, y_test)
print(accr)