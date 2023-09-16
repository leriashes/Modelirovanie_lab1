from app import app
from time import time
from flask import render_template, url_for , request, jsonify
import pandas as pd
import json
import plotly
import plotly.express as px

@app.route('/')
@app.route('/index')
@app.route('/nx2')
def index():

    start_values = []
    bad_values = []

    if request.is_json:
        cells = request.args.get('cells_values')

        i = 0

        cells_values = cells.split( '"},{"val":"')
        cells_values[0] = cells_values[0][9:len(cells_values[0])]
        cells_values[len(cells_values) - 1] = cells_values[len(cells_values) - 1][0:len(cells_values[len(cells_values) - 1]) - 3]


        #поиск ячеек с неудовлетворяющими значениями
        k = 2

        while i < len(cells_values):
            count = 0

            for j in range(len(cells_values[i])):
                if cells_values[i][j] >= '0' and cells_values[i][j] <= '9':
                    count += 1
                else:
                    break

            if count < len(cells_values[i]) or len(cells_values[i]) == 0 or len(cells_values[i]) == 1 and cells_values[i][0] == '0':
                bad_values.append(str(i))
            else:
                if (i % k) == 0:
                    start_values.append([i // k, int(cells_values[i]), int(cells_values[i + 1])])

            i += 1

        print(start_values)

        X = []
        sum_a = 0
        sum_b = 0
        sum_x = 0

        if (len(bad_values) == 0):
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
                    X.append(str(xs[i]))

                T = sum_x + sum_b

                return jsonify({'bad': (' ').join(bad_values), 'T': T, 'X': (' ').join(X)})

            elif (request.args.get('action') == 'find'):
                mas_a = []
                mas_b = []

                k = len(start_values)
                for i in range(k):
                    m = start_values[0][1]
                    row = 0
                    ind = 0
                    #print('ja тут: ', i, row, start_values)
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
                    X.append(str(xs[i]))

                T = sum_x + sum_b
                print(bad_values, T, X, res_str)
                print('tyt')

                return jsonify({'bad': (' ').join(bad_values), 'T': T, 'X': (' ').join(X), 'res': (' ').join(res_str)})
    else:
        return render_template("index.html", title = "2")

@app.route('/nx3')
def nx3():
    # Graph One
    df = pd.DataFrame([
    dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28'),
    dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15'),
    dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30')
])

    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task")
    fig.update_yaxes(autorange="reversed")

    graph1JSON = json.dumps(fig, cls =plotly.utils.PlotlyJSONEncoder)

    return render_template("index.html", title = "3", graph1JSON = graph1JSON)