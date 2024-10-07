import unittest
from ..views.main_view import MainView
from ..controllers.main_controller import MainController
import tkinter as tk


class TestMainWindow(unittest.TestCase):

        def setUp(self):
            self.controller = MainController(MainView)
            self.view = MainView(self.controller)
            self.view.iniciar()  # Inicia la ventana para que los widgets estén disponibles

        def tearDown(self):
            if self.view.window.winfo_exists():  # Verificar si la ventana existe
                self.view.window.destroy()  # Destruye la ventana después de cada prueba

        def test_button_clicks(self):
            # Simula clics en los botones y verifica que se llamen los métodos del controlador
            self.view.btn_limpiar.event_generate("<Button-2>")  # Simula un clic izquierdo del ratón
            # ... (verifica que se imprimió el mensaje correspondiente en la consola)

    #         self.view.btn_limpiar.event_generate("<Button-1>")
    #         # ... (verifica el mensaje)
    #
    #         # ... (repite para los demás botones)
    #
    #     # Puedes agregar más métodos de prueba para verificar otros aspectos de la vista
    #


if __name__ == '__main__':
    unittest.main()
