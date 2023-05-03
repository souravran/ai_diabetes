
from flask import Flask, request, render_template
import numpy as np
import pickle
import logging
import os

logging.basicConfig(
    format="%(asctime)s - %(name)s (%(filename)s:%(lineno)d) - [%(levelname)s] - %(message)s",
    level=os.environ.get("LOGLEVEL", "INFO").upper(),
)
logger = logging.getLogger(__name__)

# load prediction model
model_file = 'model/model.pkl'
predictor = pickle.load(open(model_file, 'rb'))

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def predict():
    prediction = None
    if request.method == 'POST':
        try:
            pregnancies = int(request.form['pregnancies'])
            glucose = int(request.form['glucose'])
            bp = int(request.form['bloodpressure'])
            skin = int(request.form['skinthickness'])
            insulin = int(request.form['insulin'])
            bmi = float(request.form['bmi'])
            dpf = float(request.form['dpf'])
            age = int(request.form['age'])
            
            input = np.array([[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]])
            prediction = predictor.predict(input)
        
            logger.info(f"Here is the predicted value: {prediction}")
        except ValueError:
            logger.info("Invalid integer value supplied.")

    return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
