from flask import Blueprint

from oracledb import OracleProvider

blueprint = Blueprint('processes_delete', __name__)

conn = OracleProvider().cursor


@blueprint.route('/api/v1.0/<scheme>/<table>{<column>=<any_key>}', methods=['DELETE'])
# @auth.login_required
def delete(table, scheme, column, any_key):
    conn.execute(f'DELETE FROM {scheme}."{table}" WHERE {column} = {any_key}')
    return "Done!"
