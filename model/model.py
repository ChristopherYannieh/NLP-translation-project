import pickle
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import logging
import os

# hide TF warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def load_tokenizer(tokenizer_file):
    # Load tokenizer
    with open(tokenizer_file, 'rb') as handle:
        tokenizer = pickle.load(handle)
    return tokenizer

class Translator:
    # Load tokenizer
    english_tokenizer = load_tokenizer('english_tokenizer.pickle')
    french_tokenizer = load_tokenizer('french_tokenizer.pickle')

    def __init__(self, model_path):
        self.model = load_model(model_path)
        logging.info("Model loaded!")
        
        # Define Prepare token dictionary function
    def prepare_token_dictionary(self):
        token_dict = {}
        for key, value in self.french_tokenizer.word_index.items():
            token_dict[value] = key
        return token_dict

    # Define translate function
    def translate(self, input):
        # Tokenize input
        input_tokens = self.english_tokenizer.texts_to_sequences(input)

        # Apply post-padding to the sequences
        X = pad_sequences(input_tokens, maxlen=15, padding='post',  truncating='post')
        
        # Predict translation in french 
        encoded_output = self.model.predict(X)

        # Decode output
        decoded_output = np.argmax(encoded_output, axis = -1)[0]
        token_dict = self.prepare_token_dictionary()
        fr_output = ' '.join([token_dict[i] for i in decoded_output.flatten() if i !=0])

        # Return output
        return fr_output