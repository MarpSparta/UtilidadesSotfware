from tkinter import ttk
from ttkthemes import ThemedTk  # Asegúrate de tener instalada la librería ttkthemes
from ..utils.file_helpers import list_folders
import config

class SellerListView:
    def __init__(self, controller):
        self.root = ttk
        self.window = ThemedTk(theme="arc")
        self.window.title("Vendedores")
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.window, padding="30")
        main_frame.grid(row=0, column=0, sticky="nsew")

        # --- Frame para la lista de nombres ---
        lista_frame = ttk.Frame(main_frame)
        lista_frame.grid(row=0, column=0, columnspan=2, pady=(30, 10), sticky="ew")

        # Lista de nombres
        self.nombre_list = ttk.Combobox(lista_frame, width=30)  # Ajustar ancho del combobox
        self.nombre_list['values'] = list_folders(config.TEST_SALES_PATH)
        self.nombre_list.pack(side="left", fill="x", expand=True, padx=5, pady=5)

        # Botón Guardar para la lista
        guardar_lista_button = self.create_button(lista_frame, "Guardar Excel", "#555555", self.guardar_valor_lista)
        guardar_lista_button.pack(side="left", padx=5, pady=5)
        # --- Fin del frame para la lista ---

        # --- Frame para el textbox ---
        textbox_frame = ttk.Frame(main_frame)
        textbox_frame.grid(row=1, column=0, columnspan=2, pady=10, sticky="ew")

        # Label y textbox
        nombre_vendedor_label = ttk.Label(textbox_frame, text="Nombre del Nuevo vendedor: ")
        nombre_vendedor_label.pack(side="left", padx=5, pady=5)

        self.nombre_vendedor_entry = ttk.Entry(textbox_frame)
        self.nombre_vendedor_entry.pack(side="left", fill="x", expand=True, padx=5, pady=5)

        # Botón Guardar para el textbox
        guardar_textbox_button = self.create_button(textbox_frame, "Vendedor Nuevo", "#666666",
                                                    self.guardar_valor_textbox)
        guardar_textbox_button.pack(side="left", padx=5, pady=5)
        # --- Fin del frame para el textbox ---

        # Configurar el grid
        for i in range(2):
            main_frame.columnconfigure(i, weight=1)
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)

        # --- Ajustar tamaño de la ventana ---
        self.window.update_idletasks()  # Actualizar la ventana para obtener el tamaño correcto
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        self.window.geometry(f"{width}x{height}")  # Ajustar el tamaño

    def create_button(self, parent, text, color_string, command, row=None, column=None):
        """Crea un botón con estilo."""
        button = ttk.Button(parent, text=text, command=command, width=20)  # Ajustar ancho del botón
        if row is not None and column is not None:
            button.grid(row=row, column=column, padx=5, pady=5, sticky="ew")
        return button

    def guardar_valor_lista(self):
        valor_seleccionado = self.nombre_list.get()
        print("Valor seleccionado de la lista:", valor_seleccionado)
        # Llamada al controlador para la lista
        self.controller.guardar_valor_lista(valor_seleccionado)

    def guardar_valor_textbox(self):
        valor_textbox = self.nombre_vendedor_entry.get()
        print("Valor del textbox:", valor_textbox)
        #Limpia el textbox
        self.nombre_vendedor_entry.delete(0, "end")
        # Llamada al controlador para el textbox
        self.controller.guardar_valor_textbox(valor_textbox)

        # --- Actualizar la lista de nombres ---
        self.actualizar_lista_nombres()

    def actualizar_lista_nombres(self):
        """Actualiza la lista de nombres en el Combobox."""
        nueva_lista = list_folders(config.TEST_SALES_PATH)
        self.nombre_list['values'] = nueva_lista

    def iniciar(self):
        self.window.mainloop()