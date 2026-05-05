from flask import Flask
from src.logger import logging

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    logging.info("Testing the Log file")

    return "ML with Husnain Khalid"

if __name__ == "__main__":
    app.run(debug = True) # 5000