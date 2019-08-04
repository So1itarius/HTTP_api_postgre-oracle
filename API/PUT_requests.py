import psycopg2
from flask import Blueprint, request, abort
from psycopg2.extras import DictCursor

from Basic_HTTP_authentication import auth
from config import DBNAME, USER, PASSWORD, HOST, PORT
from crutches import id_searcher, json_converter_2, process_id_verification
from testSQL3 import sql

blueprint = Blueprint('processes_put', __name__)

conn = psycopg2.connect(dbname=DBNAME,
                        user=USER,
                        password=PASSWORD,
                        host=HOST,
                        port=PORT)


@blueprint.route('/api/v1.0/processes/<int:process_id>/<table_name>/upd', methods=['PUT'])
# @auth.login_required
def update(process_id, table_name):
    with conn.cursor(cursor_factory=DictCursor) as cursor:
        process_id_verification(process_id, cursor, conn)
        if not request.json:
            abort(400)
        id = 'process_id'
        if table_name != 'process':
            cursor.execute(f'select * from "{table_name}"')
            column_names = [desc[0] for desc in cursor.description]
            a = list(filter(lambda row: row[id_searcher(column_names)] == process_id, cursor))
            if len(a) == 0:
                abort(404)
            if not request.json:
                abort(400)
            id = id_searcher(column_names)
        final_json = json_converter_2(request.json)
        update = sql.SQL(f'UPDATE {table_name} SET {final_json} WHERE {id} = {process_id}')
        cursor.execute(update)

    return "Done!"
