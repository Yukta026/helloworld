from flask import Flask,render_template,request
import os
import pickle
import joblib
import numpy as np
import pandas as pd


app = Flask(__name__)

popular_path = os.path.join(os.path.dirname(__file__), 'popular.pkl')

with open(popular_path, 'rb') as file:
    popular = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
