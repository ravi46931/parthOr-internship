import sys
from src.exception import CustomException
from src.logger import logging
from src.components.data_extraction import DataExtraction
from src.components.report_generation import ReportGeneration

from src.entity.artifact_entity import (
    DataExtractionArtifact,
    ReportGenerationArtifact
)
from src.entity.config_entity import (
    DataExtractionConfig,
    ReportGenerationConfig
)


class ExecutePipeline:
    def __init__(self):
        self.data_extraction_config = DataExtractionConfig()
        self.report_generation_config = ReportGenerationConfig()

    def start_data_extraction(self) -> DataExtractionArtifact:
        try:
            

            logging.info("Starting data extraction from execute pipeline..")
            dataextraction = DataExtraction(self.data_extraction_config)
            data_extraction_artifact = dataextraction.initiate_data_extraction()
            logging.info("Data extraction completed in execute pipeline..")
            return data_extraction_artifact            
            
        except Exception as e:
            raise CustomException(e, sys)

    def start_report_generation(
        self, data_extraction_artifact: DataExtractionArtifact
    ) -> ReportGenerationArtifact:
        try:
            
            logging.info("Starting report generation from execute pipeline..")
            report_generation = ReportGeneration(
                data_extraction_artifact, self.report_generation_config
            )
            report_generation_artifact = (
                report_generation.initiate_report_generation()
            )
            logging.info("report generation completed in execute pipeline..")
            return report_generation_artifact
        

        except Exception as e:
            raise CustomException(e, sys)
    
    def run_pipeline(self):
        try:
            logging.info("Running execute pipeline...")
            data_extraction_artifact = self.start_data_extraction()
            report_generation_artifact = self.start_report_generation(
                data_extraction_artifact
            )
           
            logging.info("Pipeline executed successfully..")
        except Exception as e:
            raise CustomException(e, sys)