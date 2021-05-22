import configparser

from flask import jsonify

from db import Database


def get_database():
    config = configparser.ConfigParser()
    config.read('config.ini')

    db_config = config['Database']

    db_user = db_config['username']
    db_password = db_config['password']
    db_host = db_config['host']
    db_port = db_config['port']
    db_name = db_config['db_name']

    return Database(db_user, db_password, db_name, db_host, db_port)


def get_404_response():
    return jsonify(error='Object does not exist.'), 404
