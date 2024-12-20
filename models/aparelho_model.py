from pydantic import BaseModel

class AparelhoModel(BaseModel):
    codigo: str
    versao: str
    modelo: str