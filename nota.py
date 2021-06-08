from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime
from uuid import UUID, uuid4

class Nota(BaseModel):
    """
    Cria uma nova nota
    """
    id: Optional[UUID] = None
    datetime_criação: Optional[datetime] = None
    datetime_modificação: Optional[datetime] = None
    anotação: Text = None

    def __init__(__pydantic_self__, anotação: Text) -> None:
        dados_da_nota = {
            "id" : uuid4(),
            "datetime_criação" : datetime.now(),
            "datetime_modificação" :datetime.now(),
            "anotação" : anotação
        }
        super().__init__(**dados_da_nota)