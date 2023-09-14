from app import app
from time import time
from flask import render_template, url_for , request, jsonify
import pandas as pd
import json
import plotly
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go

@app.route('/')
@app.route('/index')
@app.route('/nx2')
def index():

    if request.is_json:
        secs = time()
        print('yaas')

        cells = request.args.get('cells_values')

        i = 0

        cells_values = cells.split( '"},{"val":"')
        cells_values[0] = cells_values[0][9:len(cells_values[0])]
        cells_values[len(cells_values) - 1] = cells_values[len(cells_values) - 1][0:len(cells_values[len(cells_values) - 1]) - 3]
        print(cells_values)

        start_values = []
        bad_values = []


        while i < len(cells_values):
            count = 0

            for j in range(len(cells_values[i])):

                if cells_values[i][j] >= '0' and cells_values[i][j] <= '9':
                    count += 1
                else:
                    break

            if count < len(cells_values[i]) or len(cells_values[i]) == 0 or len(cells_values[i]) == 1 and cells_values[i][0] == '0':
                bad_values.append(str(i))
                    #cells[i].style.backgroundColor = "#ea9999";
            else:
                    #cells[i].style.backgroundColor = "#ffffff";
                start_values.append(int(cells_values[i]))

            i += 1
        
        print(start_values)
        print(bad_values)
        print((' ').join(bad_values))
        #request.args.get('button_text')
        return jsonify({'secs': secs, 'bad': (' ').join(bad_values)})
    else:
        print(request.args.get('button_text'))



    




    

    fig = go.Figure()

    fig.add_trace(go.Bar(
        y=['B', 'A'],
        x=[20, 14],
        name='1',
        orientation='h',
        width=0.5,
        marker=dict(
            color='rgba(246, 78, 139, 0.6)',
            line=dict(color='rgba(246, 78, 139, 1.0)', width=2)
        )
    ))

    fig.add_trace(go.Bar(
        y=['B', 'A'],
        x=[13, 11],
        name='2',
        orientation='h',
        width=0.5,
        marker=dict(
            color='rgba(58, 91, 80, 0.6)',
            line=dict(color='rgba(58, 91, 80, 1.0)', width=2)
        ),
    ))

    fig.add_trace(go.Bar(
        y=['B', 'A'],
        x=[12, 18],
        name='2',
        orientation='h',
        width=0.5,
        marker=dict(
            color='rgba(58, 71, 80, 0.6)',
            line=dict(color='rgba(58, 71, 80, 1.0)', width=2)
        ),
    ))

    
    

    fig.update_layout(barmode='stack', legend_traceorder='normal')


    graph1JSON = json.dumps(fig, cls =plotly.utils.PlotlyJSONEncoder)

    return render_template("index.html", title = "2", graph1JSON = graph1JSON)
    #return "Hello, World! It's Le6raaa!!!"

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