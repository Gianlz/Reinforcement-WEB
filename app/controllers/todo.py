from app.models.todo import TodoTable
from app.database import engine
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=engine)


def add_to_DB(name: str, description = "") -> None:
    """Adiciona novo TODO para o banco de dados"""
    tabela = TodoTable(name,description)
    session = Session()
    session.add(tabela)
    session.commit()
    session.close()
    
def get_all():
    session = Session()
    content = session.query(TodoTable).all()
    session.close()
    return content


