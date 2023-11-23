# SimpleCNN Documentation

## Overview

The `SimpleCNN` model is a Convolutional Neural Network (CNN) designed for image classification tasks. It consists of three convolutional layers followed by max-pooling layers and two fully connected layers. The model is suitable for scenarios where a simple yet effective image classification architecture is required.

## Architecture

### Convolutional Layers
1. `conv1`: First convolutional layer with 32 filters, kernel size 3x3, and ReLU activation.
2. `pool1`: Max pooling layer with kernel size 2x2.

3. `conv2`: Second convolutional layer with 64 filters, kernel size 3x3, and ReLU activation.
4. `pool2`: Max pooling layer with kernel size 2x2.

5. `conv3`: Third convolutional layer with 128 filters, kernel size 3x3, and ReLU activation.
6. `pool3`: Max pooling layer with kernel size 2x2.

### Fully Connected Layers
7. `flatten`: Flatten layer to transition from convolutional layers to fully connected layers.
8. `fc1`: First fully connected layer with 512 units and ReLU activation.
9. `fc2`: Output layer with `NUM_CATEGORIES` units (number of output categories).


### parameters
- `optimizer` : Adam Optimizer
- `learning rate` : 0.001
- `EPOCHS` : 10
- `Test size` " 0.4


#### Results
- `Accuracy`: 0.9628517823639775

