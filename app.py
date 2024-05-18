from taipy.gui import Gui
from routes.routes import routes
    
Gui(pages=routes, css_file="main.css").run(debug=True, dark_mode=True, use_reloader=True, title="Inicio de Sesión", stylekit=True,)

