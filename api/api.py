import pandas as pd
from flask import Flask, jsonify, request
from shsexam.shs import *
from flask_cors import CORS
from dashboard.dashboard import *
import plotly
import plotly.graph_objects as go
import json
app = Flask(__name__)
CORS(app)

@app.route('/allgraphs', methods=['GET', 'PUT'])
def allgraphs():
    data = total_students()
    graph_11_male_female = bar_graph_11_male_female()
    graph_12_male_female = bar_graph_12_male_female()
    graph_11_12 = pie_chart_11_12_students()
    strand = pie_by_strand()
    grouped = strand_grouped_gender()
    region = line_chart_by_region() 
    sector = total_by_sector()
    sectorchart = line_sector_chart()
    return {
        "data": data,
        "graph_11_male_female": graph_11_male_female,
        "graph_12_male_female": graph_12_male_female,
        "graph_11_12": graph_11_12,
        "strand": strand,
        "grouped": grouped,
        "region": region,
        "sector": sector,
        "sectorchart" : sectorchart
    }
# @app.route('/totalstudentsbystrandgenderandtotal', methods=['GET'])
# def totalstudentsbystrandgenderandtotal():
#     strand = pie_by_strand()
#     grouped = strand_grouped_gender()
#     return {
#         "strand": strand,
#         "grouped": grouped
#     }

# @app.route('/totaleachregion', methods=['GET', 'PUT'])
# def totaleachregion():
#     region = total_each_region() 
#     return jsonify(region)

# @app.route('/totaleachregionbyyear', methods=['GET', 'PUT'])
# def totaleachregionbyyear():
#     region = line_chart_by_region() 
#     return jsonify(region)

# @app.route('/totalbtyector', methods=['GET', 'PUT'])
# def totalbtyector():
#     sector = total_by_sector() 
#     return jsonify(sector)

# @app.route('/totalbtyectorandyear', methods=['GET', 'PUT'])
# def totalbtyectorandyear():
#     sector = total_by_year_and_sector() 
#     return jsonify(sector)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)