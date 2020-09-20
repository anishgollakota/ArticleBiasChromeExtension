import pandas as pd
import torch
import numpy as np
import transformers
from transformers import AutoModel, BertTokenizerFast, AdamW, BertModel
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import torch.nn as nn
import tensorflow
from keras import Input, Model
from keras.layers import Dense, Flatten, Dropout
from keras.losses import SparseCategoricalCrossentropy
from keras.metrics import SparseCategoricalAccuracy

# class Bert_Arch(nn.Module):
#     def __init__(self, bert):
#         super(Bert_Arch, self).__init__()
#         self.bert = bert
#         self.fc1 = nn.Linear(768, 256)
#         self.fc2 = nn.Linear(256, 1)
#     def forward(self, input_id, mask):


tweets = pd.read_csv('../data/clean_tweets.csv')

#split into training/testing
train_text, test_text, train_label, test_label = train_test_split(tweets['Tweet'], tweets['label'], random_state=2020, test_size=0.25, stratify=tweets['label'])

model = BertModel.from_pretrained('bert-base-uncased', output_hidden_states=True)
tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased')

# seq_len = [len(i.split()) for i in train_text]
# pd.Series(seq_len).hist(bins=30)
# plt.show()

#tokenize and encode sentences
tokens_train = tokenizer.batch_encode_plus(train_text.tolist(), max_length=15, padding='max_length', truncation=True)
tokens_test = tokenizer.batch_encode_plus(test_text.tolist(), max_length=15, padding='max_length', truncation=True)

train_input_ids = torch.tensor(tokens_train['input_ids'])
train_attention_mask = torch.tensor(tokens_train['attention_mask'])
train_token_ids = torch.tensor(tokens_train['token_type_ids'])

train_inputs = [train_input_ids, train_attention_mask, train_token_ids]

print(train_inputs[0][0])

def convert_inputs_to_tf_dataset(inputs):
    # args.max_seq_len = 256
    ids = inputs[0][0]
    masks = inputs[1][0]
    token_types = inputs[2][0]

    ids = torch.reshape(ids, (-1, 15))
    print("Input ids shape: ", ids.shape)
    masks = torch.reshape(masks, (-1, 15))
    print("Input Masks shape: ", masks.shape)
    token_types = torch.reshape(token_types, (-1, 15))
    print("Token type ids shape: ", token_types.shape)

    ids=ids.numpy()
    masks = masks.numpy()
    token_types = token_types.numpy()

    return [ids, masks, token_types]

inputs = convert_inputs_to_tf_dataset(train_inputs)

input_ids_layer = Input(shape=(15, ), dtype=np.int32)
input_mask_layer = Input(shape=(15, ), dtype=np.int32)
input_token_type_layer = Input(shape=(15,), dtype=np.int32)

bert_layer = model([input_ids_layer, input_mask_layer, input_token_type_layer])[0]
print(bert_layer)
flat_layer = Flatten()(bert_layer)
dropout= Dropout(0.3)(flat_layer)
dense_output = Dense(1, activation='softmax')(dropout)

model_ = Model(inputs=[input_ids_layer, input_mask_layer, input_token_type_layer], outputs=dense_output)

loss = SparseCategoricalCrossentropy(from_logits=True)
metric = SparseCategoricalAccuracy('accuracy')
model.compile(optimizer='adam', loss=loss, metrics=[metric])
#model.fit(inputs=inputs, outputs=..., validation_data=..., epochs=50, batch_size = 32, metrics=metric, verbose=1)

train_mask = tokens_train['attention_mask']
cross_entropy = nn.NLLLoss()

# def train():
#     model.train()
#     loss, accuracy = 0
#     total_pred = []


optimizer = AdamW(model.parameters(), lr=1e-4)