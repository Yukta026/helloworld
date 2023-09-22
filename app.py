from flask import Flask,render_template,request
import os
import pickle
import joblib
import numpy as np
import pandas as pd
import logging

app = Flask(__name__)

logging.basicConfig(filename='app.log', level=logging.DEBUG)

# Define a function to load pickle files
def load_pickle(file_path):
    try:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
        return data
    except Exception as e:
        logging.error(f"Error loading pickle file '{file_path}': {str(e)}")
        return None

# Define the paths to your pickle files
script_dir = os.path.dirname(os.path.abspath(__file__))
popular_path = os.path.join(script_dir, 'popular.pkl')
pt_path = os.path.join(script_dir, 'pt.pkl')
similarity_scores_path = os.path.join(script_dir, 'similarity_scores.pkl')
# Load the pickle files
popular = load_pickle(popular_path)
pt = load_pickle(pt_path)
similarity_scores = load_pickle(similarity_scores_path)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
