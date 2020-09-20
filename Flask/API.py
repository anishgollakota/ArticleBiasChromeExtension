import flask
from politicalClassifier.testLSTM import get_score
from reliability.reliable_prediction import predict
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/getScore', methods=['GET'])
def getScore(articleBody):
    return get_score(articleBody)

@app.route('/isFakeNews', methods=['GET'])
def isFakeNews(fact):
    return predict(fact)

app.run()