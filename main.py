from typing import Text
from fastapi import FastAPI, datastructures
from nota import Nota


app = FastAPI()

notas = {}

@app.get("/")
def home():
    return {"Projeto": "Teste Martech",
            "Autor" : "Marcos Ferreira",
            "Situação do Projeto": "Impletamenta as funções para adicinar e listar notas"}

@app.post("/notas/nova_nota/{anotacao: Text}")
def nova_nota(anotação: Text):
    """
    Adiciona uma nova nota
    """
    nova_nota = Nota(anotação)
    
    notas[nova_nota.id] = nova_nota

    return nova_nota

def atualizar_nota():
    pass

@app.get("/notas/todas_as_notas")
def todas_as_notas():
    """
    Exibe todas as notas
    """
    return notas

@app.get("/notas/nota/{id: uuid}")
def nota_por_id(id):
    pass

@app.delete("/nota/deletar/{id: uuid}")
def deletar_nota(id):
    pass