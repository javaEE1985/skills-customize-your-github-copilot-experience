from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

# Inicialize a aplicação FastAPI
app = FastAPI(
    title="Task Management API",
    description="Uma API simples para gerenciar tarefas",
    version="1.0.0"
)

# Modelo Pydantic para validação de dados
class TaskBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=100, description="Título da tarefa")
    description: str = Field(..., min_length=5, max_length=500, description="Descrição da tarefa")
    completed: bool = Field(default=False, description="Status de conclusão da tarefa")

class Task(TaskBase):
    id: int = Field(..., description="ID único da tarefa")
    created_at: datetime = Field(default_factory=datetime.now, description="Data de criação")

# Simulação de banco de dados em memória
tasks_db: List[Task] = []
next_id = 1

# TODO: Implementar endpoint POST para criar nova tarefa
# Deve validar os dados e retornar status 201

# TODO: Implementar endpoint GET para listar todas as tarefas

# TODO: Implementar endpoint GET para obter tarefa específica por ID
# Deve retornar 404 se tarefa não existir

# TODO: Implementar endpoint PUT para atualizar tarefa existente
# Deve validar ID e dados antes de atualizar

# TODO: Implementar endpoint DELETE para deletar tarefa
# Deve retornar 404 se tarefa não existir

# Inicie o servidor com: uvicorn starter-code:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
