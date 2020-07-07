from flask import Flask, jsonify, make_response

from API.GET_requests import blueprint as GET_blueprint
from API.POST_requests import blueprint as POST_blueprint
from API.PUT_requests import blueprint as PUT_blueprint
from API.DELETE_requests import blueprint as DELETE_blueprint

app = Flask(__name__)

app.register_blueprint(GET_blueprint)
app.register_blueprint(POST_blueprint)
app.register_blueprint(PUT_blueprint)
app.register_blueprint(DELETE_blueprint)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
