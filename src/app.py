from flask import Flask, Blueprint


app = Flask(__name__)

api_bp = Blueprint('api', __name__, url_prefix='/api')


@api_bp.route("/")
def root_page():
    return "<h1></h1>"


if __name__ == '__main__':
    app.run()