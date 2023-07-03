from pipeline import clean, tokenizer, encoder, translate, give_review
from keras.models import load_model

class Detector:
    def __init__(self):
        self.model = self.load_model()
        self.results = []
        return None
    
    def load_model(self):
        return load_model('models/checkpoint_01.h5')
    
    def predict(self, text):
        try:
            text = translate(text)
        except:
            print('Text already in english')
        clean_text = clean.Clean(text=text).text
        preprocessed_text = tokenizer.Tokenizer(text=clean_text).text
        prediction = self.model.predict(preprocessed_text)
        prediction = encoder.inverse_transform(prediction)
        pred_to_label = {4:'real',3:'mostly-true', 2:'half-true',1:'mostly-false' , 0:'fake' }
        label = pred_to_label[prediction[0][0]]
        review = give_review(text, label)
        return {'text': text, 'label': label,'review': review}

        