from flask import Flask, render_template, request
from numpy import array
from neural_network import NeuralNetwork  # Import your NeuralNetwork class

app = Flask(__name__)
neural_network = NeuralNetwork()

# Train the neural network with your initial data
training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
training_set_outputs = array([[0, 1, 1, 0]]).T
neural_network.train(training_set_inputs, training_set_outputs, 10000)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    input_data = request.form.get('input_data')
    input_array = array(list(map(int, input_data.split(',')))).reshape(1, -1)
    prediction = neural_network.think(input_array)
    return render_template('index.html', prediction=prediction[0])

if __name__ == "__main__":
    app.run(debug=True)
