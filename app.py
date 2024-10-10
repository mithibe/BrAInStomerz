from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import joblib # For loading the saved model

app = Flask(__name__)

# Load the trained model (Make sure to train and save your model using joblib)
model = joblib.load('career_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods['POST'])
def predict():
    # Get the data from the form data into the format by the model
    input_data = pd.DataFrame([data], columns=['PhysicsScore', 'BiologyScore','MathematicsScore', 'EnglishScore', 'SportsParticipation', 'SportsAchievements', 'ExtracurricularActivities', 'LeadershipRole', 'STEMPathway'])

    # Perform prediction
    prediction = model.predict(input_data)

    # Return the result
    return jsonify({'prediction': prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)