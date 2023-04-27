
from flask import Flask, request, Response, make_response, render_template
import logging
import os

import pickle
import numpy as np

logging.basicConfig(
    format="%(asctime)s - %(name)s (%(filename)s:%(lineno)d) - [%(levelname)s] - %(message)s",
    level=os.environ.get("LOGLEVEL", "INFO").upper(),
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

# POST
# ----------------------------------------------------------------------------------------------------------------------
@app.route("/predict", methods=["POST"])
def predict():
    # preg = int(request.form['pregnancies'])
    # glucose = int(request.form['glucose'])
    # bp = int(request.form['bloodpressure'])
    # st = int(request.form['skinthickness'])
    # insulin = int(request.form['insulin'])
    # bmi = float(request.form['bmi'])
    # dpf = float(request.form['dpf'])
    # age = int(request.form['age'])
    
    # data = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
    # my_prediction = classifier.predict(data)
    my_prediction = 0.2
    
    logger.info(f"Here is the predicted value: {my_prediction}")

    return render_template('prediction.html', prediction=my_prediction)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
