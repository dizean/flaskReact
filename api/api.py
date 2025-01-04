import pandas as pd
from flask import Flask, jsonify, request
from shsexam.shs import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load CSV data once when the server starts
def load_data():
    try:
        df = pd.read_csv("FSHS.csv")
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        df = None  # Set df to None if there's an error
    return df

df = load_data()


@app.route('/totalbyStrandEachRegion', methods=['GET', 'PUT'])
def totalStrand():
    if df is None:
        return jsonify({"error": "Data not loaded"}), 500  # Return an error if data isn't loaded

    print("Endpoint /get-plot accessed")
    
    if request.method == 'GET':
        print("Handling GET request")
        regIndex, secIndex, gradegenIndex, html_content = totalbyStrandEachRegion(df)
        return jsonify({
            "regions": regIndex,
            "sectors": secIndex,
            "gradeGender": gradegenIndex,
            'plotHTML': html_content,
        })
    
    elif request.method == 'PUT':
        print("Handling PUT request")
        data = request.get_json()
        regionIndex = data.get('regIndex', 0)
        sectorIndex = data.get('secIndex', 0)
        gradegenderIndex = data.get('gradegenIndex', 0)

        # Update plot based on new indices
        regIndex, secIndex, gradegenIndex, html_content = totalbyStrandEachRegion(df, regionIndex, sectorIndex, gradegenderIndex)

        return jsonify({
            "message": "Indices updated",
            "regions": regIndex,
            "sectors": secIndex,
            "gender": gradegenIndex,
            "updatedRegIndex": regionIndex,
            "updatedSecIndex": sectorIndex,
            "updatedGradeGenIndex": gradegenderIndex,
            "updatedPlot": html_content
        })

@app.route('/totalStudentsbySector', methods=['GET', 'PUT'])
def totalStudentsSector():
    if df is None:
        return jsonify({"error": "Data not loaded"}), 500  # Return an error if data isn't loaded

    print("Endpoint /get-plot accessed")
    
    if request.method == 'GET':
        print("Handling GET request")
        regIndex, yrIndex, gendIndex, html_content= totalStudentsbySector(df)
        return jsonify({
            "regions": regIndex,
            "years": yrIndex,
            "genders": gendIndex,
            'plotHTML': html_content,
        })
    
    elif request.method == 'PUT':
        print("Handling PUT request")
        data = request.get_json()
        regionIndex = data.get('regIndex', 0)
        genderIndex = data.get('genIndex', 0)
        yearIndex = data.get('yearIndex', 0)

        # Update plot based on new indices
        regIndex, yrIndex, gendIndex,html_content  = totalStudentsbySector(df, regionIndex, yearIndex,genderIndex )
# 
        return jsonify({
            "message": "Indices updated",
            "regions": regIndex,
            "sectors": yrIndex,
            "gender": gendIndex,
            "updatedRegIndex": regionIndex,
            "updatedGenderIndex": genderIndex,
            "updatedYearIndex": yearIndex,
            "updatedPlot": html_content
        })  
@app.route('/totalStudentsbyRegion', methods=['GET', 'PUT'])
def totalStudentsRegion():
    if df is None:
        return jsonify({"error": "Data not loaded"}), 500  # Return an error if data isn't loaded

    print("Endpoint /get-plot accessed")
    
    if request.method == 'GET':
        print("Handling GET request")
        yrIndex,html_content= totalStudentsbyRegion(df)
        return jsonify({
            "years": yrIndex,
            'plotHTML': html_content,
        })
    
    elif request.method == 'PUT':
        print("Handling PUT request")
        data = request.get_json()
        yearIndex = data.get('yearIndex', 0)

        # Update plot based on new indices
        yrIndex ,html_content  = totalStudentsbyRegion(df, yearIndex )
# 
        return jsonify({
            "message": "Indices updated",
            "sectors": yrIndex,
            "updatedYearIndex": yearIndex,
            "updatedPlot": html_content
        })  
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)