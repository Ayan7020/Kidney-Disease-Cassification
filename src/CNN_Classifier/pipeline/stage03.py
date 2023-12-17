from CNN_Classifier.config.configuration import ConfigurationManager
from CNN_Classifier.components.model_training import Training
from CNN_Classifier import logger

STAGE_NAME = "Model Training"


class Modeltraining:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_path()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()


if __name__ == "__main__":
    try:
        logger.info(f"*" * 10)
        logger.info(f">>>>>> stage {STAGE_NAME} Started <<<<<<")
        obj = Modeltraining()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} Completed <<<<<<<\n\nx=============x")
    except Exception as e:
        logger.exception(e)
        raise e
