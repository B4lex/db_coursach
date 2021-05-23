from common import get_database

database = get_database()


class ValidationError(Exception):
    pass


class GenericModel:
    def __init__(self, table_name, fields, fk_related_fields=None, m2m_related_fields=None):
        self._database = database
        self.table_name = table_name
        self.fields = fields
        self.fk_related_fields = fk_related_fields if fk_related_fields else dict()
        self.m2m_related_fields = m2m_related_fields if m2m_related_fields else dict()

    def validate_data(self, data):
        is_valid = all([
            len(data) == len(self.fields),
            all([field == key for field, key in zip(self.fields, data)])
        ])
        if not is_valid:
            raise ValidationError('data is not valid.')

    def insert(self, data):
        self.validate_data(data)
        conn = self._database.get_connection()
        values = list(data.values())
        fields = ', '.join(self.fields)
        query = (f'INSERT INTO {self.table_name} ('
                 f'{fields}) VALUES({", ".join("%s" for _ in values)})'
                 f'ON CONFLICT DO NOTHING RETURNING id')
        with self._database.get_connection().cursor() as cursor:
            cursor.execute(query, values)
            conn.commit()
            return cursor.fetchone()['id']

    def select(self, entity_id=None, fields=None):
        fields = '*' if not fields else ', '.join(fields)
        query = f'SELECT {fields} from {self.table_name}'
        if entity_id:
            query += f' WHERE id = {entity_id}'

        with self._database.get_connection().cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    def delete(self, entity_id):
        query = f'DELETE FROM {self.table_name} WHERE id = {entity_id} ON CONFLICT DO NOTHING'
        with self._database.get_connection().cursor() as cursor:
            cursor.execute(query)
            if cursor.rowcount > 0:
                return True
            else:
                return False

    def update(self, entity_id, data):
        self.validate_data(data)
        update_query = ', '.join([f'{field} = {value}' for field, value in data.items()])
        query = f'UPDATE {self.table_name} SET {update_query} WHERE id = {entity_id}'
        with self._database.get_connection().cursor() as cursor:
            cursor.execute(query)
            if cursor.rowcount > 0:
                return True
            else:
                return False


books_manager = GenericModel(
    table_name='books',
    fields=['title', 'description', 'author_id', 'genre_id', 'stylistics_id',
            'pages_count', 'release_date', 'age_restrictions'],
    fk_related_fields={
        'authors': 'author_id',
        'genres': 'genre_id',
        'stylistics': 'stylistics_id'
    },
    m2m_related_fields=[
        {
            'm2m_table': 'person_has_book',
            'self_field': 'book_id',
            'related_table': 'persons',
            'related_field': 'person_id'
        }
    ]
)

authors_manager = GenericModel(
    table_name='authors',
    fields=['first_name', 'last_name', 'birth_date', 'country_id'],
    fk_related_fields={
        'countries': 'country_id'
    }
)

genres_manager = GenericModel(
    table_name='genres',
    fields=['name']
)

stylistics_manager = GenericModel(
    table_name='stylistics',
    fields=['name']
)

countries_manager = GenericModel(
    table_name='countries',
    fields=['name']
)

persons_manager = GenericModel(
    table_name='persons',
    fields=['first_name', 'last_name', 'age'],
    m2m_related_fields=[
        {
            'm2m_table': 'person_has_book',
            'self_field': 'person_id',
            'related_table': 'books',
            'related_field': 'book_id'
        }
    ]
)
