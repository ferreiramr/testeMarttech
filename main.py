from typing import Text
from fastapi import FastAPI, datastructures
from nota import Nota


app = FastAPI()

notas = {}

@app.post("/notas/nova_nota/{anotacao: Text}")
def nova_nota(anotação: Text):

    nova_nota = Nota(anotação)
    
    notas[nova_nota.id] = nova_nota

    return {"id": nova_nota.id,
            "data de criação": nova_nota.datetime_criação,
            "data de modificação": nova_nota.datetime_modificação,
            "anotação": nova_nota.anotação}

def atualizar_nota():
    pass

@app.get("/notas/todas_as_notas")
def todas_as_notas():
    return notas

@app.get("/notas/nota/{id: uuid}")
def nota_por_id(id):
    pass

@app.delete("/nota/deletar/{id: uuid}")
def deletar_nota(id):
    pass