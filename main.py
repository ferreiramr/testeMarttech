from typing import Dict, Text
from uuid import UUID
from fastapi import FastAPI, HTTPException
from app.notas import Notas
from app.nota import Nota

app = FastAPI()

notas = Notas()


@app.get("/")
def teste_Marttech():
    return {"Projeto": "Teste Martech",
            "Autor": "Marcos Ferreira",
            "Descriao": "Teste realizado para a vaga de desenvolvedor Python",
            "Situaao do Projeto": "CRUD finalizada"}


@app.post("/nova-nota/{anotacao: Text}", status_code=201, tags=['Adicionar'])
def nova_nota(anotacao: Text) -> Nota:
    """
    View que adiciona uma nova nota
    """
    return notas.adicionar(anotacao)


@app.get("/obter-nota/{id: UUID}", tags=['Pesquisar'])
def obter_uma_nota(id: UUID) -> Nota:
    """
    View que mostra uma nota a partir de seu UUID
    """
    print(type(notas.nota(id)))
    if notas.existe(id):
        return notas.nota(id)
    else:
        return HTTPException(status_code=404, detail="Nota nao localizada")


@app.get("/todas-as-notas", tags=['Pesquisar'])
def obter_todas_as_notas() -> Dict[UUID, Nota]:
    """
    View que mostra todas as notas
    """
    return notas.listar()


@app.put("/atualizar-nota/{id: UUID}", status_code=201, tags=['Atualizar'])
def atualizar_uma_nota(id: UUID, nova_anotacao: Text) -> Nota:
    """
    View que atualiza uma nota à partir de seu UUID
    """
    if notas.existe(id):
        return notas.atualizar(id, nova_anotacao)
    else:
        return HTTPException(status_code=404, detail="Nota nao localizada")


@app.delete("/excluir-nota/{id: UUID}", tags=['Excluir'])
def excluir_uma_nota(id: UUID) -> Nota:
    """
    View que exclui uma nota a partir de seu UUID
    """
    if notas.existe(id):
        return notas.excluir(id)
    else:
        return HTTPException(status_code=404, detail="Nota nao localizada")


@app.delete("/exluir-todas-as-notas", tags=['Excluir'])
def excluir_todas_as_notas() -> Dict[None, None]:
    """
    View que excluir todas as todas as notas
    """
    notas.excluir_todas()
    return notas.listar()
