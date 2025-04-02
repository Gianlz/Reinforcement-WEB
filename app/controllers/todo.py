from app.models.todo import todo_table
from app.database import engine
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=engine)


def add_to_DB(name: str, description = "") -> None:
    """Adiciona novo TODO para o banco de dados"""
    tabela = todo_table(name,description)
    session = Session()
    session.add(tabela)
    session.commit()
    session.close()
    


