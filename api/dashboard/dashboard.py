import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from flask import jsonify
try:
    df = pd.read_csv("FSHS.csv")
except Exception as e:
    print(f"Error reading CSV file: {e}")
    df = None
regions = df['Region'].unique()
years = df['Year'].unique()
sectors = df['Sector'].unique()

gr11_columns = [col for col in df.columns if '11' in col]
gr12_columns = [col for col in df.columns if '12' in col]
gr11_male_columns = [col for col in df.columns if '11' in col and 'MALE' in col and 'FEMALE' not in col]
gr11_female_columns = [col for col in df.columns if '11' in col and 'FEMALE' in col]
gr12_male_columns = [col for col in df.columns if '12' in col and 'MALE' in col and 'FEMALE' not in col]
gr12_female_columns = [col for col in df.columns if '12' in col and 'FEMALE' in col]

strand_columns = [col for col in df.columns if col not in ['Region', 'Year', 'Sector']]

strands = ['ABM', 'HUMMS', 'STEM', 'GAS', 'MARITIME', 'TVL', 'SPORTS', 'ARTS&DESIGN']


def total_students():
    df['Grade 11 Total Students'] = df[gr11_columns].sum(axis=1)
    df['Grade 12 Total Students'] = df[gr12_columns].sum(axis=1)
    df['Grade 11 Male Total'] = df[gr11_male_columns].sum(axis=1)
    df['Grade 11 Female Total'] = df[gr11_female_columns].sum(axis=1)
    df['Grade 12 Male Total'] = df[gr12_male_columns].sum(axis=1)
    df['Grade 12 Female Total'] = df[gr12_female_columns].sum(axis=1)
    df['Total Male Students'] =  df[gr11_male_columns].sum(axis=1) +  df[gr12_male_columns].sum(axis=1)
    df['Total Female Students'] =  df[gr11_female_columns].sum(axis=1) +df[gr12_female_columns].sum(axis=1)
    df['Total Students'] = df[strand_columns].sum(axis=1)

    total_grade_11_male_students = df['Grade 11 Male Total'].sum()
    total_grade_11_female_students = df['Grade 11 Female Total'].sum()
    total_grade_12_male_students = df['Grade 12 Male Total'].sum()
    total_grade_12_female_students = df['Grade 12 Female Total'].sum()
    total_grade_11_students = df['Grade 11 Total Students'].sum()
    total_grade_12_students = df['Grade 12 Total Students'].sum()
    total_male_students =  df['Total Male Students'].sum()
    total_female_students =  df['Total Female Students'].sum()
    overall_total_students = df['Total Students'].sum()

    total_grade_11_students = int(total_grade_11_students)
    total_grade_12_students = int(total_grade_12_students)
    total_grade_11_male_students = int(total_grade_11_male_students)
    total_grade_11_female_students = int(total_grade_11_female_students)
    total_grade_12_male_students = int(total_grade_12_male_students)
    total_grade_12_female_students = int(total_grade_12_female_students)
    total_male_students = int(total_male_students)
    total_female_students = int(total_female_students)
    overall_total_students = int(overall_total_students)

    total = {
        'Grade 11 Total Students': total_grade_11_students,
        'Grade 12 Total Students': total_grade_12_students,
        'Grade 11 Total Male Students': total_grade_11_male_students,
        'Grade 11 Total Female Students': total_grade_11_female_students,
        'Grade 12 Total Male Students': total_grade_12_male_students,
        'Grade 12 Total Female Students': total_grade_12_female_students,
        'Grand Total Male Students': total_male_students,
        'Grand Total Female Students' : total_female_students,
        'Grand Total of All Students': overall_total_students,
    }
    return total

totalstudents = total_students()

def bar_graph_11_male_female():
    grade_11_male = totalstudents.get('Grade 11 Total Male Students', 0)
    grade_11_female = totalstudents.get('Grade 11 Total Female Students', 0)
    categories = ['Grade 11 Male Students', 'Grade 11 Female Students']
    values = [grade_11_male, grade_11_female]
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=categories,
        y=values
    ))
    fig.update_layout(
        xaxis=dict(
            title='Gender',
            titlefont=dict(color='black'),
            tickfont=dict(color='black')
        ),
        yaxis=dict(
            title='Total Students',
            titlefont=dict(color='black'),
            tickfont=dict(color='black')
        ),
        legend=dict(
            font=dict(
                color='black',
                size=12
            )
        ),
        autosize=True,
        width=900,
        height=500,
        margin=dict(l=0, r=0, t=0, b=0),
        plot_bgcolor='white',
        modebar=dict(
            orientation="v",
            bgcolor='#1565C0', 
            activecolor='white', 
            remove=['pan2d', 'lasso2d', 'select2d', 'zoom2d', 'autoScale2d', 
                    'hoverClosestCartesian', 'hoverCompareCartesian'], 
            add=['zoomIn2d', 'zoomOut2d', 'resetScale2d']  
        )
    )
    return fig.to_dict()

def bar_graph_12_male_female():
    grade_12_male = totalstudents.get('Grade 12 Total Male Students', 0)
    grade_12_female = totalstudents.get('Grade 12 Total Female Students', 0)
    categories = ['Grade 12 Male Students', 'Grade 12 Female Students']
    values = [grade_12_male, grade_12_female]
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=categories,
        y=values
    ))
    fig.update_layout(
        xaxis=dict(
            title='Gender',
            titlefont=dict(color='black'),
            tickfont=dict(color='black')
        ),
        yaxis=dict(
            title='Total Students',
            titlefont=dict(color='black'),
            tickfont=dict(color='black')
        ),
        legend=dict(
            font=dict(
                color='black',
                size=12
            )
        ),
        autosize=True,
        width=900,
        height=500,
        margin=dict(l=0, r=0, t=0, b=0),
        plot_bgcolor='white',
        modebar=dict(
            orientation="v",
            bgcolor='#1565C0', 
            activecolor='white', 
            remove=['pan2d', 'lasso2d', 'select2d', 'zoom2d', 'autoScale2d', 
                    'hoverClosestCartesian', 'hoverCompareCartesian'], 
            add=['zoomIn2d', 'zoomOut2d', 'resetScale2d']  
        )
    )
    return fig.to_dict()

def pie_chart_11_12_students():
    grade_11 = totalstudents.get('Grade 11 Total Students', 0)
    grade_12 = totalstudents.get('Grade 12 Total Students', 0)
    categories = ['Grade 11 Total Students', 'Grade 12 Total Students']
    values = [grade_11, grade_12]

    fig = go.Figure()
    fig.add_trace(go.Pie(
        labels=categories,
        values=values,
        textinfo='label+percent',
        insidetextorientation='radial',
        hole=0.4,
        textposition='inside',
    ))

    fig.update_layout(
        width=700,
        height=500,
        margin=dict(l=0, r=0, t=0, b=0),
        showlegend = False,
        plot_bgcolor='white',
        modebar=dict(
            orientation="v", 
            bgcolor='#1565C0', 
            activecolor='white', 
            remove=['pan2d', 'lasso2d', 'select2d', 'zoom2d', 'autoScale2d', 
                    'hoverClosestCartesian', 'hoverCompareCartesian'], 
            add=['zoomIn2d', 'zoomOut2d', 'resetScale2d', 'zoom2d', 'saveImage', 'resetAxes']
        )
    )

    return fig.to_dict()




def total_students_by_strand_gender_and_total():
    totals = {}
    for strand in strands:
        male_cols = [col for col in df.columns if strand in col and 'MALE' in col and 'FEMALE' not in col]
        female_cols = [col for col in df.columns if strand in col and 'FEMALE' in col]
        male_total = df[male_cols].sum().sum()
        female_total = df[female_cols].sum().sum()
        strand_total = male_total + female_total
        totals[strand] = {'Male': male_total, 'Female': female_total, 'Total': strand_total}
    totals_df = pd.DataFrame.from_dict(totals, orient='index').reset_index()
    totals_df.columns = ['Strand', 'Male', 'Female', 'Total']
    return totals_df.to_dict(orient='index')

bystrand = total_students_by_strand_gender_and_total()

def pie_by_strand():
    strands = [value["Strand"] for value in bystrand.values()]
    total_counts = [value["Total"] for value in bystrand.values()]
    fig = go.Figure(data=[go.Pie(
        labels=strands,
        values=total_counts,
        textinfo='label+percent',
        insidetextorientation='radial',
        hole=0.4,
        textposition='inside',
    )])
    fig.update_layout(
        width=700,
        height=500,
        margin=dict(l=0, r=0, t=0, b=0),
        modebar=dict(
            orientation="v", 
            bgcolor='#1565C0', 
            activecolor='white', 
            remove=['pan2d', 'lasso2d', 'select2d', 'zoom2d', 'autoScale2d', 
                    'hoverClosestCartesian', 'hoverCompareCartesian'], 
            add=['zoomIn2d', 'zoomOut2d', 'resetScale2d', 'zoom2d', 'saveImage', 'resetAxes']
        )
    )
    return fig.to_dict()

def strand_grouped_gender():
    strands = [value["Strand"] for value in bystrand.values()]
    female_counts = [value["Female"] for value in bystrand.values()]
    male_counts = [value["Male"] for value in bystrand.values()]

    fig = go.Figure(data=[
        go.Bar(name='Female', x=strands, y=female_counts, offsetgroup=0),
        go.Bar(name='Male', x=strands, y=male_counts, offsetgroup=1)
    ])

    fig.update_layout(
         xaxis=dict(
            title='Year',
            titlefont=dict(color='black'),
            tickfont=dict(color='black')
        ),
        yaxis=dict(
            title='Total Students',
            titlefont=dict(color='black'),
            tickfont=dict(color='black')
        ),
        legend=dict(
            font=dict(
                color='black',
                size=12
            )
        ),
        autosize=True,
        width=1050,
        height=500,
        plot_bgcolor='white',
        margin=dict(l=0, r=0, t=0, b=0),
        modebar=dict(
            orientation="v",
            bgcolor='#1565C0', 
            activecolor='white', 
            remove=['pan2d', 'lasso2d', 'select2d', 'zoom2d', 'autoScale2d', 
                    'hoverClosestCartesian', 'hoverCompareCartesian'], 
            add=['zoomIn2d', 'zoomOut2d', 'resetScale2d']  
        )
    )
    return fig.to_dict()

def total_each_region_by_year():
    region_year_totals = (
        df.groupby(['Region', 'Year'])['Total Students'] 
        .sum()  
        .reset_index()  
    )
    region_data = {}
    for _, row in region_year_totals.iterrows():
        region = row['Region']
        year = row['Year']
        total_students = row['Total Students']
        
        if region not in region_data:
            region_data[region] = {}
        
        region_data[region][year] = total_students

    return region_data


region_by_year = total_each_region_by_year()
def line_chart_by_region():
    traces = []
    years = ["2016 - 2017", "2017 - 2018", "2018 - 2019", "2019 - 2020", "2020 - 2021"]

    for region, year_data in region_by_year.items():
        simplified_region = region.split(" - ")[0]
        traces.append(go.Scatter(
            x=years,
            y=[year_data[year] for year in years],
            mode='lines+markers',
            name=simplified_region 
        ))

    layout = go.Layout(
        xaxis=dict(
            title='Year',
            titlefont=dict(color='black'),
            tickfont=dict(color='black')
        ),
        yaxis=dict(
            title='Total Students',
            titlefont=dict(color='black'),
            tickfont=dict(color='black')
        ),
        legend=dict(
            font=dict(
                color='black',
                size=12
            )
        ),
        autosize=True,
        width=1050,
        height=500,
        plot_bgcolor='white',
        margin=dict(l=0, r=0, t=0, b=0),
        modebar=dict(
            orientation="v",
            bgcolor='#1565C0', 
            activecolor='white', 
            remove=['pan2d', 'lasso2d', 'select2d', 'zoom2d', 'autoScale2d', 
                    'hoverClosestCartesian', 'hoverCompareCartesian'], 
            add=['zoomIn2d', 'zoomOut2d', 'resetScale2d']  
        )
    )

    fig = go.Figure(data=traces, layout=layout)
    return fig.to_dict()





def total_each_region():
    df['Total Students'] = df[strand_columns].sum(axis=1)
    region_totals = (
        df.groupby('Region')['Total Students']
        .sum()
        .reset_index()
    )
    return region_totals.to_dict(orient='index')


def total_by_sector():
    df['Total Students'] = df[strand_columns].sum(axis=1)
    sector_totals = (
        df.groupby('Sector')['Total Students']
        .sum()
        .reset_index()
    )
    sector_totals.columns = ['Sector', 'Total Students']
    return sector_totals.to_dict(orient='index')

def total_by_year_and_sector():
    df['Total Students'] = df[strand_columns].sum(axis=1)
    year_sector_totals = (
        df.groupby(['Year', 'Sector'])['Total Students']
        .sum()
        .reset_index()
    )

    year_sector_totals.columns = ['Year', 'Sector', 'Total Students']
    return year_sector_totals.to_dict(orient='index')

sectorchart = total_by_year_and_sector()
def line_sector_chart():
    years = list(set([entry['Year'] for entry in sectorchart.values()]))  
    years.sort(key=lambda x: int(x.split(" - ")[0])) 

    sectors = ['PRIVATE', 'PUBLIC', 'SUCsLUCs']

    lines = []
    for sector in sectors:
        y_values = [entry['Total Students'] for entry in sectorchart.values() if entry['Sector'] == sector]
        lines.append(go.Scatter(
            x=years,
            y=y_values,
            mode='lines+markers',
            name=sector
        ))

    fig = go.Figure(lines)
    fig.update_layout(
        xaxis=dict(
            title='Year',
            titlefont=dict(color='black'),
            tickfont=dict(color='black')
        ),
        yaxis=dict(
            title='Total Students',
            titlefont=dict(color='black'),
            tickfont=dict(color='black')
        ),
        legend=dict(
            font=dict(
                color='black',
                size=12
            )
        ),
        autosize=True,
        width=1800,
        height=500,
        plot_bgcolor='white',
        margin=dict(l=0, r=0, t=0, b=0),
        modebar=dict(
            orientation="v",
            bgcolor='#1565C0', 
            activecolor='white', 
            remove=['pan2d', 'lasso2d', 'select2d', 'zoom2d', 'autoScale2d', 
                    'hoverClosestCartesian', 'hoverCompareCartesian'], 
            add=['zoomIn2d', 'zoomOut2d', 'resetScale2d']  
        )
    )

    return fig.to_dict()