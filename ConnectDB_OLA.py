#Phase 2: OLA Cleaned Data - Data Loading to MySql 

#  importing libraries
import warnings
warnings.filterwarnings('ignore')

from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import urllib.parse
import gdown

from tabulate import tabulate

import pandas as pd
import mysql.connector

# Database credentials 
DB_USER = "root"
DB_PASSWORD = "MySQL@1234"
DB_HOST = "localhost"       # or IP address
DB_PORT = 3306              # default MySQL port
DB_NAME = "OlaDB"


#Connecting to MySQL

connection = mysql.connector.connect(host="localhost",user="root",password=DB_PASSWORD)

#Creating cursor object
cursor = connection.cursor()


# Create Database

query = ("CREATE DATABASE IF NOT EXISTS OlaDB;")
cursor.execute(query)


# Safely encode password in case it contains special characters
encoded_password = urllib.parse.quote_plus(DB_PASSWORD)

# Create the connection URL
connection_url = f"mysql+mysqlconnector://{DB_USER}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create the SQLAlchemy engine
engine = create_engine(connection_url, echo=True, pool_pre_ping=True)

# Test the connection
with engine.connect() as conn:
    result = conn.execute(text("SELECT VERSION()"))
    version = result.scalar()
    print(f"Connected to MySQL Server version: {version}")



# Importing from Google Drive - OLA Cleaned Data csv file 


download_url = 'https://drive.google.com/file/d/1AJZubf6AZY86bsMtbgH88RoVZHkPAz0H/view?usp=sharing'
# Temporary File name

output_file = "Ola_CleanedDS.csv"

# 3. Read the CSV straight into a pandas DataFrame
try:

    # gdown automatically handles large files and virus scan prompts
    gdown.download(download_url, output_file, quiet=False)

    df = pd.read_csv(output_file)
    print("Success! Here is the data:")
  
except Exception as e:
    print(f"Error downloading file: {e}")


#Transferring Data From CSV to MySQL Table
df.to_sql(name="OlaRides",con=engine,if_exists='replace',chunksize=5000,method="multi",index=False)
