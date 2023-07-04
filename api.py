from flask import Flask, jsonify, request
from detector import Detector
import easyocr
import os 

os.environ["_BARD_API_KEY"]= 'YQhd-K3VoTIJtrpJdi4H7WFih4uI_veFBYjAbLPaYwOVe-emstt5CvSOxY1TqAmADKGFoA.'   
model = Detector()
ocr = easyocr.Reader(['en','ar'])

app = Flask(__name__)

@app.post('/predict')
def english():
    data = request.json
    try:
        sample = data['text']
    except KeyError:
        return jsonify({'error' : 'No text sent'})
        
    predictions = model.predict(sample)

    try:
        result = jsonify(predictions)
    except TypeError as e:
        result = jsonify({'error' : str(e)})
    return result

@app.post('/predict-image')
def english_image():
    data = request.files['img']
    try:
        extracted_text = ocr.readtext(data.stream.read(), detail=0, paragraph=True)
    except KeyError:
        return jsonify({'error' : 'No text sent'})
        
    text=''
    for i in extracted_text:
        text+=i
    
    predictions = model.predict(text)

    try:
        result = jsonify(predictions)
    except TypeError as e:
        result = jsonify({'error' : str(e)})
    return result

from api import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)