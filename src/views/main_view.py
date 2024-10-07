
from tkinter import ttk  # Importa colorchooser directamente
from PIL import Image, ImageTk
from ttkthemes import ThemedTk
import config


class MainView:
    def __init__(self, controller):
        self.sellerlistview = None
        self.root = ttk
        self.window = ThemedTk(theme="arc")
        self.window.title("Multifunciones Sotfware")
        self.controller = controller
        self.limpiar_entry = False
        self.create_widgets()

    def create_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.window, padding="30")
        main_frame.grid(row=0, column=0, sticky="nsew")

        # Logo en lugar del título (con redimensionamiento manteniendo la proporción)
        logo_image = Image.open(config.LOGO)
        ancho_original, alto_original = logo_image.size
        nuevo_alto = 120
        nuevo_ancho = int(ancho_original * (nuevo_alto / alto_original))
        logo_image = logo_image.resize((nuevo_ancho, nuevo_alto), Image.Resampling.LANCZOS)
        logo_photo = ImageTk.PhotoImage(logo_image)
        logo_label = ttk.Label(main_frame, image=logo_photo)
        logo_label.image = logo_photo
        logo_label.grid(row=0, column=0, columnspan=6, pady=(0, 30))


        # Botones en escala de grises
        button_styles = [
            ("Salir", "#555555", self.cerrar_aplicacion),
            ("Limpiar", "#666666", self.controller.manejar_clic_boton_limpiar_documento),
            ("Guardar", "#777777", self.controller.manejar_clic_boton_guardar_documento),
            ("Recobros", "#888888", self.controller.manejar_clic_boton_recobros),
            ("Generar PDF", "#999999", self.controller.manejar_clic_boton_generar_pdf),
            ("Actualizar BD", "#AAAAAA", self.controller.manejar_clic_boton_actualizar_base_de_datos),
        ]

        for i, (text, color, command) in enumerate(button_styles):
            self.create_button(main_frame, text, color, command, 1, i)

        # Etiqueta y entrada para el ID
        ttk.Label(main_frame, text="No.Doc:",foreground = "black").grid(row=2, column=0, padx=(0, 10), pady=(30, 0), sticky="w")
        self.id_entry = ttk.Entry(main_frame)
        self.id_entry.grid(row=2, column=1, columnspan=2, pady=(30, 0), sticky="ew")
        self.id_entry.bind("<Return>", self.on_enter_pressed)

        # Configurar el grid
        for i in range(3):
            main_frame.columnconfigure(i, weight=1)
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)

    def create_button(self, parent, text, color_string, command, row, column):
        """Crea un botón con estilo y lo coloca en el grid."""
        button = ttk.Button(parent, text=text, command=command)  # Sin estilo "Rounded.TButton"
        button.grid(row=row, column=column, padx=5, pady=5, sticky="ew")

        # Configurar el estilo del botón (escala de grises)
        style = ttk.Style()
        style.configure("TButton", background=color_string, foreground="black",
                        font=("Arial", 10), borderwidth=0, focuscolor=color_string)  # Sin negrita


    def on_enter_pressed(self, event):
        """Maneja el evento Enter en el textbox."""
        self.controller.handle_id_entry_enter(self.id_entry.get())
        self.id_entry.delete(0, 'end')

    # ... (resto de los métodos mostrar_informacion, obtener_datos_textbox, etc.)

    def cerrar_aplicacion(self):
        """Cierra la aplicación."""
        self.window.destroy()  # Cerrar la ventana principal


    def iniciar(self):
        self.window.mainloop()
