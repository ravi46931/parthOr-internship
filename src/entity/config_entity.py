import os
from src.constants import *
from dataclasses import dataclass


@dataclass
class DataExtractionConfig:
    DATA_EXTRACTION_ARTIFACT_DIR = os.path.join(
        ARTIFACT_DIR, DATA_EXTRACTION_ARTIFACT_DIR
    )
    EXTRACT_DATA_FILE_PATH = os.path.join(DATA_EXTRACTION_ARTIFACT_DIR, EXTRACT_DATA_FILE_NAME)


@dataclass
class ReportGenerationConfig:
    REPORT_GENERATION_ARTIFACT_DIR = os.path.join(
        ARTIFACT_DIR, REPORT_GENERATION_ARTIFACT_DIR
    )
    PDF_FILEPATH = os.path.join(
        REPORT_GENERATION_ARTIFACT_DIR, PDF_FILENAME
    )
    
