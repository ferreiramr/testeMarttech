from typing import Dict, Text
from uuid import UUID
from fastapi import FastAPI, HTTPException, status
from pydantic import Json, ValidationError
from app.notas import Notas
from app.nota import Nota

app = FastAPI(
    title="Teste Martech - Marcos Ferreira",
    description="Teste do processo seletivo para a vaga de desenvolvedor Python. O escopo do projeto consiste em crir um bloco de anotações utilizando biblioteca FastAPI na AWS Lambada gerenciada pelo AWS API Gateway"
)

notas = Notas()


@app.get("/",tags=["Descrição do Projeto"])
def descricao_do_projeto():
    return {"Projeto": "Teste Martech",
            "Autor": "Marcos Ferreira",
            "Descriao": "Teste realizado para a vaga de desenvolvedor Python",
            "Status": "CRUD finalizada com funcionalidades essenciais coberta por testes"}


@app.post("/nova-nota/{anotacao: Text}", status_code=201, tags=['Adicionar Nota'])
def nova_nota(anotacao: Text) -> Nota:
    """
    View que adiciona uma nova nota
    """
    try:
        return notas.adicionar(anotacao)
    except ValidationError:
        return ValidationError(status=402, detail="Tamanho máximo da anotação excedido")


@app.get("/obter-nota/{id: UUID}", tags=['Pesquisar Notas'])
def obter_uma_nota(id: UUID) -> Nota:
    """
    View que mostra uma nota a partir de seu UUID
    """
    print(type(notas.nota(id)))
    if notas.existe(id):
        return notas.nota(id)
    else:
        return HTTPException(status_code=404, detail="Nota nao localizada")


@app.get("/todas-as-notas", tags=['Pesquisar Notas'])
def obter_todas_as_notas() -> Dict[UUID, Nota]:
    """
    View que mostra todas as notas
    """
    return notas.listar()


@app.put("/atualizar-nota/{id: UUID}", status_code=201, tags=['Atualizar Nota'])
def atualizar_uma_nota(id: UUID, nova_anotacao: Text) -> Nota:
    """
    View que atualiza uma nota à partir de seu UUID
    """
    if notas.existe(id):
        return notas.atualizar(id, nova_anotacao)
    else:
        return HTTPException(status_code=404, detail="Nota nao localizada")


@app.delete("/excluir-nota/{id: UUID}", tags=['Excluir Notas'])
def excluir_uma_nota(id: UUID) -> Nota:
    """
    View que exclui uma nota a partir de seu UUID
    """
    if notas.existe(id):
        return notas.excluir(id)
    else:
        return HTTPException(status_code=404, detail="Nota nao localizada")


@app.delete("/exluir-todas-as-notas", tags=['Excluir Nota'])
def excluir_todas_as_notas() -> Dict[None, None]:
    """
    View que excluir todas as todas as notas
    """
    notas.excluir_todas()
    return notas.listar()
