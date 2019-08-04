import psycopg2
from flask import Blueprint, request, abort
from psycopg2 import sql
from psycopg2.extras import DictCursor

from Basic_HTTP_authentication import auth

from config import DBNAME, USER, PASSWORD, HOST, PORT
from crutches import json_converter, id_searcher, process_id_verification

blueprint = Blueprint('processes_post', __name__)

conn = psycopg2.connect(dbname=DBNAME,
                        user=USER,
                        password=PASSWORD,
                        host=HOST,
                        port=PORT)


@blueprint.route('/api/v1.0/processes', methods=['POST'])
# @auth.login_required
def add_process():
    if not request.json:
        abort(400)
    final_json = json_converter(request.json)
    with conn.cursor() as cursor:
        conn.autocommit = True
        insert = sql.SQL(f'INSERT INTO "process" {final_json[0]} VALUES {final_json[1]}')
        cursor.execute(insert)
    return 'Done!', 201


@blueprint.route('/api/v1.0/processes/<int:process_id>/<table_name>', methods=['POST'])
# @auth.login_required
def insert(process_id, table_name):
    with conn.cursor(cursor_factory=DictCursor) as cursor:
        process_id_verification(process_id, cursor, conn)
        if not request.json:
            abort(400)
        if table_name != 'process_executor':
            cursor.execute(f'select * from "{table_name}"')
            column_names = [desc[0] for desc in cursor.description]
            request.json[id_searcher(column_names)] = process_id
        final_json = json_converter(request.json)
        insert = sql.SQL(f'INSERT INTO {table_name} {final_json[0]} VALUES {final_json[1]}')
        cursor.execute(insert)
    return 'Done!', 201
