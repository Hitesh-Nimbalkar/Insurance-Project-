from Insurance_Project.logger import logging
from Insurance_Project.exception import InsuranceException
from Insurance_Project.utils import get_collection_as_dataframe
import sys, os
from Insurance_Project.entity.config_entity import DataIngestionConfig
from Insurance_Project.entity import config_entity
from Insurance_Project.components.data_ingestion import DataIngestion



if __name__=="__main__":
     try:
          #start_training_pipeline()
          #test_logger_and_expection()
       # get_collection_as_dataframe(database_name ="INSURANCE", collection_name = 'INSURANCE_PROJECT')
       training_pipeline_config = config_entity.TrainingPipelineConfig()
       
      #data ingestion
       data_ingestion_config  = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
       print(data_ingestion_config.to_dict())
       data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
       data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

      
     except Exception as e:
          print(e)