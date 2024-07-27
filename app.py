from flask import Flask, request, jsonify, render_template
import joblib
import os

app = Flask(__name__)
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
vectorizer_path = os.path.join(os.path.dirname(__file__), 'vectorizer.pkl')

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if not data or 'symptom' not in data:
            return jsonify({'error': 'No symptom provided'}), 400
        
        symptoms = data['symptom']
        print(f"Received symptoms: {symptoms}")
        symptoms_tfidf = vectorizer.transform([symptoms])
        prediction = model.predict(symptoms_tfidf)[0]
        
        disease = map_prediction_to_disease(prediction)
        print("HELLOOOO")
        
        return jsonify({'disease': disease})
    
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({'error': 'An error occurred during prediction'}), 500

def map_prediction_to_disease(prediction):
    print(prediction)

    
    return prediction

if __name__ == '__main__':
    app.run(debug=True)
