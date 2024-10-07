import pyodbc
import config


def consulta(intrucciones):
    """
    Executes an SQL query on an Access database and returns the cursor.

    Args:
        intrucciones (str): The SQL query to execute.

    Returns:
        pyodbc.Cursor: The cursor of the query result.
    """

    try:
        conn_str = (config.ACCESS_CONN_STR)
        cnxn = pyodbc.connect(conn_str)
        crsr = cnxn.execute(intrucciones)
        return crsr
    except pyodbc.Error as ex:
        print(f"Error connecting to database: {ex}")
        return None


def query_database(sql_instructions,doc):  # Added default value for data
    """
    Performs a query to the database using the global connection.

    Args:
        sql_instructions (str): The SQL query to execute.
        data (tuple, optional): Data to be passed to the query. Defaults to None.

    Returns:
        pyodbc.Cursor: The cursor of the query result.
    """
    try:
        # Global connection to the database (created only once at the start of the application)
        conn_str = (config.ACCESS_CONN_STR)
        cnxn = pyodbc.connect(conn_str)
        crsr = cnxn.cursor()
        return crsr.execute(sql_instructions, doc)
    except pyodbc.Error as e:
        print(f"Error querying database: {e}")
        # You can add additional logic to handle the error, such as logging it or showing it to the user.


def data_customer(id):
    """
    Retrieves and processes customer information from the database.

    Args:
        id (str): The document or search criteria for the query.

    Returns:
        list: A list with the customer data if results are found,
              or None if no matching record is found.
    """

    lis_data = []  # List to store customer data

    # Perform the first query to the Tbl_App_Credito table
    query = query_database(
        "SELECT Documento, Cantidad, Fecha, FechaVencimiento, Saldo, Cliente FROM Tbl_App_Credito WHERE Documento=?;",
        id)  # Pass id as a tuple

    try:
        # Fetch the first result from the query
        query_tbl_app_credito = query.fetchone()
        if query_tbl_app_credito:
            query_tbl_app_credito = list(query_tbl_app_credito)  # Convert to list

            # Perform the second query to the Tbl_App_Clientes table using the customer ID obtained in the first query
            query = query_database("SELECT Nombre, Vendedor FROM Tbl_App_Clientes WHERE Id=?;",
                                   query_tbl_app_credito[5])  # Pass id as a tuple

            # Fetch the first result from the second query
            query_tbl_app_clientes = query.fetchone()
            if query_tbl_app_clientes:
                query_tbl_app_clientes = list(query_tbl_app_clientes)  # Convert to list

                # Add data to the 'lis_data' list
                lis_data.append(query_tbl_app_credito[4])  # Saldo (Balance)
                # lis_data.append(query_tbl_app_credito[1])  # Cantidad (Quantity) (commented, not currently used)
                lis_data.append(query_tbl_app_clientes[0])  # Nombre cliente (Customer name)
                lis_data.append(query_tbl_app_credito[2])  # Fecha (Date)
                lis_data.append(query_tbl_app_credito[3])  # Fecha final (End date)
                lis_data.append(query_tbl_app_credito[0])  # No.Doc (Document number)

                # Determine the assigned salesperson based on the value of 'Vendedor' (Salesperson) in the second query
                if query_tbl_app_clientes[1] == 1:
                    lis_data.append("M")
                elif query_tbl_app_clientes[1] == 6:
                    lis_data.append("R")
                elif query_tbl_app_clientes[1] == 10:
                    lis_data.append("J")
                else:
                    lis_data.append(".")

                return lis_data  # Return the list with the customer data

        # If no results are found in either query
        return None

    except Exception as e:
        print(f"Error querying database: {e}")
        return None