# Rutas de prueba (Test paths)
TEST_DATABASE_PATH = r"C:/UtilidadesSotfware/recursos/BDD/Database.accdb"  # Path to the test database
TEST_SALES_PATH = r"C:\UtilidadesSotfware\recursos\Vendedores"  # Path to the test sales folder - ¿Qué se almacena aquí? (What is stored here?)

# Otros archivos (Other files)
EXCEL_PATH = r"C:/UtilidadesSotfware/recursos/exel/Controldecredito.xlsx"  # Path to the Excel file for credit control
LOGO = r"C:/UtilidadesSotfware/recursos/Logo/example.png"  # Path to the logo image
PDF = r"C:/UtilidadesSotfware/recursos/pdf/Productos.pdf"  # Path to the product PDF


# Consultas SQL (SQL queries)
SELECT_CUSTOMERS_BASIC_INFO = """
SELECT Nombre,Direccion,Colonia,Telefono 
FROM Tbl_App_Clientes 
ORDER BY Nombre ASC
"""  # Query to get basic customer information

GET_AVAILABLE_PRODUCTS = """
SELECT Nombre,Costo,Existencia 
FROM Tbl_App_Productos 
WHERE Tbl_App_Productos.Existencia > 0 
ORDER BY Nombre ASC
"""  # Query to get available products

GET_AVAILABLE_PRODUCTS_DETAILS = """
SELECT Id,Nombre,Costo,Precio1,Existencia  
FROM Tbl_App_Productos 
WHERE Tbl_App_Productos.Existencia > 0 
ORDER BY Nombre ASC
"""  # Query to get details of available products

# Connection string for the Access database.
# Note: Consider storing the password in an environment variable for better security.
ACCESS_CONN_STR = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    fr'DBQ={TEST_DATABASE_PATH};'
    r'PWD=admin;'  # Replace with environment variable
)


