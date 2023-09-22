from flask import Flask,render_template,request
import pickle
import numpy as np




app = Flask(__name__)

popular_df = pickle.load(open("popular.pkl","rb"))

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
