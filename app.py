from flask import Flask, request, jsonify, render_template 
import os
from flask_cors import CORS, cross_origin
from CNN_Classifier.pipeline.prediction import PredictionPipeline 
from CNN_Classifier.utils.common import decodeImage 

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self): 
        self.filename = "input_image.jpg"
        self.classifier = PredictionPipeline(self.filename)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')




@app.route("/predict", methods=['POST'])
@cross_origin()
def predict():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predict() 
    return jsonify(result)
 
if __name__ == "__main__":
    clApp = ClientApp() 
    app.run(debug=True)
