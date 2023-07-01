import json
from keras.utils import pad_sequences
from keras.preprocessing.text import tokenizer_from_json

class Tokenizer:
    def __init__(self, text):
        self.text = [text]
        self.max_length = 25
        self.trunc_type = 'post'
        self.padding_type = 'post'
        self.tokenizer = self.load_data()
        self.text = self.tokenize()
        self.text = self.padding()
        return None
    
    def load_data(self):
        with open('tokenizer/tok_conf.json') as json_file:
            self.tokenizer = tokenizer_from_json(json.load(json_file))
        return self.tokenizer
    
    def tokenize(self):
        self.text = self.tokenizer.texts_to_sequences(self.text)
        return self.text
    
    def padding(self):
        self.text = pad_sequences(self.text, maxlen=self.max_length,
                         padding=self.padding_type,
                         truncating=self.trunc_type)
        return self.text
