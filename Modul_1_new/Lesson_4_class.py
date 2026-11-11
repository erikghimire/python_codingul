import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras import layers

# 1. Load the data: 70,000 pictures (28x28 pixels) of handwritten digits 0-9
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0  # pixels 0-255 -> 0.0-1.0

# 2. Build the model: picture in -> 10 scores out (one per digit)
model = tf.keras.Sequential([
    layers.Input(shape=(28, 28)),
    layers.Flatten(),                        # 28x28 grid -> list of 784 numbers
    layers.Dense(128, activation="relu"),    # hidden layer: learns patterns
    layers.Dense(10, activation="softmax"),  # output: probability of each digit
])
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# 3. Train, then test on pictures the model has never seen
model.fit(x_train, y_train, epochs=5)
loss, accuracy = model.evaluate(x_test, y_test)
print(f"Test accuracy: {accuracy:.2%}")

# 4. Show one test picture with the model's guess
guess = model.predict(x_test[:1]).argmax()
plt.imshow(x_test[0], cmap="binary")
plt.title(f"Predicted: {guess}")
plt.show()
