from taipy.gui import Gui, State, notify, Markdown, navigate
import requests


def on_login(state: State, id, login_args):
    username, password = login_args["args"][:2]
    validate = auth_user(user=username, password=password)
    if validate == True:
        navigate(state, to="/chat", tab="_self")
    else:
        print("No existe este usuario")


def auth_user(user, password):
    endpoint = "https://hackthon-edubot-api.onrender.com/api/v1/user/login"
    
    params = {
    "username": user,
    "password": password
    }
    response = requests.get(endpoint, params=params)
    
    if response.status_code == 200:        
        return True
    else:
        print(f"Error: {response.status_code}")
        return False
    
def auth_google():
    return False
    
    

login = Markdown(
"""
<|Welcome to Taipy!|login|>
""")