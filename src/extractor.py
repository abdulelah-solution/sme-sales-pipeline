import os
import pandas as pd
from typing import Optional
from config import logging, DATA_DIR

from typing import Optional

logger = logging.getLogger(__name__)

def extract_csv_data(file_name: str) -> Optional[pd.DataFrame]:
    '''
    Pulling data from a CSV file, cleaning it up, and checking the integrity of the columns.
    '''

    # Merge the path with the main data folder
    csv_path = os.path.join(DATA_DIR, file_name)

    logger.info(f'--- Start reading csv file: {csv_path} ---')

    if not os.path.exists(csv_path):
        logger.error(f'File not found: {csv_path}')
        return None
        
    try:
        # Read the file
        df = pd.read_csv(csv_path)

        # 1. Clean the column names of spaces
        df.columns = df.columns.str.strip()

        # 2. Cleaning up text data within cells
        # We used apply to ensure the cleanup was applied to every text cell.
        df = df.apply(lambda col: col.str.strip() if col.dtype == 'object' else col)

        if df.empty:
            logger.warning(f"File {csv_path} is empty of records.")
            return None
        
        # 3. Checking for the presence of the required columns (Schema Validation)
        EXPECTED_COLUMNS = ['product_id', 'quantity', 'total_price']

        if not set(EXPECTED_COLUMNS).issubset(df.columns):
            missing = list(set(EXPECTED_COLUMNS) - set(df.columns)) 
            logger.error(f"Missing columns: {missing}")
            return None
        
        logger.info(f'✔️ Successfully extracted {len(df)} records.')
        return df
    
    except Exception as e:
        logger.error(f'❌ Unexpected error during extraction: {e}')
        return None