from fpdf import FPDF
import pyodbc
import re

class GeneradorPDF:
    """
    Clase para generar un PDF con información de productos desde una base de datos Access.
    """

    def __init__(self, crsr, ruta_imagen, ruta_salida):
        """
        Inicializa la clase con la ruta de la base de datos, la ruta de la imagen del logo
        y la ruta del archivo PDF de salida.
        """
        self.crsr = crsr
        self.ruta_imagen = ruta_imagen
        self.ruta_salida = ruta_salida

    def generar_pdf(self):
        """
        Genera el PDF con la información de los productos.
        """
        print("si entro a la funcion")
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.alias_nb_pages()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 12)
        pdf.image(self.ruta_imagen, x=50, y=1, w=0, h=40)
        pdf.ln(32)

        # Encabezados de la tabla
        pdf.cell(w=20, h=15, txt='Código', border=1, align='C', fill=0)
        pdf.cell(w=100, h=15, txt='Producto', border=1, align='C', fill=0)
        pdf.cell(w=18, h=15, txt='Costo', border=1, align='C', fill=0)
        pdf.cell(w=18, h=15, txt='Precio 1', border=1, align='C', fill=0)
        pdf.multi_cell(w=0, h=15, txt='Existencia', border=1, align='C', fill=0)

        # Iterar por los resultados
        for fila in self.crsr.fetchall():
            pdf.set_font('Arial', '', 10)

            lista = list(fila)
            lista[1] = str(lista[1]).lstrip(' ').strip(' ')  # Eliminar espacios en blanco

            pdf.cell(w=20, h=7, txt=str(lista[0]), border=1, align='C', fill=0)
            pdf.cell(w=100, h=7, txt=lista[1], border=1, align='C', fill=0)
            pdf.cell(w=18, h=7, txt='$' + str(lista[2]), border=1, align='C', fill=0)
            pdf.cell(w=18, h=7, txt='$' + str(lista[3]), border=1, align='C', fill=0)
            pdf.multi_cell(w=0, h=7, txt=str(lista[4]), border=1, align='C', fill=0)

        pdf.output(self.ruta_salida)
        print(f"PDF Generado: {self.ruta_salida}")