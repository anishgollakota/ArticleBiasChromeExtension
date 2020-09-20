import pickle
import keras
from keras_preprocessing import sequence

def get_score(tweet):

    reconstructed_model = keras.models.load_model("lstm_model")

    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    sequences_test = tokenizer.texts_to_sequences(tweet)
    sequences_matrix_test = sequence.pad_sequences(sequences_test, maxlen=20)

    prediction = reconstructed_model.predict(sequences_matrix_test)[0][0]
    return prediction

test_tweet = ['We are fighting for a better, fairer, and brighter future for every American: rolling up our sleeves, empowering grassroots voters, and organizing everywhere to take our country back.']
test_label = 0

print(get_score(test_tweet))