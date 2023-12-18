from CNN_Classifier.config.configuration import ConfigurationManager
from CNN_Classifier.components.model_eval_mlflow import Evaluation
from CNN_Classifier import logger


STAGE_NAME = "Model Evaluating" 

class ModelEvaluating:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.log_in_to_mlflow()
        
if __name__ == "__main__":
    try:
        logger.info(f"*" * 10)
        logger.info(f">>>>>> stage {STAGE_NAME} Started <<<<<<")
        obj = ModelEvaluating()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} Completed <<<<<<<\n\nx=============x")
    except Exception as e:
        logger.exception(e)
        raise e
        