from sqlalchemy import create_engine

# AKA connection/driver with the DB

USER = "root"
PASSWORD = ""
HOST = "localhost:3306"
DATABASE = "ListDB"

engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}")
