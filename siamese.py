"""
    Siamese Network:
        Designed to comare similarities or  differences between pair of inputs.
        Applications: Text similarity, Face Recognition, Signature Verificatoion, and Recommendation Systems
        Network architecture consists of two identical subnetworks that are twins and share the same set of weights and parameters.
        The subnetworks process each input separately and extract their respective feature representations.

"""
from keras.models import Sequential, Model
from keras.layers import Input, Conv2D, MaxPool2D, Flatten, Dense, Lambda
from keras.optimizers import RMSprop
import numpy as np


# Define the Siamese Network architecture
def create_siamese_network(input_shape):
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
    model.add(MaxPool2D(pool_size=(2, 2)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPool2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))

    return model


# Define the Siamese Network function
def siamese_network(input_shape):
    # Create two separate instances of the Siamese Network architecture
    input_a = Input(shape=input_shape)
    input_b = Input(shape=input_shape)
    siamese_network = create_siamese_network(input_shape)

    # Generate the encoded features for each input
    encoded_a = siamese_network(input_a)
    encoded_b = siamese_network(input_b)

    # Compute the Euclidean distance between the encoded features
    distance = Lambda(lambda x: np.sqrt(np.sum((x[0] - x[1])**2, axis=1)), output_shape=(1,))([encoded_a, encoded_b])

    # Define the Siamese model with two inputs and the computed distance as output
    model = Model(inputs=[input_a, input_b], outputs=distance)

    return model


# Set the input shape of the images
input_shape = (28, 28, 1)

# Create the Siamese Network
siamese_model = siamese_network(input_shape)

# Compile the model
siamese_model.compile(loss='binary_crossentropy', optimizer=RMSprop(), metrics=['accuracy'])

# Print the summary of the model
siamese_model.summary()
