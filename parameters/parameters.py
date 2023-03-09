import os

FILE_NAME = "telco_customer_data.csv"
DATA_FOLDER = "data"

main_path = os.getcwd()

file_path = os.path.join(os.path.join(main_path, DATA_FOLDER), FILE_NAME)