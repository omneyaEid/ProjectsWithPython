from flask import Flask, render_template, request
from model import *
import numpy as np
from joblib import load
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import uuid

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    request_type_str = request.method
    if request_type_str == 'GET':
        return render_template('index.html', href='static/base_pic.svg')

    text = request.form['text']
    random_string = uuid.uuid4().hex
    path = "static/" + random_string + ".svg"
    model = load('model.joblib')
    np_arr = floats_string_to_np_arr(text)
    make_picture('AgesAndHeights.pkl', model, np_arr, path)
    return render_template('index.html', href=path)
