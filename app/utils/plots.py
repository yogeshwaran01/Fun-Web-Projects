import pygal
from pygal.style import Style

def pie_chart(list_of_tuple: list, title):
    pie = pygal.Pie()
    pie.title = title
    for data in list_of_tuple:
        pie.add(data[0], data[1])

    return pie.render_response()
