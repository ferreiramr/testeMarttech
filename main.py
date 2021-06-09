from typing import Dict, Text
from uuid import UUID
from fastapi import FastAPI
from notas import Notas
from nota import Nota

app = FastAPI()

notas = Notas()


@app.get("/")
def home():
    return {"Projeto": "Teste Martech",
            "Autor": "Marcos Ferreira",
            "Situação do Projeto": "CRUD implementada"}


@app.post("/notas/nova/{anotacao: Text}")
def nova(anotação: Text) -> Nota:
    """
    Adiciona uma nova nota
    """
    return notas.adicionar(anotação)


@app.put("/notas/atualizar/{id: UUID}")
def atualizar(id: UUID, nova_anotação: Text) -> Nota:
    """
    Atualiza a anotação de uma nota à partir de seu UUID
    """
    notas.atualizar(id, nova_anotação)


@app.get("/notas/todas")
def todas() -> Dict[UUID, Nota]:
    """
    Exibe todas as notas
    """
    return notas.listar()


@app.get("/notas/nota/{id: UUID}")
def nota(id: UUID) -> Nota:
    """
    Retorna uma nota a partir de seu UUID
    """
    return notas.nota(id)


@app.delete("/nota/deletar/{id: UUID}")
def deletar(id: UUID) -> Nota:
    """
    Deleta uma nota a partir de seu UUID
    """
    return notas.excluir(id)
