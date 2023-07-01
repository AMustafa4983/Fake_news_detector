from pipeline import clean
from pipeline import tokenizer
import pickle

with open("pipeline/encoder", "rb") as f: 
    encoder = pickle.load(f)
