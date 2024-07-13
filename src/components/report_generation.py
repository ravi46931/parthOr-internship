import os
import sys
import math
import json
from src.logger import logging
from reportlab.lib import colors
from reportlab.lib.units import inch
from src.exception import CustomException
from reportlab.lib.pagesizes import letter
from src.entity.config_entity import ReportGenerationConfig
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from src.entity.artifact_entity import DataExtractionArtifact, ReportGenerationArtifact
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer


class ReportGeneration:
    def __init__(
        self,
        data_extraction_artifact: DataExtractionArtifact,
        report_generation_config: ReportGenerationConfig,
    ):
        self.data_extraction_artifact = data_extraction_artifact
        self.report_generation_config = report_generation_config

    def generate_report(self, data):
        try:
           # Extract dictionary and list from data
            summary_dict = data[0]
            orders_list = data[1]
            
            pdf = SimpleDocTemplate(self.report_generation_config.PDF_FILEPATH, pagesize=letter, rightMargin=inch*0.5, leftMargin=inch*0.5, topMargin=inch*0.75, bottomMargin=inch*0.75)
            # Define styles
            styles = getSampleStyleSheet()
            title_style = styles['Title']
            subtitle_style = styles['Heading2']
            normal_style = styles['BodyText']
            small_normal_style = ParagraphStyle(name='SmallNormal', fontSize=10, parent=normal_style)

            # Create story list for the PDF
            story = []

            # Title and Subtitle
            story.append(Paragraph('Daily Sales Report', title_style))
            story.append(Spacer(1, 12))

            # Summary Section
            summary_data = list(summary_dict.items())
            summary_table = Table(summary_data, colWidths=[200, 300])
            summary_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.beige),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]))

            order_date = summary_dict['Order Date']
            formatted_date = f"Date: {order_date}"

            # Add order date as text
            story.append(Paragraph(formatted_date, subtitle_style))
            story.append(Spacer(1, 6))

            story.append(Paragraph("Summary", subtitle_style))
            story.append(summary_table)
            story.append(Spacer(1, 12))


            # Orders Section
            if orders_list:
                for index, order in enumerate(orders_list):
                    
                    # headers = ["Key", "Value"]
                    order_data = []
                    
                    for key, value in order.items():
                        # Convert NaN to empty string for display
                        if isinstance(value, float) and math.isnan(value):
                            value = ''
                        order_data.append([key, value])
                    
                    # Add a blank line between orders
                    if index > 0:
                        story.append(Spacer(1, 12))
                    
                    # Create and style table for each order
                    # order_table = Table([headers] + order_data, colWidths=[200, 300])
                    order_table = Table(order_data, colWidths=[200, 300])
                    order_table.setStyle(TableStyle([
                        ('BACKGROUND', (0, 0), (-1, 0), colors.white),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black),
                        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
                        ('FONTSIZE', (0, 0), (-1, -1), 10),
                    ]))
                    
                    # Add order details to the story
                    story.append(Paragraph(f"Order {index + 1}", subtitle_style))
                    story.append(order_table)
                    story.append(Spacer(1, 12))

            # Build the PDF
            pdf.build(story)

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_report_generation(self) -> ReportGenerationArtifact:
        try:
            with open(self.data_extraction_artifact.data_file_path, 'r') as file:
                data = json.load(file)

            os.makedirs(
                self.report_generation_config.REPORT_GENERATION_ARTIFACT_DIR,
                exist_ok=True,
            )

            self.generate_report(data)

            report_generation_artifact = ReportGenerationArtifact(
                pdf_report_file_path=self.report_generation_config.PDF_FILEPATH
            )

            return report_generation_artifact
            
        except Exception as e:
            raise CustomException(e, sys)
