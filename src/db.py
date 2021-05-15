from psycopg2 import connect
from psycopg2.extras import DictConnection 


class Database:

    def __init__(self, username, password, db_name, host='localhost', port=5432):
        self.__connection = connect(
            f'db_name={db_name} user={username} password={password} host={host} port={port}',
            connection_factory=DictConnection
        )

    def __new__(cls):
        if not hasattr(cls.__instance, '__instance'):
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def get_connection(self):
        return self.__connection

    def select_all(self, fields=None):
        with self.__connection.cursor() as cursor:
            cursor.execute('SELECT {} FROM books'.format(', '.join(fields) if fields else '*'))
            return cursor.fetchall()
 
    def __del__(self):
        self.__connection.close()


database = Database()
