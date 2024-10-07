import config
from tkinter import messagebox
from ..models.ExcelManager import ExcelManager
from ..models.Generarpdf import GeneradorPDF
from ..models.fireStore import nube  # Assuming this handles cloud storage interaction
from ..utils.file_helpers import get_formatted_date_spanish, format_and_save_query_results # Assuming these are utility functions
from ..models.database import consulta, data_customer
from ..views.seller_list_view import SellerListView
from ..controllers.seller_list_controller import SellerListController


class MainController:
    """
    Controller class for the main view.
    Handles user interactions and updates the view accordingly.
    """

    def __init__(self, vista):
        """
        Initializes the MainController with the given view.

        Args:
            vista: The main view object.
        """
        self.vista = vista

    def manejar_clic_boton_salir(self):
        """
        Handles the click event of the "Exit" button.
        Currently not implemented (pass).
        """
        pass

    def manejar_clic_boton_limpiar_documento(self):
        """
        Handles the click event of the "Clean Document" button.
        Cleans the Excel data using ExcelManager and displays a success message.
        """
        ExcelManager(config.EXCEL_PATH, config.TEST_SALES_PATH, "NP", "NP", "NP").clean_excel_data()
        messagebox.showerror("Clean Document", "Cleaning completed.")


    def manejar_clic_boton_guardar_documento(self):
        """
        Handles the click event of the "Save Document" button.
        Instantiates and starts the SellerListView to allow the user to select sellers.
        """
        self.controller = SellerListController(self.vista)
        self.view = SellerListView(self.controller)
        print("Save Document button pressed")
        self.view.iniciar()  # Assuming this method starts the SellerListView

    def manejar_clic_boton_recobros(self):
        """
        Handles the click event of the "Recobros" button.
        This method seems to be related to adding a "recobro" (recovery),
        but the exact functionality is unclear without further context about 'add_recobro()'.
        """
        ExcelManager(config.EXCEL_PATH, config.TEST_SALES_PATH, "NP", "NP", "NP").add_recobro()


    def manejar_clic_boton_generar_pdf(self):
        """
        Handles the click event of the "Generate PDF" button.
        Generates a PDF report of the products using GeneradorPDF and displays a success message.
        """
        GeneradorPDF(consulta(config.GET_AVAILABLE_PRODUCTS_DETAILS), config.LOGO, config.PDF).generar_pdf()
        messagebox.showerror("PDF", "Product PDF generated.")
        print("Generate PDF button pressed")

    def manejar_clic_boton_actualizar_base_de_datos(self):
        """
        Handles the click event of the "Update Database" button.
        Updates the database with customer and product information, potentially involving cloud storage.
        The specifics of the update process are unclear without further context about 'txtformatobusqueda' and 'nube'.
        """
        format_and_save_query_results(consulta(config.SELECT_CUSTOMERS_BASIC_INFO), "ClientesA", ".txt")
        format_and_save_query_results(consulta(config.GET_AVAILABLE_PRODUCTS), "ProductosA", ".txt")

        #nube("ClientesA.txt", "ProductosA.txt")  # Interacts with cloud storage

    def handle_id_entry_enter(self, id_value):
        """
        Handles the Enter key press event in the ID entry field.
        Validates the input and, if it's a valid numeric ID, retrieves customer data using
        'data_customer()' and saves it to Excel using ExcelManager.

        Args:
            id_value (str): The value entered in the ID entry field.
        """
        if id_value.isdigit():
            lista = data_customer(id_value)
            if lista is not None:
                ExcelManager(config.EXCEL_PATH, config.TEST_SALES_PATH, "NP", "NP", lista).save_exel()
            else:
                messagebox.showerror("No.Doc", "Value out of range.")
        else:
            messagebox.showerror("Error", "Please enter only numbers in the ID field.")