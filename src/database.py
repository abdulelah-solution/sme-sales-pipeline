from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from config import DATABASE_URL, logging


logger = logging.getLogger(__name__)


# Creating a database engine
# connect_args is only necessary for SQLite to allow access from multiple threads
engine = create_engine(
                DATABASE_URL,
                connect_args = {'check_same_thread': False}
            )
    
SessionLocal = sessionmaker(
                    autocommit = False, 
                    autoflush = False, 
                    bind = engine
                )

class Base(DeclarativeBase):
    '''
    The base class for all models.  
    Any table we create later must inherit from this class.
    '''
    pass

logger.info('Database engine and session factory initialized.')
