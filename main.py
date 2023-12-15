from CNN_Classifier import logger
from CNN_Classifier.pipeline.stage01 import DataIngestionTrainingPipeline


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
