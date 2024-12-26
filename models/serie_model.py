from pydantic import BaseModel

# Classe de exemplo para cadastrar a série de um novo produto ou eletrodomêstico 
class SerieModel(BaseModel):
    ano: int
    versao: float
    modelo: str

    '''
    Ao final vou querer algo como:
    Ex.:
    ano 2024;
    versão 0.2 do nosso aparelho;
    modelo PA - só para dizer que nosso aparelho é a versão Pré-Automático
    Saída: 20240.2PA (Essa é nossa série do modelo do eletrodomêstico)
    '''

    def toMap(self):
        return {
            'ano': self.ano,
            'versao': self.versao,
            'modelo': self.modelo
        }