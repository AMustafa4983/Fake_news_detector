from flask import Flask, jsonify, request
from detector import Detector
import os 

os.environ["_BARD_API_KEY"]= 'YQhd-K3VoTIJtrpJdi4H7WFih4uI_veFBYjAbLPaYwOVe-emstt5CvSOxY1TqAmADKGFoA.'   
model = Detector()

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

if __name__ == '__main__':
    app.run(host='0.0.0.0')