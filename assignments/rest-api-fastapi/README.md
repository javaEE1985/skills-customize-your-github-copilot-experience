# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objective

Você aprenderá a construir APIs REST profissionais utilizando o framework FastAPI. Durante esta tarefa, você criará endpoints para operações CRUD, implementará validação de dados, e utilizará o interactive API documentation do FastAPI para testar suas APIs.

## 📝 Tasks

### 🛠️ Criar uma API básica com CRUD para Tarefas

#### Description
Construa uma API REST completa que gerencie uma lista de tarefas. A API deve permitir criar, ler, atualizar e deletar tarefas. Cada tarefa deve ter um ID único, título, descrição e status de conclusão.

#### Requirements
Completed program should:

- Implementar endpoint POST `/tasks` para criar nova tarefa com validação de dados
- Implementar endpoint GET `/tasks` para listar todas as tarefas
- Implementar endpoint GET `/tasks/{id}` para obter uma tarefa específica
- Implementar endpoint PUT `/tasks/{id}` para atualizar uma tarefa existente
- Implementar endpoint DELETE `/tasks/{id}` para deletar uma tarefa
- Retornar respostas JSON apropriadas com status HTTP corretos (201 para criação, 404 para não encontrado, etc.)


### 🛠️ Implementar Validação de Dados com Pydantic

#### Description
Utilize Pydantic para definir modelos de dados que validem automaticamente as entradas do usuário. Garanta que os dados recebidos estejam no formato correto e contenham os campos obrigatórios.

#### Requirements
Completed program should:

- Definir modelos Pydantic para Task com campos: id, title, description, completed
- Implementar validação de comprimento mínimo/máximo para título e descrição
- Retornar mensagens de erro detalhadas quando dados inválidos forem enviados
- Utilizar type hints para melhorar a documentação automática da API


### 🛠️ Utilizar FastAPI Interactive Documentation

#### Description
Explore e teste sua API utilizando o Swagger UI e ReDoc, que são gerados automaticamente pelo FastAPI. Use a documentação interativa para validar que todos os endpoints funcionam corretamente.

#### Requirements
Completed program should:

- Acessar `/docs` para abrir o Swagger UI e testar endpoints
- Acessar `/redoc` para visualizar a documentação em formato ReDoc
- Adicionar descrições aos endpoints usando docstrings para melhorar a documentação
- Testar todos os endpoints (criação, listagem, atualização, deleção) através da interface interativa
