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

    secs = 345
    if request.is_json:
        secs = time()
        #request.args.get('button_text')
        return jsonify({'secs': secs})
    

    # Graph One
    df = pd.DataFrame([
    dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28'),
    dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15'),
    dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30')
])

    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task")
    fig.update_yaxes(autorange="reversed")

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