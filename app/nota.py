from pydantic import BaseModel
from typing import Text
from datetime import datetime
from uuid import UUID, uuid4


class Nota(BaseModel):

    id: UUID
    datetime_criacao: datetime
    datetime_modificacao: datetime
    anotacao: Text

    def __init__(__pydantic_self__, anotacao: Text) -> None:
        dados_da_nota = {
            "id": uuid4(),
            "datetime_criacao": datetime.now(),
            "datetime_modificacao": datetime.now(),
            "anotacao": anotacao
        }
        super().__init__(**dados_da_nota)

    def atualizar_anotacao(self, nova_anotacao: Text) -> None:
        self.datetime_modificacao = datetime.now()
        self.anotacao = nova_anotacao
