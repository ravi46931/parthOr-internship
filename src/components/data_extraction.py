import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
import json
from src.entity.artifact_entity import DataExtractionArtifact
from src.entity.config_entity import DataExtractionConfig
from pathlib import Path
from src.constants import DATA_PATH, EXTRACT_DATA_FILE_NAME


class DataExtraction:
    def __init__(self, data_extraction_config: DataExtractionConfig) -> None:
        self.data_extraction_config = data_extraction_config

    def fetch_dataset(self, filepath: str = None)->pd.DataFrame:
        try:
            if filepath is None:
                msg = "Filepath is not provided to 'fetch_dataset' function"
                raise Exception(msg)
            
            filepath = Path(filepath)
            extension = filepath.suffix[1:]

            if extension == "xlsx":
                df = pd.read_excel(filepath)
            elif extension == "csv":
                df = pd.read_csv(filepath)
            return df

        except Exception as e:
            raise CustomException(e, sys)

    def single_day_data(self, df, date):
        try:
            try:
                one_day_data = df[df['ORDERDATE'] == date]
            except:
                format = "2003-02-24"
                msg = f"Either there is no entry for orderdate or date is not in correct format. e.g. {format}"
                raise Exception(msg)
            
            total_order_quantity = one_day_data['QUANTITYORDERED'].sum().item()
            total_sales = one_day_data['SALES'].sum().item()
            order_date = one_day_data['ORDERDATE'].unique()[0]
            order_date = str(order_date.date())
            total = {
                'Total Order Quantity': total_order_quantity,
                'Total Sales': total_sales,
                'Order Date': order_date
            }
            
            rows = one_day_data.shape[0]
            
            onedaylist = []
            for i in range(rows):
                onedayitem = one_day_data.iloc[i]
                onedaylist.append({
                    'Order Number': onedayitem['ORDERNUMBER'].item(),
                    'Quantity Ordered': onedayitem['QUANTITYORDERED'].item(),
                    'Price Each Item': onedayitem['PRICEEACH'].item(),
                    'Order Line Number': onedayitem['ORDERLINENUMBER'].item(),
                    'Sales': onedayitem['SALES'].item(),
                    'Status': onedayitem['STATUS'],
                    'Qtr ID': onedayitem['QTR_ID'].item(),
                    'Productline': onedayitem['PRODUCTLINE'],
                    'MSRP': onedayitem['MSRP'].item(),
                    'Product Code': onedayitem['PRODUCTCODE'],
                    'Customer Name': onedayitem['CUSTOMERNAME'],
                    'Address': onedayitem['ADDRESSLINE1'],
                    'City': onedayitem['CITY'],
                    'State': onedayitem['STATE'],
                    'Country': onedayitem['COUNTRY'],
                    'Postal Code': onedayitem['POSTALCODE'],
                    'Deal Size': onedayitem['DEALSIZE'],
                })
           
            return total, onedaylist
    
        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_extraction(self) -> DataExtractionArtifact:
        try:
            df = self.fetch_dataset(DATA_PATH)
            dates = df['ORDERDATE'].unique()
            sorted_dates = sorted(list(dates))
            """For a single day report change idx, dates are in soted order"""
            idx = 5 # change index to change the date
            date = str(sorted_dates[idx]).split(" ")[0]

            total, onedaylist = self.single_day_data(df, date)
            os.makedirs(
                self.data_extraction_config.DATA_EXTRACTION_ARTIFACT_DIR, exist_ok=True
            )
            with open(self.data_extraction_config.EXTRACT_DATA_FILE_PATH, 'w') as file:
                json.dump((total, onedaylist), file)

            data_extraction_artifact = DataExtractionArtifact(
                data_file_path=self.data_extraction_config.EXTRACT_DATA_FILE_PATH
            )

            return data_extraction_artifact
            
        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    dataextraction = DataExtraction(DataExtractionConfig())
    data_extraction_artifact = dataextraction.initiate_data_extraction()
    print(data_extraction_artifact)