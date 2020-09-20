import pickle
import numpy as np
import torch
import transformers as ppb

def get_score(tweet):
    model_class, tokenizer_class, pretrained_weights = (ppb.DistilBertModel, ppb.DistilBertTokenizer, 'distilbert-base-uncased')
    tokenizer = tokenizer_class.from_pretrained(pretrained_weights)
    model = model_class.from_pretrained(pretrained_weights)

    tokens_train = tokenizer.batch_encode_plus(tweet, max_length=15, padding='max_length', truncation=True)

    input_ids = torch.tensor(tokens_train['input_ids'])
    attention_mask = torch.tensor(tokens_train['attention_mask'])

    with torch.no_grad():
        last_hidden_states = model(input_ids, attention_mask=attention_mask)

    features = last_hidden_states[0][:,0,:].numpy()

    pickleFile = "logistic_reg.pkl"
    with open(pickleFile, 'rb') as file:
        pickle_model = pickle.load(file)

    result = pickle_model.predict(features)
    prob = pickle_model.predict_proba(features)
    if result ==1:
        print("Republican")
    else:
        print("Democrat")
    print("Probability is {0:.2f} %".format(100 * prob[0][result][0]))
    return result, prob

test_tweet = ['Stronger trade deals. Killing terrorists. National security tools. Justice reform. Coronavirus relief']
test_label = 1

print(get_score(test_tweet))