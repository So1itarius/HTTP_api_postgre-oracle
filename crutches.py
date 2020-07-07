import re

from flask import abort



def json_converter(json):
    a = list(zip(*json.items()))
    return [str(a[0]).replace("'", "\"").replace(",)", ")"),
            str(a[1]).replace(",)", ")")]


def json_converter_2(json):
    a = ""
    for i in json.items():
        try:
            a = a + i[0] + " = " + "\'" + i[1] + "\'" + ", "
        except TypeError:
            a = a + i[0] + " = " + str(i[1]) + ", "

    return a[0:-2]


def id_searcher(column_list):
    for i in column_list:
        if re.search(r'id', i):
            return i


def process_id_verification(process_id, cursor, conn):
    # conn.autocommit = True
    cursor.execute('select process.process_id from "process"')
    a = list(filter(lambda row: row['process_id'] == process_id, cursor))
    if len(a) == 0:
        abort(404)
