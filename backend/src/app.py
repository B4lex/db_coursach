from flask import Flask
from flask_cors import CORS

from views import bp


app = Flask(__name__)
app.register_blueprint(bp)
CORS(app)

app.config['JSON_AS_ASCII'] = False


if __name__ == '__main__':
    app.run()
