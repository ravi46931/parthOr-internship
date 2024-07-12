import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.constants.hyperparameter import *
from src.constants import *
from src.entity.artifact_entity import (
    DataTransformationArtifact,
    ModelTrainerArtifact,
    ModelEvaluationArtifact,
)
from src.entity.config_entity import ModelTrainerConfig, ModelEvaluationConfig

class ModelEvaluation:
    def __init__(
        self,
        data_transformation_artifact: DataTransformationArtifact,
        model_trainer_artifact: ModelTrainerArtifact,
        model_evaluation_config: ModelEvaluationConfig,
    ):
        self.data_transformation_artifact = data_transformation_artifact
        self.model_trainer_artifact = model_trainer_artifact
        self.model_evaluation_config = model_evaluation_config

    def model_evaluation(self, model_names, models):
        try:
            
           """WRITE THE CODE FOR MODEL EVALUATION"""

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_model_evaluation(self):
        try:
            """EXAMPLE:
            
            df = pd.read_csv(
                self.data_transformation_artifact.train_transform_file_path
            )
            X = df.drop(columns=["expenses", "Unnamed: 0"], axis=1)
            y = df[["expenses"]].squeeze()

            with open(
                self.model_trainer_artifact.top_models_file_name_path, "r"
            ) as json_file:
                model_names = json.load(json_file)

            with open(self.model_trainer_artifact.model1_file_path, "rb") as f:
                model1 = pickle.load(f)           
           
            # Saving the test set metrics
            with open(
                self.model_evaluation_config.TEST_METRICS_FILE_PATH, "w"
            ) as json_file:
                json.dump(test_metrics, json_file, indent=4)

            # Saving the best model
            with open(self.model_evaluation_config.BEST_MODEL_FILE_PATH, "wb") as file:
                pickle.dump(best_model, file)

            # Saving the best model to root
            os.makedirs("models", exist_ok=True)
            with open("models/best_model.pkl", "wb") as file:
                pickle.dump(best_model, file) 

            model_evaluation_artifact = ModelEvaluationArtifact(
                self.model_evaluation_config.BEST_MODEL_FILE_PATH
            )

            return model_evaluation_artifact
            """

            """WRITE THE CODE FOR INITIATING MODEL EVALUATION"""

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    pass