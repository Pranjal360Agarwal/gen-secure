import tensorflow as tf
from sklearn.model_selection import train_test_split
from metrics import evaluate_model
from logger import log_event
import numpy as np

def train_model(data, labels):
    log_event("Starting model training...")
    
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
    
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=10, batch_size=32)
    
    log_event("Model training complete.")
    evaluate_model(model, X_test, y_test)
    return model
