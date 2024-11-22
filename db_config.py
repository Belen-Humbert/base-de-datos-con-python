from pymongo import MongoClient
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

# Configuración de MongoDB
def get_mongo_connection():
    mongo_uri = os.getenv("MONGO_URI", "mongodb://root:password@localhost:27017/")
    client = MongoClient(mongo_uri)
    db = client["Escuela"]  # Conexión a la base de datos "escuela"
    return db

# Configuración de MySQL
def get_mysql_connection():
    db_connection = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        port=os.getenv("MYSQL_PORT", 3306),  
        user=os.getenv("MYSQL_USER", "root"),  
        password=os.getenv("MYSQL_PASSWORD", "37512956"),  
        database=os.getenv("MYSQL_DB", "distributed_db")  
    )
    return db_connection