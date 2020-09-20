from pandas import np
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Flatten,Dense,Embedding,LSTM,Dropout
from preprocess import vocab, onehot, padded, sentence_length, inp_fin, out_fin
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

model = Sequential()
model.add(Embedding(vocab, 50, input_length=sentence_length))
model.add(Dropout(0.2))
model.add(LSTM(100, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(50))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

x_train, x_test, y_train, y_test = train_test_split(inp_fin, out_fin, test_size=0.2, random_state=42)

model.summary()

history = model.fit(x_train, y_train, validation_data=(x_test, y_test), batch_size=64, epochs=10)

prediction = np.argmax(model.predict(x_test), axis=-1)
print(accuracy_score(y_test, prediction))

model.save('model.h5')