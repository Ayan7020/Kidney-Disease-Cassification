import tensorflow as tf
from pathlib import Path
from CNN_Classifier.enitity.config_entity import EvaluationConfig
from CNN_Classifier.utils.common import save_json
import mlflow
import mlflow.keras
from urllib.parse import urlparse

class Evaluation:
    def __init__(self,config: EvaluationConfig):
        self.config = config
        
        
    def _valid_generator(self):
        
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
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)  
    
    
    def evaluation(self):
        self.model = self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.score = self.model.evaluate(self.valid_generator)
        self.save_score()  
        
    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=Path("scores.json"), data=scores)
    
    
    def log_in_to_mlflow(self):
        mlflow.set_registry_uri(self.config.mlflow_url)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        
        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(
                {"loss":self.score[0],"accuracy":self.score[1]}
            )
            # Model registry does not work with file store
            if tracking_url_type_store != "file":
                mlflow.keras.log_model(self.model, "model", registered_model_name="VGG16Model")
            else:
                mlflow.keras.log_model(self.model, "model")     
        
        