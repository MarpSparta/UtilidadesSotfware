import os
import shutil
from datetime import datetime
import pyodbc

def create_directory(path):
    """Creates a directory at the specified path."""
    try:
        os.makedirs(path, exist_ok=True)  # exist_ok=True prevents error if directory exists
        return True  # Indicates success
    except OSError as e:
        print(f"Error creating directory: {e}")  # Print the error for debugging
        return False  # Indicates failure


def list_directories(path):
    """Lists the directories at the specified path."""
    try:
        return os.listdir(path)
    except OSError as e:
        print(f"Error listing directories: {e}")  # Print the error for debugging
        return []  # Or raise an exception


def list_folders(path):  # Renamed from 'listar_carpetas'
    """Lists the names of the folders within the specified directory."""
    try:
        return [item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item))]
    except OSError as e:
        print(f"Error listing folders: {e}")  # Print the error for debugging
        return []


def delete_directory(path):
    """Deletes the directory at the specified path."""
    try:
        shutil.rmtree(path)
        return True  # Indicates success
    except OSError as e:
        print(f"Error deleting directory: {e}")  # Print the error for debugging
        return False  # Indicates failure


def get_formatted_date_spanish(): # This function is not used in the provided code
    """
    Returns the current date and time formatted in Spanish.
    Example: 'Miércoles-04-10-2024_Hora_03.43.20_PM'
    """
    fecha_actual = datetime.now()
    dia = fecha_actual.strftime("%A").capitalize()
    dias_semana = {
        "Monday": "Lunes",
        "Tuesday": "Martes",
        "Wednesday": "Miércoles",
        "Thursday": "Jueves",
        "Friday": "Viernes",
        "Saturday": "Sábado",
        "Sunday": "Domingo"
    }
    dia_semana_espanol = dias_semana[dia]
    fecha_formateada = fecha_actual.strftime(dia_semana_espanol + "-%d-%m-%Y_Hora_%I.%M.%S_%p")
    return fecha_formateada


def format_and_save_query_results(data, filename, extension):
    """
    Formats data from a database query and saves it to a text file.

    Args:
        data (pyodbc.Cursor): The cursor with the query results.
        filename (str): The name of the output file.
        extension (str): The extension of the output file.
    """
    try:
        with open(filename + extension, 'w', encoding="utf-8") as f:
            for row in data.fetchall():
                formatted_row = []
                for item in row:
                    if item is None or item == "":
                        formatted_row.append("NR")
                    elif isinstance(item, str):
                        formatted_row.append(item.replace(",", ".").strip().upper())
                    else:
                        formatted_row.append(item)  # Keep non-string items as they are

                output_string = str(formatted_row).replace("'", "").replace(", ", ",")
                output_string = " ".join(output_string.split())  # Remove extra spaces
                output_string = output_string.replace("[", "").replace("]", "")
                f.write(output_string + "\n")
    except Exception as e:
        print(f"Error formatting and saving query results: {e}")