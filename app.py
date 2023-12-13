# Import necessary libraries
from flask import Flask, request, jsonify
import joblib

# Create Flask app
app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('attrition_forest_model.pkl')

# Define the route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the POST request
        data = request.get_json()

        # Perform predictions using the loaded model
        predictions = model.predict(data['input_data'])

        # Return the predictions as JSON
        return jsonify({'predictions': predictions.tolist()})
    except Exception as e:
        # Return an error message if something goes wrong
        return jsonify({'Error! Something went wrong': str(e)})

# Define a simple welcome route
@app.route('/')
def welcome():
    return 'Welcome to the Model Deployment API!'

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
