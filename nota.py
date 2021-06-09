from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime
from uuid import UUID, uuid4


class Nota(BaseModel):

    id: UUID
    datetime_criação:datetime
    datetime_modificação: datetime
    anotação: Text = None

    def __init__(__pydantic_self__, anotação: Text) -> None:
        dados_da_nota = {
            "id": uuid4(),
            "datetime_criação": datetime.now(),
            "datetime_modificação": datetime.now(),
            "anotação": anotação
        }
        super().__init__(**dados_da_nota)

    def atualizar_anotação(self, nova_anotação: Text) -> None:
        self.datetime_modificação = datetime.now()
        self.anotação = nova_anotação

        # TODD: IMPLEMENTAR EXEÇÃO PARA QUANDO A NOTA NÃO EXISTIR
