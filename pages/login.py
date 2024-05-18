from taipy.gui import Gui, State, notify, Markdown, navigate

def on_login(state: State, id, login_args):
    username, password = login_args["args"][:2]
    if username == "kiraft" and password == "pass":
        navigate(state, to="/chat")
    else:
        print("No existe este usuario")

login = Markdown(
"""
<|Welcome to Taipy!|login|>
""")