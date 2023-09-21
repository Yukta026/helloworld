from flask import Flask,render_template,request
import pickle
import numpy as np

popular_df = pickle.load(open('templates/popular.pkl','rb'))
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
