import os
import sys
from src.logger import logging
from src.exception import CustomException
from src.entity.config_entity import DataTransformationConfig
from src.utils.utils import label_encode_column, encode_region_column, get_feature_names
from src.entity.artifact_entity import DataIngestionArtifact, DataTransformationArtifact


class DataTransformation:
    def __init__(
        self,
        data_ingestion_artifact: DataIngestionArtifact,
        data_transformation_config: DataTransformationConfig,
    ):
        self.data_ingestion_artifact = data_ingestion_artifact
        self.data_transformation_config = data_transformation_config

    def transform_data(self, df):
        try:
           """WRITE THE CODE FOR TRANSFORMING THE DATA"""
           """RETURNS
                - trandformed data
                - preprocessor object
           """

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self) -> DataTransformationArtifact:
        try:

            """
            EXAMPLE: 

            logging.info("Data transformation initiated...")
            df = pd.read_csv(self.data_ingestion_artifact.data_file_path)
            train_df, test_df, preprocessor = self.transform_data(df)
            os.makedirs(
                self.data_transformation_config.DATA_TRANSFORMATION_ARTIFACT_DIR,
                exist_ok=True,
            )
            # Saving transform dataframe
            train_df.to_csv(self.data_transformation_config.TRAIN_TRANSFORM_FILE_PATH)
            test_df.to_csv(self.data_transformation_config.TEST_TRANSFORM_FILE_PATH)
            # Saving preprocessor object
            joblib.dump(
                preprocessor, self.data_transformation_config.PREPROCESSOR_FILE_PATH
            )
            os.makedirs("models", exist_ok=True)
            preprocessor_path = "models/" + PREPROCESSOR_FILE_NAME
            joblib.dump(preprocessor, preprocessor_path)

            data_transformation_artifact = DataTransformationArtifact(
                self.data_transformation_config.TRAIN_TRANSFORM_FILE_PATH,
                self.data_transformation_config.TEST_TRANSFORM_FILE_PATH,
                self.data_transformation_config.PREPROCESSOR_FILE_PATH,
            )

            logging.info("Data Transformation completed...")
            return data_transformation_artifact
            """

            """WRITE YOUR OWN LOGIC OF CODE"""

        except Exception as e:
            raise CustomException(e, sys)




