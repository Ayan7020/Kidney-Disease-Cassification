
from pathlib import Path
from CNN_Classifier.enitity.config_entity import TrainingConfig
import tensorflow as tf  

class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config

    def get_base_model(self):
        self.model = tf.keras.models.load_model(
            self.config.updated_base_model_path
        )
        self.model.summary()

    def train_valid_generator(self):
        datagenerator_kwargs = dict(
            rescale=1.0 / 255.0,
            validation_split=0.1
        )
        self.callback = tf.keras.callbacks.EarlyStopping(
            monitor="val_loss",
            min_delta=0.0001,
            patience=5,
            verbose=1,
            mode="auto",
            baseline=None,
            restore_best_weights=False
        )
 
        self.train_generator = tf.keras.utils.image_dataset_from_directory(
            directory=self.config.training_data,
            image_size=self.config.params_image_size[:-1], 
            validation_split=0.1,
            subset="training",
            seed=123,
            label_mode='categorical'
        )

        self.valid_generator = tf.keras.utils.image_dataset_from_directory(
            directory=self.config.training_data,
            image_size=self.config.params_image_size[:-1], 
            validation_split=0.2,
            subset="validation",
            seed=123,
            label_mode='categorical'
        )

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)

    def train(self):
        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epoch,
            validation_data=self.valid_generator,
            callbacks=self.callback
        )

        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )
