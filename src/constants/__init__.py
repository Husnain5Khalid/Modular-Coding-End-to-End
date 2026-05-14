import os, sys
from datetime import datetime

# Artifacts -> pipeline folder -> timestamp -> output

#now we created the time related function it means when we run piple line it record all details

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"

CURRENT_TIME_STAMP = get_current_time_stamp()

# below three lines show how to get data from local
#Modular-Coding-End-to-End/DATA_DIR/DATA_DIR_KEY
ROOT_DIR_KEY = os.getcwd() #means current directory Modular-coding-end-to-end
DATA_DIR = "Data"
DATA_DIR_KEY = "finalTrain.csv"

#now we created the Artifacts Folder our all ML pipeline folder are present there
ARTIFACT_DIR_KEY = "Artifact"

# Data Ingestion related variable
DATA_INGESTION_KEY = "data_ingestion" #data ingestion folder created
DATA_INGESTION_RAW_DATA_DIR = "raw_data_dir" #when we download data it is raw data so we created raw data folder
DATA_INGESTION_INGESTED_DATA_DIR_KEY = "ingested_dir"  # we split data into train and test split
RAW_DATA_DIR_KEY = "raw.csv"
TRAIN_DATA_DIR_KEY = "train.csv"
TEST_DATA_DIR_KEY = "test.csv"

# Data Transformation Related Variable
# Artifact / Data_transformation / processor->processor.pkl / transformation -> train.csv and test.csv

DATA_TRANSFORMATION_ARTIFACT = "data_transformation"
DATA_PREPROCESSED_DIR = "processor"
DATA_TRANSFORMATION_PROCESSING_OBJ = "processor.pkl"
DATA_TRANSFORMATION_DIR = "transformation"
TRANSFORM_TRAIN_DIR_KEY = "train.csv"
TRANSFORM_TEST_DIR_KEY = "test.csv"



