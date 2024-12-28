from models.conexao import Database
from models.maquina_model import MaquinaModel

class MaquinaController(Database):

    def __init__(self):
        super().__init__()

    def inserir(self, dados=MaquinaModel):
        conn = self.conectar()
        cursor = conn.cursor()
        id = 0
        try:
            cursor.execute('''
            INSERT INTO maquina (modelo, on_off, nivel_oleo, temperatura_oleo, nivel_agua, nivel_detegente, contem_soda, status_motor, temporizador) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (dados['modelo'], dados['on_off'], dados['nivel_oleo'], dados['temperatura_oleo'], dados['nivel_agua'], dados['nivel_detegente'], dados['contem_soda'], dados['status_motor'], dados['temporizador']))
            conn.commit()
            id = cursor.lastrowid
        except Exception as e:
            conn.rollback()
            return {'msg': f"Erro: {e}"}
        finally:
            cursor.close()
            conn.close()
        return {"msg": f"Item {id} salvo com sucesso!"}
    
    def atualizar(self, id, dados=MaquinaModel):
        conn = self.conectar()
        cursor = conn.cursor()
        id = id
        try:
            cursor.execute('''
            UPDATE maquina SET modelo=?, on_off=?, nivel_oleo=?, temperatura_oleo=?, nivel_agua=?, nivel_detegente=?, contem_soda=?, status_motor=?, temporizador=? WHERE id = ?
            ''', (dados['modelo'], dados['on_off'], dados['nivel_oleo'], dados['temperatura_oleo'], dados['nivel_agua'], dados['nivel_detegente'], dados['contem_soda'], dados['status_motor'], dados['temporizador'], id))
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
            cursor.execute('SELECT * FROM maquina')
            linhas = cursor.fetchall()
            lista = [{'id':e[0], 'modelo':e[1], 'on_off':e[2], 'nivel_oleo':e[3], 'temperatura_oleo':e[4], 'nivel_agua':e[5], 'nivel_detegente':e[6], 'contem_soda':e[7], 'status_motor':e[8], 'temporizador':e[9]} for e in linhas]
            
        except Exception as e:
            conn.rollback()
            return {'msg': f"Erro: {e}"}
        finally:
            cursor.close()
            conn.close()
        return lista
    
    '''
    modelo, on_off, nivel_oleo, temperatura_oleo, nivel_agua, nivel_detegente, contem_soda, status_motor, temporizador
    {'id':e[0], 'modelo':e[1], 'on_off':e[2], 'nivel_oleo':e[3], 'temperatura_oleo':e[4], 'nivel_agua':e[5], 'nivel_detegente':e[6], 'contem_soda':e[7], 'status_motor':e[8], 'temporizador':e[9]}
    
    '''