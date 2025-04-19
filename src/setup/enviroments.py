import os
import dotenv

dotenv.load_dotenv()

DB1 = {     
        "host": os.environ['DB_HOST'],
        "user": os.environ['MYSQL_USER'],
        "password": os.environ['MYSQL_PASSWORD'],
        "database": os.environ['MYSQL_DATABASE'],
        "port": os.environ['DB_PORT']
}

DB2 = {     
        "host": os.environ['DB_HOST'],
        "user": os.environ['MYSQL_USER_DB2'],
        "password": os.environ['MYSQL_PASSWORD_DB2'],
        "database": os.environ['MYSQL_DATABASE_SITE'],
        "port": os.environ['DB_PORT']
}