from flask import Flask, render_template, request
import jsonify
import pickle
import numpy
import sklearn
from sklearn.preprocessing import LabelEncoder
import os
le=LabelEncoder()

app=Flask(__name__)
model= pickle.load(open('hr_analytics1.pkl', 'rb'))

@app.route("/", methods=['GET'])

def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])

def predict():
    if request.method== 'POST':
        gender= int(request.form['gender'])
        relevent_experience= int(request.form['relavent_experience'])
        Education_level= int(request.form['education_level'])
        experience= int(request.form['experience'])
        
        prediction= model.predict([[gender,relevent_experience, Education_level, experience]])
        output = round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry better luck next time")
        else:
            return render_template('index.html',prediction_text="You Can be selected  {}".format(output))
    else:
        return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
           
