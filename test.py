from detector import Detector


model_en = Detector()
english_text = 'Climate changed naturally in prehistoric eras, modern climate change is a naturally occurring phenomenon'

# Enter your text here 
english_prediction = model_en.predict(english_text) # English text


#print(f'Our result: {english_prediction}')
print(english_prediction)