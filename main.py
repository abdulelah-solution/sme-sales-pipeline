import sys
from config import logging
from src.database import engine
from create_db import init_db
from ingest_data import run_ingestion
from analytics import generate_sales_report

logger = logging.getLogger(__name__)

def run_pipeline():
    '''
    The main organizer of all project operations is:
    1. Database creation.
    2. Data import from CSV.
    3. Generating analytics and reports.
    '''
    print("🚀 Starting SME Sales Pipeline...")
    logger.info("=== 🏁 Pipeline Execution Started ===")

    try:
        # Phase One: Infrastructure Preparation
        print("1️⃣  Initializing Database...")
        init_db()

        # Phase Two: Data Loading (ETL)
        print("2️⃣  Ingesting Data from CSV...")
        run_ingestion()

        # Phase Three: Analysis and Reporting (Analytics)
        print("3️⃣  Generating Final Report...")
        success = generate_sales_report('daily_sales_analysis.xlsx')

        if success:
            print("✅ Pipeline executed successfully! Check the 'output' folder.")
            logger.info("=== ✨ Pipeline Finished Successfully ===")
        else:
            print("⚠️  Pipeline finished with warnings. Check 'app.log'.")

    except Exception as e:
        logger.critical(f"💥 Pipeline failed due to: {e}")
        print(f"❌ Critical Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_pipeline()