import re
import string
import nltk
from nltk.corpus import stopwords

class Clean:
    def __init__(self, text):
        self.text = text
        self.text = self.clean_english_text()
        return None
    
        # Remove Stopwords
    def remove_english_stopwords(self):
        stop_words = stopwords.words('english')
        words = self.text.split()
        filtered_sentence = ''
        for word in words:
            if word not in stop_words:
                filtered_sentence = filtered_sentence + word + ' '
        return filtered_sentence


    # Remove Punvtuation
    def remove_punctuation(self):
        table = str.maketrans('','',string.punctuation)
        words = self.text.split()
        filtered_sentence = ''
        for word in words:
            word = word.translate(table)
            filtered_sentence = filtered_sentence + word + ' '
        return filtered_sentence

    # Normalize Text
    def normalize_english_text(self):
        self.text = self.text.lower()
        # get rid of urls
        self.text = re.sub('https?://\S+|www\.\S+', '', self.text)
        # get rid of non words and extra spaces
        self.text = re.sub('\\W', ' ', self.text)
        self.text = re.sub('\n', '', self.text)
        self.text = re.sub(' +', ' ', self.text)
        self.text = re.sub('^ ', '', self.text)
        self.text = re.sub(' $', '', self.text)
        return self.text

    def clean_english_text(self):
        self.text = self.text.replace(',',' , ')
        self.text = self.text.replace('.',' . ')
        self.text = self.text.replace('/',' / ')
        self.text = self.text.replace('@',' @ ')
        self.text = self.text.replace('#',' # ')
        self.text = self.text.replace('?',' ? ')
        self.text = self.normalize_english_text()
        self.text = self.remove_punctuation()
        self.text = self.remove_english_stopwords()

        return self.text