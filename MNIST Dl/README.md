# MNIST Handwritten Digit Classification

This project implements a Deep Learning model to classify handwritten digits from the famous MNIST dataset.

## Project Overview
The MNIST dataset consists of 60,000 training images and 10,000 testing images of handwritten digits (0-9). Each image is 28x28 pixels in grayscale.

## Implementation Details
- **Framework**: TensorFlow/Keras
- **Model Architecture**:
  - Flatten layer (28x28 input)
  - Dense layer (128 units, ReLU activation)
  - Dense layer (32 units, ReLU activation)
  - Output Dense layer (10 units, Softmax activation)
- **Optimizer**: Adam
- **Loss Function**: Sparse Categorical Crossentropy

## Performance
The model achieves an accuracy of approximately **97.8%** on the test dataset.

## How to Run
1. Open `predict.ipynb` in a Jupyter Notebook environment.
2. Run the cells to train the model and see predictions.
