# Dogs vs Cats Image Classification

A Deep Learning project to classify images of dogs and cats using Convolutional Neural Networks (CNN).

## Overview
This project builds a binary classifier that can distinguish between images of dogs and cats. It utilizes a CNN architecture with multiple layers of convolution, pooling, and dropout to achieve high classification accuracy.

## Workflow
1. **Data Loading**: Uses `keras.utils.image_dataset_from_directory` to load images.
2. **Preprocessing**: Normalizes pixel values and resizes images to 256x256.
3. **Model Architecture**:
   - 3 Convolutional layers with Batch Normalization.
   - Max Pooling layers for downsampling.
   - Dense layers with ReLU activation.
   - Final Sigmoid layer for binary classification.
4. **Training**: Trained using the Adam optimizer and Binary Crossentropy loss.

## Technologies Used
- **Python**
- **TensorFlow / Keras** (Deep Learning)
- **OpenCV** (Image Processing)
- **Matplotlib** (Visualization)

## Results
The model's performance is visualized through training and validation accuracy/loss plots provided in the notebook.

## Usage
Open the `DogsvsCats.ipynb` notebook in Jupyter or Google Colab and run all cells to train and test the model.
