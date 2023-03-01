import sqlalchemy
from sqlalchemy.orm import declarative_base

db_name = "test_db"
Base = declarative_base()
Engine = sqlalchemy.create_engine('sqlite:///' + db_name + '.db', echo=True)
