from app import app
from time import time
from flask import render_template, url_for , request, jsonify
import pandas as pd
import json
import plotly
import plotly.express as px

def toStrArray(cells):

    cells_values = cells.split( '"},{"val":"')
    cells_values[0] = cells_values[0][9:len(cells_values[0])]
    cells_values[len(cells_values) - 1] = cells_values[len(cells_values) - 1][0:len(cells_values[len(cells_values) - 1]) - 3]

    return cells_values

def findBad(cells_values):
    bad_values = []
    i = 0

    #поиск ячеек с неудовлетворяющими значениями
    while i < len(cells_values):
        count = 0

        for j in range(len(cells_values[i])):
            if cells_values[i][j] >= '0' and cells_values[i][j] <= '9':
                count += 1
            else:
                break

        if count < len(cells_values[i]) or len(cells_values[i]) == 0 or len(cells_values[i]) == 1 and cells_values[i][0] == '0':
            bad_values.append(str(i))
            
        i += 1

    return bad_values

def JohnsonAlgorithm(start_values):
    mas_a = []
    mas_b = []

    k = len(start_values)
    for i in range(k):
        m = start_values[0][1]
        row = 0
        ind = 0
        for j in range(len(start_values)):
            for t in range(2):
                if (start_values[j][t + 1] < m):
                    m = start_values[j][t + 1]
                    row = j
                    ind = t
        
        if (ind == 0):
            mas_a.append(start_values[row])
        else:
            mas_b.append(start_values[row])

        start_values.pop(row)

    mas_b.reverse()
    result_values = mas_a + mas_b

    return result_values



@app.route('/')
@app.route('/index')
@app.route('/nx2')
def index():
    if request.is_json:
        cells_values = toStrArray(request.args.get('cells_values'))
        bad_values = findBad(cells_values)

        mas_x = []
        start_values = []
        sum_a = 0
        sum_b = 0
        sum_x = 0

        if (len(bad_values) == 0):

            for i in range(0, len(cells_values), 2):
                start_values.append([i // 2, int(cells_values[i]), int(cells_values[i + 1])])


            if (request.args.get('action') == 'draw'):
                xs = []

                for i in range(0, len(cells_values), 2):
                    #start_values.append([i // 2, int(cells_values[i]), int(cells_values[i + 1])])
                    sum_a += start_values[i // 2][1]
                    xs.append(max(sum_a - sum_x - sum_b, 0))
                    sum_x += xs[i // 2]
                    sum_b += start_values[i // 2][2]

                #print(len(cells_values), sum_a, sum_x, sum_b)
                for i in range(len(xs)):
                    mas_x.append(str(xs[i]))

                T = sum_x + sum_b

                return jsonify({'bad': (' ').join(bad_values), 'T': T, 'mas_x': (' ').join(mas_x)})

            elif (request.args.get('action') == 'find'):
                
                result_values = JohnsonAlgorithm(start_values)
                res_str = []

                for i in range(len(result_values)):
                    for j in range(3):
                        res_str.append(str(result_values[i][j] + 1 * (j == 0)))


                xs = []
                print(len(result_values))
                for i in range(len(result_values)):
                    sum_a += result_values[i][1]
                    xs.append(max(sum_a - sum_x - sum_b, 0))
                    sum_x += xs[i]
                    sum_b += result_values[i][2]

                print(len(cells_values), sum_a, sum_x, sum_b)
                for i in range(len(xs)):
                    mas_x.append(str(xs[i]))

                T = sum_x + sum_b
                print(bad_values, T, mas_x, res_str)
                print('tyt')

                return jsonify({'bad': (' ').join(bad_values), 'T': T, 'mas_x': (' ').join(mas_x), 'res': (' ').join(res_str)})
        return jsonify({'bad': (' ').join(bad_values)})
    else:
        return render_template("index.html", title = "Задача для 2 станков", type = 2)

@app.route('/nx3')
def nx3():

    if request.is_json:
        cells_values = toStrArray(request.args.get('cells_values'))
        bad_values = findBad(cells_values)

        mas_x = []
        mas_y = []
        start_values = []
        sum_a = 0
        sum_b = 0
        sum_c = 0
        sum_x = 0
        sum_y = 0

        if (len(bad_values) == 0):

            for i in range(0, len(cells_values), 3):
                start_values.append([i // 3, int(cells_values[i]), int(cells_values[i + 1]), int(cells_values[i + 2])])


            if (request.args.get('action') == 'draw'):
                xs = []
                ys = []

                for i in range(0, len(cells_values), 3):
                    #start_values.append([i // 2, int(cells_values[i]), int(cells_values[i + 1])])
                    sum_a += start_values[i // 3][1]
                    xs.append(max(sum_a - sum_x - sum_b, 0))
                    sum_x += xs[i // 3]
                    sum_b += start_values[i // 3][2]
                    ys.append(max(sum_x + sum_b - sum_y - sum_c, 0))
                    sum_y += ys[i // 3]
                    sum_c += start_values[i // 3][3]

                #print(len(cells_values), sum_a, sum_x, sum_b)
                for i in range(len(xs)):
                    mas_x.append(str(xs[i]))
                    mas_y.append(str(ys[i]))

                T = sum_y + sum_c

                return jsonify({'bad': (' ').join(bad_values), 'T': T, 'mas_x': (' ').join(mas_x), 'mas_y': (' ').join(mas_y)})

            elif (request.args.get('action') == 'find'):

                de_values = []

                for i in range(len(start_values)):
                    de_values.append([start_values[i][0], start_values[i][1] + start_values[i][2], start_values[i][2] + start_values[i][3]])

                result_values = JohnsonAlgorithm(de_values)
                
                res_str = []
                print('here we',result_values)
                for i in range(len(result_values)):
                    res_str.append(str(result_values[i][0] + 1))
                    for j in range(3):
                        res_str.append(str(start_values[result_values[i][0]][j + 1]))

                print(res_str)
                xs = []
                ys = []
                print(len(result_values))
                for i in range(len(result_values)):
                    print(1, sum_a, sum_b, sum_c, sum_x, sum_y)
                    sum_a += start_values[result_values[i][0]][1]
                    xs.append(max(sum_a - sum_x - sum_b, 0))
                    sum_x += xs[i]
                    sum_b += start_values[result_values[i][0]][2]
                    ys.append(max(sum_x + sum_b - sum_y - sum_c, 0))
                    sum_y += ys[i]
                    sum_c += start_values[result_values[i][0]][3]
                    print(2, sum_a, sum_b, sum_c, sum_x, sum_y)
                print(xs, ys)
                print(len(cells_values), sum_a, sum_x, sum_b)
                for i in range(len(xs)):
                    mas_x.append(str(xs[i]))
                    mas_y.append(str(ys[i]))

                T = sum_y + sum_c
                print(bad_values, T, mas_x, mas_y, res_str)
                print('tyt')

                return jsonify({'bad': (' ').join(bad_values), 'T': T, 'mas_x': (' ').join(mas_x), 'mas_y': (' ').join(mas_y), 'res': (' ').join(res_str)})
        return jsonify({'bad': (' ').join(bad_values)})
    else:
        return render_template("index.html", title = "Задача для 3 станков", type = 3)