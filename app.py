from flask import Flask, render_template, request, jsonify
from predictor import load_trained_model, predict_next_word

app = Flask(__name__)

# Load models for each style
models = {
    "casual": load_trained_model("models/casual_model.h5"),
    "formal": load_trained_model("models/formal_model.h5"),
    "technical": load_trained_model("models/technical_model.h5"),
    "email": load_trained_model("models/email_model.h5")
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    input_text = data.get("text", "")
    style = data.get("style", "casual")

    if style not in models:
        return jsonify({"error": "Invalid style selected"}), 400

    predictions = predict_next_word(style,models[style], input_text)

    return jsonify({"predictions": predictions})

if __name__ == '__main__':
    app.run(debug=True)
