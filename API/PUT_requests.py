from flask import Blueprint, request, abort

from crutches import json_converter_2


from oracledb import OracleProvider

blueprint = Blueprint('processes_put', __name__)

conn = OracleProvider().cursor


@blueprint.route('/api/v1.0/<scheme>/<table>{<column>=<any_key>}', methods=['PUT'])
# @auth.login_required
def update(table, scheme, column, any_key):
    if not request.json:
        abort(400)
    final_json = json_converter_2(request.json)
    conn.execute(f'UPDATE {scheme}."{table}" SET {final_json} WHERE {column} = {any_key}')
    return "Done!"
