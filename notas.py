from nota import Nota
from typing import Dict, Optional, Text
from uuid import UUID

class Notas():

    def __init__(self):
        self.notas = dict()

    def adicionar(self, anotação:Text)->Nota:
        nova_nota = Nota(anotação)
        self.notas[nova_nota.id] = nova_nota
        return nova_nota

    def atualizar(self, id:UUID, anotação:Text)->Optional[Nota]:
        self.notas[id].atualizar_anotação(anotação)
        return self.notas[id]

    def excluir(self, id:UUID)->Optional[Nota]:
        return self.notas.pop(id, None)

    def nota(self, id:UUID)->Optional[Nota]:
        return self.notas[id]

    def listar(self)->Dict[UUID, Nota]:
        return self.notas
