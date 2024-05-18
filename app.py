from taipy.gui import Gui, State, notify, Markdown, navigate
from routes.routes import routes

Gui(pages=routes, css_file="main.css").run(debug=True, dark_mode=True, use_reloader=True, title="Inicio de Sesión", stylekit=True,)
