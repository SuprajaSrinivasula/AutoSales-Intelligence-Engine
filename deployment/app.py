from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return "Sales Prediction API Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    features = np.array(list(data.values())).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({"Predicted Units Sold": int(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True)