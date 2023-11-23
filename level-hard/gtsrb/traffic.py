import cv2
import numpy as np
import os
import sys
import tensorflow as tf
from sklearn.model_selection import train_test_split
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import torch
from PIL import Image

from sklearn.model_selection import train_test_split

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Get image arrays and labels for all image files
    images, labels = load_data(sys.argv[1])
    print("Images Loaded")

    # Split data into training and testing sets
    labels = tf.keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )

    # Get a compiled neural network
    model,criterion, optimizer = get_model()
    print("MODEL LOADED")

    # Fit model on training data
    train_dataset = TensorDataset(torch.Tensor(x_train), torch.LongTensor(y_train))
    test_dataset = TensorDataset(torch.Tensor(x_test), torch.LongTensor(y_test))
    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)
    
    fit(model, criterion, optimizer, train_loader, epochs=EPOCHS)
    print("TRAINING COMPLTETE..")

    # Evaluate neural network performance
    average_loss, accuracy = evaluate(model, criterion, test_loader)
    print("EVALUATION COMPLETE..")
    print(average_loss)
    print(accuracy)

    # Save model to file
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        model.save(filename)
        print(f"Model saved to {filename}.")


def load_data(data_dir):
    """
    Load image data from directory `data_dir`.

    Assume `data_dir` has one directory named after each category, numbered
    0 through NUM_CATEGORIES - 1. Inside each category directory will be some
    number of image files.

    Return tuple `(images, labels)`. `images` should be a list of all
    of the images in the data directory, where each image is formatted as a
    numpy ndarray with dimensions IMG_WIDTH x IMG_HEIGHT x 3. `labels` should
    be a list of integer labels, representing the categories for each of the
    corresponding `images`.
    """
    # Initialize empty lists to store images and labels
    images = []
    labels = []
    # Iterate through each category directory
    print("Loading Data")
    c = 0
    for category in os.listdir(data_dir):
        if(c%20==0):
          print(c)
        c = c+1
        category_path = os.path.join(data_dir, category)

        # Check if it's a directory
        if os.path.isdir(category_path):
            # Get the category label (assuming directories are named 0 through NUM_CATEGORIES - 1)
            label = int(category)

            # Iterate through each image file in the category directory
            for filename in os.listdir(category_path):
                # Get the full path of the image file
                image_path = os.path.join(category_path, filename)

                # Open the image using PIL
                image = Image.open(image_path)
                image = image.convert("RGB")

                # Resize the image if needed (replace IMG_WIDTH and IMG_HEIGHT with your desired dimensions)
                image = image.resize((IMG_WIDTH, IMG_HEIGHT))

                # Convert the image to a numpy array
                image_array = np.array(image)
                #print(image_array.shape)

                # Append the image and label to the lists
                images.append(image_array)
                labels.append(label)

    # Convert lists to numpy arrays
    images = np.array(images)
    labels = np.array(labels)

    return images, labels

class SimpleCNN(nn.Module):
    def __init__(self, num_categories):
        super(SimpleCNN, self).__init__()

        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.relu1 = nn.ReLU()
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)

        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.relu2 = nn.ReLU()
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)

        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        self.relu3 = nn.ReLU()
        self.pool3 = nn.MaxPool2d(kernel_size=2, stride=2)

        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(128 * (IMG_WIDTH // 8) * (IMG_HEIGHT // 8), 512)
        self.relu4 = nn.ReLU()
        self.fc2 = nn.Linear(512, num_categories)

    def forward(self, x):
        x = self.pool1(self.relu1(self.conv1(x)))
        x = self.pool2(self.relu2(self.conv2(x)))
        x = self.pool3(self.relu3(self.conv3(x)))
        x = self.flatten(x)
        x = self.relu4(self.fc1(x))
        x = self.fc2(x)
        return x

def get_model():
    """
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """
    model = SimpleCNN(num_categories=NUM_CATEGORIES)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    return model, criterion, optimizer


def fit(model, criterion, optimizer, train_loader, epochs=5):
    model.train()
    for epoch in range(epochs):
        print("EPOCH:",epoch)
        for inputs, targets in train_loader:
            inputs = inputs.permute(0, 3, 1, 2)
            #print(inputs.shape)
            optimizer.zero_grad()
            outputs = model(inputs)
            targets = torch.argmax(targets, dim=1)
            loss = criterion(outputs, targets)
            loss.backward()
            optimizer.step()
        print(loss)

def evaluate(model, criterion, test_loader):
    model.eval()
    total_loss = 0.0
    correct = 0
    total = 0

    with torch.no_grad():
        for inputs, targets in test_loader:
            inputs = inputs.permute(0, 3, 1, 2)
            outputs = model(inputs)
            targets = torch.argmax(targets, dim=1)
            loss = criterion(outputs, targets)
            total_loss += loss.item()

            _, predicted = outputs.max(1)
            total += targets.size(0)
            correct += predicted.eq(targets).sum().item()

    average_loss = total_loss / len(test_loader)
    accuracy = correct / total

    return average_loss, accuracy



if __name__ == "__main__":
    main()
