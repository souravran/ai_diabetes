
from flask import Flask, request, render_template
import logging
import os

logging.basicConfig(
    format="%(asctime)s - %(name)s (%(filename)s:%(lineno)d) - [%(levelname)s] - %(message)s",
    level=os.environ.get("LOGLEVEL", "INFO").upper(),
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def predict():
    prediction = None
    if request.method == 'POST':
        # prediction = 0
        
        logger.info(f"Here is the predicted value: {prediction}")

    return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
