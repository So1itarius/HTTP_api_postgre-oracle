import psycopg2
from flask import Blueprint, abort
from psycopg2 import sql
from psycopg2.extras import DictCursor

from Basic_HTTP_authentication import auth
from config import DBNAME, USER, PASSWORD, HOST, PORT
from crutches import id_searcher, process_id_verification

blueprint = Blueprint('processes_delete', __name__)

conn = psycopg2.connect(dbname=DBNAME,
                        user=USER,
                        password=PASSWORD,
                        host=HOST,
                        port=PORT)


@blueprint.route('/api/v1.0/processes/<int:process_id>/<table_name>/del', methods=['DELETE'])
# @auth.login_required
def delete(process_id, table_name):
    with conn.cursor(cursor_factory=DictCursor) as cursor:
        process_id_verification(process_id, cursor, conn)

        id = 'process_id'
        if table_name != 'process':
            cursor.execute(f'select * from "{table_name}"')
            column_names = [desc[0] for desc in cursor.description]
            a = list(filter(lambda row: row[id_searcher(column_names)] == process_id, cursor))
            if len(a) == 0:
                abort(404)
            id = id_searcher(column_names)

        delete = sql.SQL(f'DELETE FROM {table_name} WHERE {id} = {process_id}')
        cursor.execute(delete)

    return "Done!"
