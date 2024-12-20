
import pyrebase

class UserController:

    config = {
    "apiKey": "AIzaSyBeI3TmqeOUihbuL9om1bUGA7MjBlHTEzg",
    "authDomain": "ecomp-observatorio.firebaseapp.com",
    "databaseURL": "https://ecomp-observatorio-default-rtdb.firebaseio.com",
    "storageBucket": "ecomp-observatorio.appspot.com",
    "serviceAccount": "controllers/key-admin.json"
    }

    def __init__(self):
        firebase = pyrebase.initialize_app(config=self.config)
        self.auth = firebase.auth()

    def login(self, username:str, password:str):
        try:
            user = self.auth.sign_in_with_email_and_password(username, password)
            return {"Sucesso!": f"idToken={user['idToken']}"}
        except Exception as e:
            return {"msg": f"E-mail ou senha inválidos!\n{e}"}
