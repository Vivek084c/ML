from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import joblib
from nltk.corpus import stopwords
import string

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

# Define the text processing function as used in the Jupyter notebook
def text_process(review):
    nopunc = [char for char in review if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    return ' '.join([word for word in nopunc.split() if word.lower() not in stopwords.words('english')])

# Load the trained model using joblib
model = joblib.load('fake_review_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        print("Request received!")  # Debugging step
        data = request.json  # Get the JSON data
        print(f"Received data: {data}")  # Log incoming data

        review_text = data.get('review_text', '')
        if review_text:
            print(f"Review text: {review_text}")  # Log the review text
            processed_text = text_process(review_text)
            print(f"Processed text: {processed_text}")  # Log the processed text

            # Make the prediction using the loaded model
            prediction = model.predict([processed_text])
            print(f"Prediction: {prediction}")  # Log the prediction

            # Return the result to the frontend
            return jsonify({'prediction': 'Fake' if prediction[0] == 1 else 'Real'})
        else:
            return jsonify({'error': 'No review text provided'}), 400
    except Exception as e:
        print(f"Error occurred: {str(e)}")  # Log the error
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)