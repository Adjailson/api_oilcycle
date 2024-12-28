from pydantic import BaseModel

class MaquinaModel(BaseModel):
    modelo: str # Gerar um modelo com base na série
    on_off: bool # Desligar a máquina
    nivel_oleo: int # Nível de óleo por Porcentagem
    temperatura_oleo: int # Temperatura atual do óleo
    nivel_agua: int # Nível de água por Porcentagem
    nivel_detegente: int # Nível de detegente por Porcentagem
    contem_soda: bool # Se contém soda cáustica
    status_motor: bool # Motor principal para mexer
    temporizador: int # Contador com o tempo dos processos para finalização