from common import get_database

database = get_database()


class ValidationError(Exception):
    pass


class Model:
    def __init__(self, table_name, fields, _database=database):
        self._database = _database
        self.table_name = table_name
        self.fields = fields

    def insert(self, data):
        self.validate_data(data)
        conn = self._database.get_connection()
        with conn.cursor() as cursor:
            values = list(data.values())
            print(values)
            fields = ', '.join(self.fields)
            query = (f'INSERT INTO {self.table_name} ('
                     f'{fields}) VALUES({", ".join("%s" for _ in values)}) RETURNING id;')
            print(query)
            cursor.execute(query, values)
            conn.commit()
            return cursor.fetchone()['id']

    def validate_data(self, data):
        is_valid = all([
            len(data) == len(self.fields),
            all([field == key for field, key in zip(self.fields, data)])
        ])
        if not is_valid:
            raise ValidationError('data is not valid.')

    def select_all(self, fields=None):
        with self._database.get_connection().cursor() as cursor:
            fields = '*' if not fields else ', '.join(fields)
            query = f'SELECT {fields} from {self.table_name}'
            cursor.execute(query)
            return cursor.fetchall()


books_manager = Model(
    table_name='books',
    fields=['title', 'author_id', 'genre_id', 'stylistics_id',
            'pages_count', 'release_date', 'age_restrictions']
)

authors_manager = Model(
    table_name='authors',
    fields=['first_name', 'last_name', 'birth_date', 'country_id']
)

genres_manager = Model(
    table_name='genres',
    fields=['name']
)

stylistics_manager = Model(
    table_name='stylistics',
    fields=['name']
)

countries_manager = Model(
    table_name='countries',
    fields=['name']
)

persons_manager = Model(
    table_name='persons',
    fields=['first_name', 'last_name', 'age']
)
