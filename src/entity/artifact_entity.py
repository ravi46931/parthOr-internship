from dataclasses import dataclass

"""MODIFY OR ADD ATTRIBUTES"""

@dataclass
class DataIngestionArtifact:
    data_file_path: str


@dataclass
class DataTransformationArtifact:
    train_transform_file_path: str
    test_transform_file_path: str
    preprocessor_file_path: str


@dataclass
class ModelTrainerArtifact:
    top_models_file_name_path: str
    model_file_path: str
   

@dataclass
class ModelEvaluationArtifact:
    best_model_file_path: str