import flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin

from politicalClassifier.testLSTM import get_score
from reliability.reliable_prediction import predict

app = flask.Flask(__name__)
app.config["DEBUG"] = True
#app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app)

articleBody = ''

@app.route('/', methods=['GET'])
def home():
    return "Pranav, Abhijaat, Anish, Saarthak"

@app.route('/getScore', methods=['POST'])
#@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def getScore():
    articleBody = request.json['article']
    return jsonify(str(get_score(articleBody)))

# @app.route('/sendArticle', methods=['POST'])
# def sendArticle():

@app.route('/isFakeNews', methods=['POST'])
def isFakeNews():
    articleBody = request.json['article']
    return jsonify(str(predict(articleBody)))

app.run()