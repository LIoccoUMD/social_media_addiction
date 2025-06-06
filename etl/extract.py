import kaggle
import logging

logging.basicConfig(filename='log/extract.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Starting Kaggle dataset extraction.")

try:
# Download latest version
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files("adilshamim8\\social-media-addiction-vs-relationships", path="data\\extracted", unzip=True)
    logging.info("Dataset downloaded and extracted successfully.")
    kaggle.api.dataset_metadata("adilshamim8\\social-media-addiction-vs-relationships", path="data\\extracted")
    logging.info("Dataset metadata downloaded successfully.")
    
except Exception as e:
    logging.error(f"Problem with loading the dataset. Please try again.")