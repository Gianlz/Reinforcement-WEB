from sqlalchemy import Column, Integer, String, Boolean, DATE, func
from sqlalchemy.orm import declarative_base
from app.database import engine


Base = declarative_base()


# Tables of the DB
class TodoTable(Base):
    __tablename__ = "todo"
    
    _id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(25),nullable= False)
    description = Column(String(50))
    completed = Column(Boolean, nullable=False)
    creation_date = Column(DATE, nullable=False, default=func.current_date())

    def __init__(self, nome=None, description=None):
        self.name = nome
        self.description = description
        self.completed = False

        
# Criar as tabelas no banco (caso ainda não existam)
Base.metadata.create_all(engine)


