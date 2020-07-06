from flask import Blueprint, request, abort

from crutches import json_converter
from oracledb import OracleProvider

blueprint = Blueprint('processes_post', __name__)

conn = OracleProvider().cursor


@blueprint.route('/api/v1.0/<scheme>/<table>', methods=['POST'])
# @auth.login_required
def insert(table, scheme):
    if not request.json:
        abort(400)
    final_json = json_converter(request.json)
    conn.execute(f'INSERT INTO {scheme}."{table}" {final_json[0]} VALUES {final_json[1]}')

    return 'Done!', 201
