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
