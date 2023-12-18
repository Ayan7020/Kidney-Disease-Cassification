from CNN_Classifier import logger

from CNN_Classifier.pipeline.stage01 import DataIngestionTrainingPipeline
from CNN_Classifier.pipeline.stage02 import PrepareBaseModelPipeline
from CNN_Classifier.pipeline.stage03 import Modeltraining
from CNN_Classifier.pipeline.stage04 import ModelEvaluating


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> Stage {STAGE_NAME} Started <<<<<<<")
    logger.info(f">>>>Stage {STAGE_NAME} started <<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>Stage {STAGE_NAME} Completed <<<<\n\nx===============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare Base model"

try:
    logger.info(f"*" * 10)
    logger.info(f">>>>>> stage {STAGE_NAME} Started <<<<<<")
    obj = PrepareBaseModelPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} Completed <<<<<<<\n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training"

try:
    logger.info(f"*" * 10)
    logger.info(f">>>>>> stage {STAGE_NAME} Started <<<<<<")
    obj = Modeltraining()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} Completed <<<<<<<\n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluating"

try:
    logger.info(f"*" * 10)
    logger.info(f">>>>>> stage {STAGE_NAME} Started <<<<<<")
    obj = ModelEvaluating()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} Completed <<<<<<<\n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e
