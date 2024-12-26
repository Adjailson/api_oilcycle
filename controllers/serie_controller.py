from models.conexao import Database
from models.serie_model import SerieModel

class SerieController(Database):

    def __init__(self):
        super().__init__()

    def inserir(self, dados=SerieModel):
        conn = self.conectar()
        cursor = conn.cursor()
        id = 0
        try:
            cursor.execute('''
            INSERT INTO serie (ano, versao, modelo) VALUES (?, ?, ?)''', (dados['ano'], dados['versao'], dados['modelo']))
            conn.commit()
            id = cursor.lastrowid
        except Exception as e:
            conn.rollback()
            return {'msg': f"Erro: {e}"}
        finally:
            cursor.close()
            conn.close()
        return {"id": id, "ano": dados['ano'], "versao": dados['versao'], "modelo": dados['modelo']}
    
    def atualizar(self, id, dados=SerieModel):
        conn = self.conectar()
        cursor = conn.cursor()
        id = id
        try:
            cursor.execute('''
            UPDATE serie SET ano = ?, versao = ?, modelo = ? WHERE id = ?''', (dados['ano'], dados['versao'], dados['modelo'], id))
            conn.commit()
        except Exception as e:
            conn.rollback()
            return {'msg': f"Erro: {e}"}
        finally:
            cursor.close()
            conn.close()
        return {"msg": f'Item {id} atualizado com sucesso!'}
    
    def listar(self):
        conn = self.conectar()
        cursor = conn.cursor()
        lista = []
        try:
            cursor.execute('SELECT * FROM serie')
            linhas = cursor.fetchall()
            lista = [{'id':e[0], 'ano': e[1],'versao':e[2], 'modelo':e[3]} for e in linhas]
            
        except Exception as e:
            conn.rollback()
            return {'msg': f"Erro: {e}"}
        finally:
            cursor.close()
            conn.close()
        return lista
    
    def excluir(self,id):
        conn = self.conectar()
        cursor = conn.cursor()
        try:
            cursor.execute('DELETE FROM serie WHERE id = ?',(id,))
            conn.commit()
            
        except Exception as e:
            conn.rollback()
            return {'msg': f"Erro: {e}"}
        finally:
            cursor.close()
            conn.close()
        return {'msg': f'Item {id} deletado com sucesso!'}