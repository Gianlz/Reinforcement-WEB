from app.controllers.todo import add_to_DB, get_all
from app.models.todo import TodoTable


# Entry Point of the code'

# Teste de adição
add_to_DB("tarefa1", "Tarefa muito foda feita por mim, sem validação")

# Teste de recuperar dados
content = get_all()
for todo in content:
    print(f"ID:{todo._id}\nName [{todo.name}]\nDescription [{todo.description}]\nCompleted [{todo.completed}]")
