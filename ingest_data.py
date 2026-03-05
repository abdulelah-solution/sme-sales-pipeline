import pandas as pd
from src.database import SessionLocal
from src.extractor import extract_csv_data
from src.crud import create_product, create_sale
from config import logging

logger = logging.getLogger(__name__)

# Sample data to ensure products are in the database before sales are recorded
dummy_products = [
    {"name": "Laptop Pro 15", "price": 4500.00, "stock_quantity": 10},
    {"name": "Wireless Mouse", "price": 150.00, "stock_quantity": 50},
    {"name": "Mechanical Keyboard", "price": 350.00, "stock_quantity": 25}
]


def run_ingestion():
    logger.info('--- 🚀 Starting Ingestion Pipeline ---')

    # 1. Pulling data from the file (pass only the filename because the extractor uses DATA_DIR)
    data = extract_csv_data('daily_sales.csv')

    # 2. Opening the session and dealing with the rule
    with SessionLocal() as db:
        logger.info('📦 Step 1: Adding/Syncing dummy products...')
        for item in dummy_products:
            create_product(
                    name = item['name'],
                    price = item['price'],
                    stock = item['stock_quantity'],
                    db = db
            )
        
    # 3. Processing CSV Sales
    if data is not None:
        logger.info(f'📉 Step 2: Processing {len(data)} sales from CSV...')
        
        for _, row in data.iterrows():
            new_sale = create_sale(
                            product_id = int(row['product_id']),
                            quantity = int(row['quantity']),
                            total_price = float(row['total_price']),
                            db = db
                        )
            if new_sale:
                    logger.info(f'✅ Sale recorded - ID: {new_sale.id}')
    else:
        logger.warning("⚠️ No CSV data to process.")
    
    logger.info('--- 🏁 Ingestion Pipeline Finished ---')


if __name__ == "__main__":
    run_ingestion()