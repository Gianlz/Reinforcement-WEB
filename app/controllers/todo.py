from app.models.todo import TodoTable
from app.database import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from contextlib import contextmanager


SessionLocal = sessionmaker(bind=engine)

@contextmanager
def db_session():
    """Gerenciador de contexto para operações com banco de dados"""
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        raise
    finally:
        session.close()


def add_to_DB(name: str, description = "") -> None:
    """Adiciona novo TODO para o banco de dados"""
    tabela = TodoTable(name,description)
    with db_session() as session:
        try:
            session.add(tabela) 
        except SQLAlchemyError as e:
            raise RuntimeError(f"Database error {str(e)}")
            
    
def get_all():
    with db_session() as session:
        try:
            query_result = session.query(TodoTable).all()
            result = []
            for item in query_result:
                todo = {
                    "_id": item._id,
                    "name": item.name,
                    "description": item.description,
                    "completed": item.completed,
                    "creation_date": item.creation_date
                }
                result.append(todo)
                
            return result
        except SQLAlchemyError as e:
            raise RuntimeError(f"Database error {str(e)}")
    


