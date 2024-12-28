#executar comando: pip install -r requirements.txt
#como rodar: uvicorn app.main:app --reload

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from models.maquina_model import MaquinaModel
from controllers.serie_controller import SerieController

api = FastAPI(
    title="API - OilCycle FACEPE",
    version="0.0.2",
    description="RESP API OilCycle - Projeto de um aparelho Eletrodoméstico para processar óleo de cozinha.",
)

#Lembre-se que a API vai tá no endereço: http://127.0.0.1:8000/docs 
#Métodos ou ENDPOINT da RESP API

@api.post("/novaSerie")# Define o endpoint
def nova_serie(ano: int, versao: float, modelo: str):
    obj = SerieController()
    return obj.inserir({'ano':ano, 'versao':versao, 'modelo': modelo})

@api.put("/atualizarSerie/{id}")
def atualizar_serie(id: int, ano: int, versao: float, modelo: str):
    obj = SerieController()
    return obj.atualizar(id,{'ano':ano, 'versao':versao, 'modelo': modelo})

@api.get("/listaSerie")
def listar_serie():
    obj = SerieController()
    return obj.listar()

@api.delete("/excluiSerie/{id}")
def excluir_serie(id:int):
    obj = SerieController()
    return obj.excluir(int(id))



#Corpo da requisição, informação enviada pelo cliente para a API
api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




