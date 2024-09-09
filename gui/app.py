import tkinter as tk
from tkinter import StringVar
from numpy import array
from neural_network import NeuralNetwork  # Import your NeuralNetwork class

# Initialize Neural Network
neural_network = NeuralNetwork()

# Train the neural network with your initial data
training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
training_set_outputs = array([[0, 1, 1, 0]]).T
neural_network.train(training_set_inputs, training_set_outputs, 10000)

# Set up the Tkinter window
root = tk.Tk()
root.title("Neural Network Predictor")

# Input field
input_label = tk.Label(root, text="Enter Inputs (comma-separated, e.g., 1,0,0):")
input_label.pack()
input_entry = tk.Entry(root)
input_entry.pack()

# Result display
result_var = StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.pack()

# Predict function
def predict():
    input_data = input_entry.get()
    input_array = array(list(map(int, input_data.split(',')))).reshape(1, -1)
    prediction = neural_network.think(input_array)
    result_var.set(f"Prediction: {prediction[0]}")

# Predict button
predict_button = tk.Button(root, text="Predict", command=predict)
predict_button.pack()

# Run the Tkinter main loop
root.mainloop()
