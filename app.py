from taipy.gui import Gui, State, notify, Markdown, navigate
from chat_page import chat

def on_login(state: State, id, login_args):
    username, password = login_args["args"][:2]
    if username == "kiraft" and password == "pass":
        navigate(state, to="/chat")
    else:
        print("No existe este usuario")

page = Markdown(
"""
<|Welcome to Taipy!|login|>
""")

routes = {
    "home": page,
    "chat": chat,
}
    
if __name__ == "__main__":
    Gui(pages=routes, css_file="style.css").run(debug=True, dark_mode=True, use_reloader=True, title="Inicio de Sesión", stylekit=True,)
