from src.controllers.main_controller import MainController  # Importación absoluta sin el punto inicial
from src.views.main_view import MainView

if __name__ == "__main__":
    controller = MainController(MainView)
    vista = MainView(controller)
    vista.iniciar()