import psycopg2
from flask import Blueprint, jsonify, abort
from psycopg2.extras import DictCursor


from config import DBNAME, USER, PASSWORD, HOST, PORT

blueprint = Blueprint('processes_get', __name__)

conn = psycopg2.connect(dbname=DBNAME,
                        user=USER,
                        password=PASSWORD,
                        host=HOST,
                        port=PORT)


@blueprint.route('/api/v1.0/processes', methods=['GET'])
def get_processes(conn=conn):
    processes = []
    # with closing(conn) as conn:
    with conn.cursor() as cursor:
        cursor.execute('select * from "process"')
        for row in cursor:
            processes.append({'executor_id': row[0],
                              'process_id': row[1],
                              'process_name': row[2],
                              'description': row[3],
                              'activity_flag': row[4]})

    return jsonify({'processes': processes})


@blueprint.route('/api/v1.0/processes/<int:id>', methods=['GET'])
def get_process(id):
    with conn.cursor(cursor_factory=DictCursor) as cursor:
        conn.autocommit = True
        cursor.execute(f'select * from "process"')
        a = list(filter(lambda row: row['process_id'] == id, cursor))
        if len(a) == 0:
            abort(404)
    return jsonify({'process': {'executor_id': a[0][0],
                                'process_id': a[0][1],
                                'process_name': a[0][2],
                                'description': a[0][3],
                                'activity_flag': a[0][4]}})
