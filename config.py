import os
import logging
from dotenv import load_dotenv
from pathlib import Path

# Root Directory
BASE_DIR = Path(__file__).resolve().parent


# Logging Setting
logging.basicConfig(
    filename = 'app.log',
    filemode = 'w',
    format = '%(asctime)s | %(name)s | %(levelname)s | %(message)s',
    datefmt = '%Y-%m-%d %I:%M:%S %p',
    level = logging.INFO,
    encoding = 'utf-8-sig'
)


# Download environment variables from file .env
load_dotenv()


# Extracting primary links
DATABASE_URL = os.getenv('DATABASE_URL')
API_BASE_URL = os.getenv('API_BASE_URL')


# Defining folder paths to standardize usage in the project
DATA_DIR = os.path.join(BASE_DIR, 'data')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')


# Make sure the folders exist (if they don't, the code will create them)
os.makedirs(DATA_DIR, exist_ok = True)
os.makedirs(OUTPUT_DIR, exist_ok = True)
