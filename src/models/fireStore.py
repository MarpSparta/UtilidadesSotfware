
import firebase_admin
from google.cloud import storage
from firebase_admin import credentials, initialize_app, storage

def nube(fileName,fileName2):


    cred = credentials.Certificate("clave.json")
    initialize_app(cred,{'storageBucket':'basededatos117-597e4.appspot.com'})

    # Put your local file path

    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

    # Opt : if you want to make public access from theRL
    blob.make_public()

    print("SUBIENDO ARCHIVO CLIENTES.......")
    print()
    print("ARCHIVO CLIENTES SUBIDO CON EXITO")



    # Put your local file path

    bucket = storage.bucket()
    blob = bucket.blob(fileName2)
    blob.upload_from_filename(fileName2)

    # Opt : if you want to make public access from the URL
    blob.make_public()
    print()
    print()
    print("SUBIENDO ARCHIVO PRODUCTOS.......")
    print()
    print("ARCHIVO PRODUCTOS SUBIDO CON EXITO")

