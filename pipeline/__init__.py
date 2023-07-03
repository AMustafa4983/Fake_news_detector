from pipeline import clean, tokenizer
import pickle
from translate import Translator


with open("pipeline/encoder", "rb") as f: 
    encoder = pickle.load(f)


translator = Translator(from_lang='arabic', to_lang='english')


def translate(text):
    return translator.translate(text)


from bardapi import Bard


def give_review(text,label):
    response = Bard().get_answer(f'why the following text {text}. is {label}')['content']
    return response

