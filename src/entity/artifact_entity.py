from dataclasses import dataclass


@dataclass
class DataExtractionArtifact:
    data_file_path: str


@dataclass
class ReportGenerationArtifact:
    pdf_report_file_path: str
