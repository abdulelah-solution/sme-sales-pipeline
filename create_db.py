from src.database import engine, Base
import src.models as models
from config import logging

logger = logging.getLogger(__name__)

def init_db():
    '''
    The function of this file is to create tables in the database,
    based on the models defined in models.py.
    '''
    logger.info('--- 🛠️  Starting Database Creation Process ---')

    try:
        # Create all tables linked to Base
        Base.metadata.create_all(bind = engine)
        
        logger.info('✅ Tables created successfully! Check your project folder.')
        print('✅ Database is ready.') # Quick message to you in Terminal   
        
    except Exception as e:
        logger.error(f'❌ Failed to create tables: {e}')
        print(f'❌ Error: {e}')


if __name__ == "__main__":
    init_db()


    
