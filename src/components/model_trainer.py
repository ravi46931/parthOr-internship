import os
import sys
import json
import time
import warnings
from src.logger import logging
from src.exception import CustomException
from src.constants import *
from src.constants.hyperparameter import *
from src.entity.artifact_entity import DataTransformationArtifact, ModelTrainerArtifact
from src.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(
        self,
        data_transformation_artifact: DataTransformationArtifact,
        model_trainer_config: ModelTrainerConfig,
    ):
        self.data_transformation_artifact = data_transformation_artifact
        self.model_trainer_config = model_trainer_config

    def model_trainer(self, cat_df, Y_df):
        try:
            """
            EXAMPLE:

            # Models
            linreg = LinearRegression()
            linreg.fit(cat_df, Y_df)
            """

            """WRITE THE OWN LOGIC FOR MODEL TRAINING"""

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_model_trainer(self):
        try:
            """EXAMPLE: 
            logging.info("Model traing started...")
            df = pd.read_csv(
                self.data_transformation_artifact.train_transform_file_path
            )
            X = df.drop(columns=["expenses", "Unnamed: 0"], axis=1)
            y = df[["expenses"]].squeeze()
            
            df_test = pd.read_csv(
                self.data_transformation_artifact.test_transform_file_path
            )
            # Save the model using pickle
            import pickle

            file_paths = []
            model_names = []
            os.makedirs(
                self.model_trainer_config.MODEL_TRAINER_ARTIFACT_DIR, exist_ok=True
            )
            os.makedirs(self.model_trainer_config.MODELS_DIR_PATH, exist_ok=True)
            for model_name, _ in top_models.items():
                name_model = "".join(model_name.split()).lower()
                file_name = name_model + "_model.pkl"
                file_path = os.path.join(
                    self.model_trainer_config.MODELS_DIR_PATH, file_name
                )
            with open(
                self.model_trainer_config.TOP_MODELS_NAME_FILE_PATH, "w"
            ) as json_file:
                json.dump(model_names, json_file, indent=4)

            model_trainer_artifact = ModelTrainerArtifact(
                self.model_trainer_config.TOP_MODELS_NAME_FILE_PATH, *file_paths
            )

            return model_trainer_artifact
            """

        except Exception as e:
            raise CustomException(e, sys)