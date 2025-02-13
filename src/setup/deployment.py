import dotenv
import os


dotenv.load_dotenv()

DB_ERP = {
        "host":os.environ['DB_HOST'],
        "user":os.environ['MYSQL_USER'],
        "password":os.environ['MYSQL_PASSWORD'],
        "database":os.environ['MYSQL_DATABASE'],
        "port":os.environ['DB_PORT'],
    }
# print(DB_ERP)