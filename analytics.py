import os
import pandas as pd
from sqlalchemy import text
from config import logging, OUTPUT_DIR
from src.database import engine

logger = logging.getLogger(__name__)

def generate_sales_report(file_name: str = 'daily_report.xlsx'):
    '''
    Pull data from SQL, perform Pandas analytics, and export it to an Excel file.
    '''

    # Specify the final path of the file within the output folder
    report_path = os.path.join(OUTPUT_DIR, file_name)

    logger.info("📊 Generating sales analytics report...")

    try:
        with engine.connect() as conn:
            query = text('''
                            SELECT 
                                p.name,
                                s.total_price,
                                s.quantity
                            FROM
                                sales s
                            JOIN 
                                products p
                            ON  s.product_id = p.id
                    ''')

            df = pd.read_sql(query, conn)

            if df.empty:
                logger.warning("⚠️ No data found in database to export.")
                return False
        
            # --- Analysis Phase (Analytics) ---
            agg_data = df.groupby('name').agg(
                            total_revenue = ('total_price', 'sum'),
                            total_sold = ('quantity', 'sum')
                        ).reset_index()
            
            # Ranking results from highest profit
            agg_data = agg_data.sort_values(by='total_revenue', ascending=False)

            # --- Export Phase ---
            agg_data.to_excel(report_path, index=False)

            logger.info(f"✔️ Report generated successfully at: {report_path}")
            return True

    except Exception as e:
            logger.error(f"❌ Failed to generate report: {e}")
            return False