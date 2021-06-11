from app.nota import Nota
from typing import Dict, Optional, Text
from uuid import UUID


class Notas():

    def __init__(self):
        self.notas = dict()

    def adicionar(self, anotacao: Text) -> Nota:
        nova_nota = Nota(anotacao)
        self.notas[nova_nota.id] = nova_nota
        return nova_nota

    def atualizar(self, id: UUID, anotacao: Text) -> Optional[Nota]:
        self.notas[id].atualizar_anotacao(anotacao)
        return self.notas[id]

    def excluir(self, id: UUID) -> Optional[Nota]:
        return self.notas.pop(id, None)

    def excluir_todas(self) -> Dict[None, None]:
        self.notas = {}

    def nota(self, id: UUID) -> Optional[Nota]:
        return self.notas[id]

    def listar(self) -> Dict[UUID, Nota]:
        return self.notas

    def existe(self, id: UUID) -> bool:
        return id in self.notas.keys()
