from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import date

app = FastAPI()

lista = []

class Todo(BaseModel):
    tarefa: str
    realizada: bool
    prazo: Optional[date]


@app.post('/inserir')
def inserir(todo: Todo):
    try:
        lista.append(todo)
        return {'status': 'sucesso'}
    except:
        return {'status': 'erro'}
    

@app.post('/lista')
def inserir(opcao: int = 0):
    if opcao == 0:
        return lista
    elif opcao == 1:
        return list(filter(lambda x: x.realizada == False, lista))
    elif opcao == 2:
        return list(filter(lambda x: x.realizada == True, lista))
    

@app.get('/listaUnica/{id}')
def listar(id: int):
    try:
        return lista[id]
    except:
        return {'status': 'Tarefa inexistente'}
    

@app.post('/alteraStatus')
def altera_status(id: int):
    try:
        lista[id].realizada = not lista[id].realizada
        return {'status': 'sucesso'}
    except:
        return {'status': 'erro'}
    

@app.post('/excluirTarefa')
def excluir_tarefa(id: int):
    try:
        del lista[id]
        return {'status': 'Tarefa deletada'}
    except:
        return {'status': 'erro'}