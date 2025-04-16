from flask import Flask, render_template, request
import sqlite3
import pickle
import numpy as np

app = Flask(__name__)

# Load ML model
with open('model/genre_classifier.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    ms = float(request.form['milliseconds'])
    bytes_ = float(request.form['bytes'])
    price = float(request.form['unitprice'])

    features = np.array([[ms, bytes_, price]])
    prediction = model.predict(features)[0]

    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=False,use_reloader=False)
