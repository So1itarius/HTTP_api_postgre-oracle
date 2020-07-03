from flask import Blueprint, jsonify, abort, request

from oracledb import OracleProvider

blueprint = Blueprint('processes_get', __name__)

conn = OracleProvider().cursor


@blueprint.route('/api/v1.0/<scheme>/<table>', methods=['GET'])
def get_processes(table, scheme):
    if not request.json:
        abort(400)
    processes = []
    conn.execute(f'select * from {scheme}."{table}" FETCH FIRST 100 ROWS ONLY')
    for row in conn:
        processes.append({f'{j[0]}': i for i, j in zip(row, conn.description)})

    return jsonify({'processes': processes})

# непонятен принцип формирования http строки
@blueprint.route('/api/v1.0/<scheme>/<table>{<column>:[<any_key>]}', methods=['GET'])
def get_process(table, scheme, column, any_key):
    if not request.json:
        abort(400)
    processes = []
    conn.execute(f'select * from {scheme}."{table}" where {column}=\'{any_key}\' FETCH FIRST 100 ROWS ONLY')
    for row in conn:
        processes.append({f'{j[0]}': i for i, j in zip(row, conn.description)})

    return jsonify({'processes': processes})
