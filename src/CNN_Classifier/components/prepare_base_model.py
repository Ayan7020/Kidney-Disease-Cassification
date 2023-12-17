import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from dataclasses import dataclass
from pathlib import Path
from CNN_Classifier.enitity.config_entity import PrepareBaseModelConfig


class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config

    def get_base_model(self):
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape=self.config.params_image_size,  
            pooling='max',
            weights=self.config.params_weights,
            include_top=self.config.params_include_top,
            classes=4
        )

        self.save_model(path=self.config.base_model_path, model=self.model)

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)

    @staticmethod
    def _prepare_full_model(model, classes, freeze_all, freeze_till):
        if freeze_all:
            for layer in model.layers:
                model.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                model.trainable = False

        flatten_in = tf.keras.layers.Flatten()(model.output)
        layer = tf.keras.layers.Dense(units=512, activation="relu")(flatten_in)
        norm = tf.keras.layers.BatchNormalization()(layer) 
        drop = tf.keras.layers.Dropout(0.5)(norm) 
         
        prediction = tf.keras.layers.Dense(units=classes, activation="softmax")(drop)

        full_model = tf.keras.models.Model(inputs=model.input, outputs=prediction)

        full_model.compile(
            optimizer=tf.keras.optimizers.Adam(0.0001),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"],
        )

        full_model.summary()
        return full_model

    def update_base_model(self):
        self.full_model = self._prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None, 
        )
        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)
