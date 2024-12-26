#executar comando: pip install -r requirements.txt
#como rodar: uvicorn app.main:app --reload

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from models.aparelho_model import AparelhoModel
from controllers.serie_controller import SerieController

api = FastAPI(
    title="API - OilCycle FACEPE",
    version="0.0.1",
    description="RESP API OilCycle - Projeto de um aparelho Eletrodomêstico para processar óleo de cozinha.",
)

#Lembre-se que a API vai tá no endereço: http://127.0.0.1:8000/docs 
#Métodos ou ENDPOINT da RESP API

@api.post("/novaSerie")# Define o endpoint
def nova_serie(ano: int, versao: float, modelo: str):
    obj = SerieController()
    return obj.inserir({'ano':ano, 'versao':versao, 'modelo': modelo})

'''
@api.post("/novoAparelho/")
def novoAparelho(dados:AparelhoModel):
    #classe model aqui. Ex. obj = AparelhoModel()
    return {'teste_post': 'Teste de um POST novo aparelho'}


@api.put("/editarAparelho/{id}/")
def atualizarAparelho(codigo: str, dados: AparelhoModel):
    dados.codigo = id
    return {'teste_put': f'Teste de um PUT novo aparelho: {id}'}

@api.delete("/excluirAparelho/{id}")
def desativarAparelho(codigo:str):
    return {'teste_delete': f'Teste de um Delete novo aparelho: {id}'}

@api.get("/aparelhos/")
def listarAparelhos():
    return {'teste_aparelhos': f'Mostrar todos os aparelhos'}

@api.get("/aparelho/{id}/")
def buscarAparelho(id: AparelhoModel):
    if not id:
        raise HTTPException(status_code=404, detail="Aparelho não encontrado!")
    return {'teste_exception': f'Teste de busca do aparelho: {id}'}


#Login dos admin
@api.post("/login")
def login(token: str):
    #classe model aqui. Ex. obj = LoginModel()
    return {'login','Realizar um token'}

'''

#Corpo da requisição, informação enviada pelo cliente para a API
api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




