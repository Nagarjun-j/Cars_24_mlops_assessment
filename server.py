from flask import Flask, request, jsonify
import cv2
import numpy as np
import tensorflow as tf

app = Flask(__name__)
model = tf.keras.models.load_model("mnist_model.h5")

@app.route('/')
def index():
    return 'Flask server is running!'

@app.route('/predict', methods=['POST'])
def predict():
    # Get image data from request
    image_data = request.files['image']
    # Read the image
    image = cv2.imdecode(np.fromstring(image_data.read(), np.uint8), cv2.IMREAD_GRAYSCALE)
    
    # Preprocess the image
    resized_image = cv2.resize(image, (28, 28))
    inverted_image = cv2.bitwise_not(resized_image)
    normalized_image = inverted_image / 255.0
    input_image = normalized_image.reshape(1, 28, 28, 1)

    # Perform prediction
    prediction = model.predict(input_image)
    predicted_digit = np.argmax(prediction)

    # Return prediction as JSON response
    return jsonify({'predicted_digit': str(predicted_digit)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
