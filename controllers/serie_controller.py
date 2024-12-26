from models.conexao import Database
from models.serie_model import SerieModel

class SerieController(Database):

    def __init__(self):
        super().__init__()

    def inserir(self, dados=SerieModel):
        cursor = self.conectar()
        try:
            id = cursor.execute('''
            INSERT INTO serie (ano, versao, modelo) VALUES (?, ?, ?)''', (dados['ano'], dados['versao'], dados['modelo']))
            cursor.commit()
            
        except Exception as e:
            self.rollBack()
            return {'msg': f"Erro: {e}"}
        finally:
            cursor.close()
            self.fechar()
        return {"id": id, "ano": dados['ano'], "versao": dados['versao'], "modelo": dados['modelo']}
    