from flask import jsonify, Blueprint, request

from common import get_404_response
from models import (database, authors_manager, books_manager, genres_manager,
                    stylistics_manager, countries_manager, persons_manager, ValidationError)


bp = Blueprint('main_routes', __name__, url_prefix='/api')


@bp.route('/db_cleanup')
def init_db():
    database.init_tables()
    return "DB initialized."


def get_api_view(manager):

    def generic_api_view():
        if request.method == 'GET':
            entity_id = request.args.get('id')
            data = manager.select(
                entity_id=entity_id,
            )

            if data or not entity_id:
                response = jsonify(data)
            else:
                response = get_404_response()
            return response
        elif request.method == 'POST':
            entity_data = request.json
            try:
                entity_id = manager.insert(entity_data)
                return jsonify(id=entity_id), 201
            except ValidationError as e:
                return jsonify({'error': str(e)}), 400
        elif request.method == 'DELETE':
            entity_id = request.args.get('id')
            if not entity_id:
                return jsonify(error='You should provide "id" url parameter.'), 400
            success = manager.delete(entity_id)
            if success:
                return '', 204
            else:
                return get_404_response()

    return generic_api_view


bp.add_url_rule(
    '/books', 'books', view_func=get_api_view(books_manager),
    methods=['GET', 'POST', 'DELETE', 'PATCH']
)
bp.add_url_rule(
    '/authors', 'authors', view_func=get_api_view(authors_manager),
    methods=['GET', 'POST', 'DELETE', 'PATCH']
)
bp.add_url_rule(
    '/genres', 'genres', view_func=get_api_view(genres_manager),
    methods=['GET', 'POST', 'DELETE', 'PATCH']
)
bp.add_url_rule(
    '/stylistics', 'stylistics', view_func=get_api_view(stylistics_manager),
    methods=['GET', 'POST', 'DELETE', 'PATCH']
)
bp.add_url_rule(
    '/countries', 'countries', view_func=get_api_view(countries_manager),
    methods=['GET', 'POST', 'DELETE', 'PATCH']
)
bp.add_url_rule(
    '/persons', 'persons', view_func=get_api_view(persons_manager),
    methods=['GET', 'POST', 'DELETE', 'PATCH']
)


# NVM about the following code)
@bp.route('/readers/books', methods=[''])
def reader_books():
    pass