from flask import Flask
from views import bp


app = Flask(__name__)
app.register_blueprint(bp)

app.config['JSON_AS_ASCII'] = False


if __name__ == '__main__':
    app.run()
