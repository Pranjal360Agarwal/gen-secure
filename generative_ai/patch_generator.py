import tensorflow as tf
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.models import Model

def build_gan():
    # Generator model
    generator_input = Input(shape=(100,))
    x = Dense(256, activation='relu')(generator_input)
    generated_patch = Dense(1024, activation='sigmoid')(x)
    generator = Model(generator_input, generated_patch)

    # Discriminator model
    discriminator_input = Input(shape=(1024,))
    x = Dense(256, activation='relu')(discriminator_input)
    validity = Dense(1, activation='sigmoid')(x)
    discriminator = Model(discriminator_input, validity)

    return generator, discriminator
