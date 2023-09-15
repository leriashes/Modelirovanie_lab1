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
                start_values.append(int(cells_values[i]))

            i += 1


        x_start = []
        sum_a = 0
        sum_b = 0
        sum_x = 0


        T = sum_x + sum_b

        if (len(bad_values) == 0):
            xs = []

            for i in range(0, len(cells_values), 2):
                sum_a += int(cells_values[i])
                xs.append(max(sum_a - sum_x - sum_b, 0))
                sum_x += xs[i // 2]
                sum_b += int(cells_values[i + 1])

            print(len(cells_values), sum_a, sum_x, sum_b)
            for i in range(len(xs)):
                x_start.append(str(xs[i]))

        return jsonify({'bad': (' ').join(bad_values), 'T': T, 'x_start': (' ').join(x_start)})
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