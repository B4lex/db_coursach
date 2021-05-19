from flask import jsonify, Blueprint, request

from models import database, authors_manager, ValidationError

bp = Blueprint('main_routes', __name__, url_prefix='/api')


@bp.route('/db_cleanup')
def init_db():
    database.init_tables()
    return "DB initialized."


@bp.route("/books", methods=['GET', 'POST'])
def root_page():
    if request.method == 'GET':
        return jsonify(authors_manager.select_all())
    elif request.method == 'POST':
        author_data = request.json
        try:
            authors_manager.insert(author_data)
            return '', 204
        except ValidationError as e:
            return jsonify({'error': str(e)}), 400




