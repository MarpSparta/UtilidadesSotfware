from ..models.ExcelManager import ExcelManager
from ..utils.file_helpers import get_formatted_date_spanish,create_directory
import config

class SellerListController:

    def __init__(self, vista):
        self.vista = vista

    def guardar_valor_lista(self, valor):
        fecha_español = get_formatted_date_spanish()

        ExcelManager(config.EXCEL_PATH,config.TEST_SALES_PATH,
                     valor,
                     fecha_español,
                     "NP").create_new_excel()

        print("Valor guardado en el controlador:", valor)



    def guardar_valor_textbox(self,nombre):

        path = config.TEST_SALES_PATH + fr"\{nombre}"
        create_directory(path)
        print("Valor guardado en el controlador:", path)
