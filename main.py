from typing import Dict, Optional, Text
from uuid import UUID
from fastapi import FastAPI
from nota import Nota

app = FastAPI()

notas = {}

@app.get("/")
def home():
    return {"Projeto": "Teste Martech",
            "Autor" : "Marcos Ferreira",
            "Situação do Projeto": "Impletamenta as funções para adicinar e listar notas"}

@app.post("/notas/nova/{anotacao: Text}")
def nova_nota(anotação: Text)->Nota:
    """
    Adiciona uma nova nota
    """
    nova_nota = Nota(anotação)
    notas[nova_nota.id] = nova_nota

    return nova_nota

@app.put("/notas/atualizar/{id: UUID}")
def atualizar_nota(id: UUID, nova_anotação: Text)->Nota:
    """
    Atualiza a anotação de uma nota
    """

    # TODD: IMPLEMENTAR EXEÇÃO PARA QUANDO A NOTA NÃO EXISTIR

    notas[id].atualizar(nova_anotação)
    return notas[id]

@app.get("/notas/todas")
def todas_as_notas()->Dict[Nota]:
    """
    Exibe todas as notas
    """
    return notas

@app.get("/notas/nota/{id: UUID}")
def nota_por_id(id:UUID)->Nota:
    """
    Exibe uma nota a partir de seu UUID
    """

    # TODD: IMPLEMENTAR EXEÇÃO PARA QUANDO A NOTA NÃO EXISTIR
    
    return notas[id]

@app.delete("/nota/deletar/{id: UUID}")
def deletar_nota(id:UUID):
    """
    Deleta uma nota a partir de seu UUID
    """

    # TODD: IMPLEMENTAR EXEÇÃO PARA QUANDO A NOTA NÃO EXISTIR

    return notas.pop(id, None)
