from psycopg2 import connect
from psycopg2.extras import RealDictConnection


class Database:

    def __init__(self, username, password, db_name, host='localhost', port=5432, schema_file='db_schema.sql'):
        self.__connection = connect(
            f'dbname={db_name} user={username} password={password} host={host} port={port}',
            connection_factory=RealDictConnection
        )
        self.schema_file = schema_file

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '__instance'):
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def init_tables(self):
        with open(self.schema_file, 'rt') as f:
            connection = self.get_connection()
            with connection.cursor() as curr:
                curr.execute(f.read())
                connection.commit()

    def get_connection(self):
        return self.__connection

    def __del__(self):
        self.__connection.close()
