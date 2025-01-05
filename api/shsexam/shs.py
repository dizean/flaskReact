import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from mpld3 import plugins
import mpld3
import plotly as px

try:
    df = pd.read_csv("FSHS.csv")
except Exception as e:
    print(f"Error reading CSV file: {e}")
    df = None  # Set df to None if there's an error

def fillMissing(df):
    filler = df.fillna(0)
    return filler

def processCSV(df):
    missingFill = fillMissing(df)
    return missingFill

regions = df['Region'].unique()
years = df['Year'].unique()
sectors = df['Sector'].unique()
gr11male = [col for col in df.columns if 'MALE' in col and 'FEMALE' not in col and '11' in col]
gr12male = [col for col in df.columns if 'MALE' in col and 'FEMALE' not in col and '12' in col]
gr11female = [col for col in df.columns if 'FEMALE' in col and '11' in col]
gr12female = [col for col in df.columns if 'FEMALE' in col and '12' in col]
gr11 = [col for col in df.columns if '11' in col]
gr12 = [col for col in df.columns if '12' in col]
grandtotal = gr11 + gr12
male = [col for col in df.columns if 'MALE' in col and 'FEMALE' not in col]
sortedmale = sorted(male, key=lambda x: (x.split(' ')[1], x.split(' ')[0]))
groupedmale = df[sortedmale].T.groupby(lambda x: x.split(' ')[1]).sum().T
groupedmale['Year'] = df['Year']
groupedmale['Sector'] = df['Sector']
groupedmale['Region'] = df['Region']
female = [col for col in df.columns if 'FEMALE' in col]
sortedfemale = sorted(female, key=lambda x: (x.split(' ')[1], x.split(' ')[0]))
groupedfemale = df[sortedfemale].T.groupby(lambda x: x.split(' ')[1]).sum().T
groupedfemale['Year'] = df['Year']
groupedfemale['Sector'] = df['Sector']
groupedfemale['Region'] = df['Region']
allmandf = male + female
# PLOTS BY REGION
# TOTAL BY STRAND EACH REGION
def totalbyStrandEachRegion(regionIndex=0, sectorIndex=0, gradegenderIndex=0):
    regIndex = len(regions)
    secIndex = len(sectors)
    gradegenIndex = 22
    fig, ax = plt.subplots(figsize=(8, 5))
    def update_plot(region_idx, selection_idx, sector_idx):
        print("regionidx:", region_idx, flush= True)
        print("selection_idx:", selection_idx, flush= True)
        print("sector_idx:", sector_idx, flush= True)
        ax.clear()
        current_region = regions[region_idx]
        current_sector = sectors[sector_idx]

        gradegender = {
            0: (gr11male, "Grade 11 Male Students"),#para sa male students by strand, sector,region
            1: (gr11female, "Grade 11 Female Students"),#female students by strand, sector,region
            2: (gr12male, "Grade 12 Male Students"),#para sa male students by strand, sector,region
            3: (gr12female, "Grade 12 Female Students"),#para sa female students by strand, sector,region
            4: (groupedmale.columns.tolist(), "Grade 11 and 12 Male Students"),#group by strand 11abm + 12abm ..etc male
            5: (groupedfemale.columns.tolist(), "Grade 11 and 12 Female Students"),#group by strand 11abm + 12abm ..etc female
            6: (gr11male, "Total Grade 11 Male Students Grand Total"),#total grade 11 by sector, region male
            7: (gr11female, "Total Grade 11 Female Students Grand Total"),#total grade 11 by sector, region female
            8: (gr12male, "Total Grade 12 Male Students Grand Total"),#total grade 12 by sector, region male
            9: (gr12female, "Total Grade 12 Female Students Grand Total"),#total grade 12 by sector, region female
            10: (gr11, "Grade 11 Grand Total"),#grandtotal gr11
            11: (gr12, "Grade 12 Grand Total"),#grandtotal gr12
            12: (grandtotal, "Grade 11 and Grade 12"),#grandtotal gr11+gr12
            13: (male, "Grand Total Male"),#grandtotal male gr11+gr12
            14: (female, "Grand Total Female"),#grandtotal female gr11+gr12
            15: (male, "Total Grade 11 and 12 Male"),#total male 11 and 12 all sector by strand
            16: (female, "Total Grade 11 and 12 Female"),#total female 11 and 12 all sector by strand
            17: (groupedmale.columns.tolist(), "Total 11 and 12 Male Students"),#total male 11 and 12 all sector and merge strand 11abm+12abm ..etc
            18: (groupedfemale.columns.tolist(), "Total 11 and 12 Female Students"),#total female 11 and 12 all sector and merge strand 11abm+12abm ..etc
            19: (male, "OVERALL MALE"),#overallmale all sector
            20: (female,"OVERALL FEMALE"),#overallfemale all sector
            21: (allmandf, "OVERALL MALE AND FEMALE"),#overmale + overfemale
            22: (df, "TOTAL STUDENT OF EACH REGION OF ALL SECTORS IN YEARS 2016 - 2021")#total student all sector by region
        }
        selected_gradegender, title = gradegender[selection_idx]
        print(title)
        colors = sns.color_palette("tab20", n_colors=20)
        if selection_idx in [0, 1,2,3]:
            region_sector_data = df[(df['Region'] == current_region) & (df['Sector'] == current_sector)]
            region_data = region_sector_data.groupby('Year')[selected_gradegender].sum()
            for i, strand in enumerate(selected_gradegender):
                line, = ax.plot(region_data.index, region_data[strand], label=f'{strand}', color=colors[i], marker='o',
                                markersize=5)
                tooltip = plugins.PointLabelTooltip(line, labels=[f"{strand}: {y}" for y in region_data[strand]])
                plugins.connect(fig, tooltip)
            ax.set_title(f"{title} in {current_region} - Sector {current_sector}")
            ax.set_xlabel('Year')
            ax.set_ylabel('Number of students')
            ax.legend()
        elif selection_idx in [4, 5]:
            if selection_idx == 4:
                region_data = groupedmale[
                    (groupedmale['Region'] == current_region) & (groupedmale['Sector'] == current_sector)]
            else:
                region_data = groupedfemale[
                    (groupedfemale['Region'] == current_region) & (groupedfemale['Sector'] == current_sector)]

            region_data_year = region_data.groupby('Year').sum()
            strand_columns = [col for col in region_data_year.columns if col not in ['Region', 'Year', 'Sector']]

            for i, strand in enumerate(strand_columns):
                line, = ax.plot(region_data_year.index, region_data_year[strand], 
                                label=f'{strand}', marker='o', markersize=5, color=colors[i])
                tooltip = plugins.PointLabelTooltip(line, labels=[f"{strand}: {y}" for y in region_data_year[strand]])
                plugins.connect(fig, tooltip)
        elif selection_idx in [15, 16]:
            # Filter data by the selected region
            region_sector_datas = df[df['Region'] == current_region]

            # Group data by 'Year' and sum across the selected columns
            region_datas = region_sector_datas.groupby('Year')[selected_gradegender].sum()

            for i, strand in enumerate(selected_gradegender):
                # Plot the line for the current strand
                line, = ax.plot(
                    region_datas.index,
                    region_datas[strand],
                    label=f'{strand}',
                    marker='o',
                    markersize=5,
                    color=colors[i]
                )

                # Ensure the labels correspond to the y-values for the strand
                labels = [f"{strand}: {y}" for y in region_datas[strand]]

                # Add tooltips for the line plot
                tooltip = plugins.PointLabelTooltip(line, labels=labels)
                plugins.connect(fig, tooltip)

            # Set title and labels
            ax.set_title(f"{title} Trends in {current_region}")
            ax.set_xlabel('Year')
            ax.set_ylabel('Number of Students')
            ax.legend()

        elif selection_idx in [17, 18]:
            # Determine which dataset to use based on selection_idx
            if selection_idx == 17:
                region_data = groupedmale[groupedmale['Region'] == current_region]
            else:
                region_data = groupedfemale[groupedfemale['Region'] == current_region]

            # Group by Year and sum across selected columns
            region_data_year = region_data.groupby('Year')[selected_gradegender].sum()

            # Get valid strand columns for plotting
            strand_columns = [col for col in region_data_year.columns if col not in ['Region', 'Year', 'Sector']]

            for i, strand in enumerate(strand_columns):
                # Plot the line and extract the first Line2D object
                line, = ax.plot(
                    region_data_year.index,
                    region_data_year[strand],
                    label=f'{strand}',
                    marker='o',
                    markersize=5,
                    color=colors[i]
                )

                # Create tooltips for the current strand
                labels = [f"{strand}: {y}" for y in region_data_year[strand]]

                # Attach tooltips to the line
                tooltip = plugins.PointLabelTooltip(line, labels=labels)
                plugins.connect(fig, tooltip)

            # Set title and labels
            ax.set_title(f"Trends for {current_region} ({'Male' if selection_idx == 17 else 'Female'})")
            ax.set_xlabel('Year')
            ax.set_ylabel('Number of Students')
            ax.legend()

            ax.set_title(f"{title} enrolled in {current_region} - ALL SECTORS")
            ax.set_xlabel('Year')
            ax.set_ylabel('Number of students')
            ax.legend()
            ax.set_title(f"{title} enrolled in {current_region} - ALL SECTORS")
            ax.set_xlabel('Year')
            ax.set_ylabel('Number of students')
            ax.legend()
        elif selection_idx in [19, 20, 21]:
            # Filter data for the selected region
            region_sector_data = df[df['Region'] == current_region]

            # Group by Year and sum the selected columns
            region_datas = region_sector_data.groupby('Year')[selected_gradegender].sum().sum(axis=1)
            bars = ax.bar(region_datas.index, region_datas.values, label=title, color=colors[:len(region_datas)])

            # Correct tooltip attachment
            tooltip = plugins.PointLabelTooltip(bars, labels=[str(value) for value in region_datas.values])

            plugins.connect(fig, tooltip)

            # Set chart titles and labels
            ax.set_title(f"{title} enrolled in {current_region} - ALL SECTORS")
            ax.set_xlabel('Year')
            ax.set_ylabel('Number of Students')
            ax.legend()

        elif selection_idx in [22]:
            numeric_df = df.select_dtypes(include='number')
            result = df.groupby('Region')[numeric_df.columns].sum()
            result['Total Students'] = result.sum(axis=1)
            regionss = result.index.str.split(' - ').str[0]
            total_students = result['Total Students']
            bars = ax.barh(regionss, total_students, color=colors)
            tooltip = plugins.BarLabelTooltip(bars)
            plugins.connect(fig, tooltip)
            ax.set_title('Total Students by Region (2016-2021)')
            ax.set_xlabel('Student Count')
            ax.set_ylabel('Regions')
        else:
            region_sector_data = df[(df['Region'] == current_region) & (df['Sector'] == current_sector)]
            # Sum the selected columns grouped by Year
            region_datas = region_sector_data.groupby('Year')[selected_gradegender].sum()
            if region_datas.empty:
                print(f"No data found for {title} in {current_region} - Sector {current_sector}")
                return  # Exit if no data

            # Flatten the data for bar plot
            total_per_year = region_datas.sum(axis=1)

            bars = ax.bar(total_per_year.index, total_per_year.values, label=title, color=colors[:len(total_per_year)])
            
            # Tooltip fix: Ensure the tooltips are connected to the correct data
            tooltip = plugins.PointLabelTooltip(bars, labels=[str(value) for value in total_per_year.values])
            print(tooltip,flush=True)
            plugins.connect(fig, tooltip)

            ax.set_title(f"{title} enrolled in {current_region} - Sector {current_sector}")
            ax.set_xlabel('Year')
            ax.set_ylabel('Number of students')
            ax.legend()

    update_plot(regionIndex, gradegenderIndex, sectorIndex)

    # Adding interactive legend
    handles, labels = ax.get_legend_handles_labels()
    interactive_legend = plugins.InteractiveLegendPlugin(zip(handles, ax.collections), labels)
    # plugins.connect(fig, interactive_legend, plugins.Zoom())
    plugins.connect(fig, interactive_legend, plugins.Zoom(), plugins.Reset())
    # toolbar_html = """
    # <div style="display: flex; justify-content: center; margin-top: 10px;">
    #     <button onclick="mpld3.reset(fig)">Reset</button>
    #     <button onclick="mpld3.enable_zoom(fig)">Zoom</button>
        
    # </div>
    # """
    mpld3.save_html(fig, "plot.html")
    html_content = mpld3.fig_to_html(fig) 
    return regIndex, secIndex, gradegenIndex, html_content

def totalStudentsbySector(regionIndex=0, yearIndex=0, genderIndex=0, width=500, height=500):
    regIndex = len(regions)
    yrIndex = len(years)
    gendIndex = 3
    
    fig, ax = plt.subplots(figsize=(width / 100, height / 100))  
    
    def update_plot(region_idx, year_idx, gender_idx):
        ax.clear()
        gender = {
            0: (male, "Male"),
            1: (female, "Female"),
            2: (df.columns, "Overall")
        }
        
        current_region = regions[region_idx]
        current_year = years[year_idx]
        current_gender = gender[gender_idx]
        gender_cols = current_gender[0]
        gender_label = current_gender[1]

        if gender_idx in [0, 1]:  # Male or Female
            by_sector = df.groupby(['Region', 'Year', 'Sector'])[gender_cols].sum()
            region_year_data = by_sector.loc[(current_region, current_year)]
            sector_counts = region_year_data.sum(axis=1)
        else:  # Overall
            by_sector = df.groupby(['Region', 'Year', 'Sector']).sum()
            region_year_data = by_sector.loc[(current_region, current_year)]
            sector_counts = region_year_data.sum(axis=1)

        wedges, texts, autotexts = ax.pie(
                sector_counts,
                labels=sector_counts.index,
                autopct=lambda pct: f'{pct:.1f}%' if pct > 0 else '',
                colors=sns.color_palette("rocket_r"),
                radius=1.2,
                labeldistance=0.3
            )

        ax.set_title(f"{gender_label} Students in ({current_year}) by Sector in {current_region}")

    update_plot(regionIndex, yearIndex, genderIndex)

    plt.subplots_adjust(left=0.05, right=0.95, top=0.85, bottom=0.1)  
    plt.tight_layout(pad=0) 

    html_content = mpld3.fig_to_html(fig)
    return regIndex, yrIndex, gendIndex, html_content


def totalStudentsbyRegion(yearIndex=0): 
    yrIndex = len(years)
    fig, ax = plt.subplots(figsize=(10, 5))

    def update_plot(year_idx):
        ax.clear()
        current_year = years[year_idx]
        df_filtered = df[df['Year'] == current_year]
        total_counts = df_filtered.groupby('Region')[allmandf].sum().sum(axis=1)
        num_regions = len(regions)
        color = sns.color_palette("flare", n_colors=num_regions)

        wedges, texts, autotexts = ax.pie(
            total_counts,
            labels=regions,
            autopct=lambda pct: f'{pct:.1f}%' if pct > 0 else '',
            colors=color,
            radius=1.2
        )
        ax.set_title(f'Total Students - Year {current_year}', pad=20)

    update_plot(yearIndex)
    
    html_content = mpld3.fig_to_html(fig)
    return yrIndex, html_content




# @app.route('/totalbyStrandEachRegion', methods=['GET', 'PUT'])
# def totalStrand():
#     if request.method == 'GET':
#         print("Handling GET request")
#         regIndex, secIndex, gradegenIndex, html_content = totalbyStrandEachRegion()
#         return jsonify({
#             "regions": regIndex,
#             "sectors": secIndex,
#             "gradeGender": gradegenIndex,
#             'plotHTML': html_content,
#         })
    
#     elif request.method == 'PUT':
#         print("Handling PUT request")
#         data = request.get_json()
#         regionIndex = data.get('regIndex', 0)
#         sectorIndex = data.get('secIndex', 0)
#         gradegenderIndex = data.get('gradegenIndex', 0)

#         # Update plot based on new indices
#         regIndex, secIndex, gradegenIndex, html_content = totalbyStrandEachRegion(regionIndex, sectorIndex, gradegenderIndex)

#         return jsonify({
#             "message": "Indices updated",
#             "regions": regIndex,
#             "sectors": secIndex,
#             "gender": gradegenIndex,
#             "updatedRegIndex": regionIndex,
#             "updatedSecIndex": sectorIndex,
#             "updatedGradeGenIndex": gradegenderIndex,
#             "updatedPlot": html_content
#         })

# @app.route('/totalStudentsbySector', methods=['GET', 'PUT'])
# def totalStudentsSector():
#     if request.method == 'GET':
#         print("Handling GET request")
#         regIndex, yrIndex, gendIndex, html_content= totalStudentsbySector()
#         return jsonify({
#             "regions": regIndex,
#             "years": yrIndex,
#             "genders": gendIndex,
#             'plotHTML': html_content,
#         })
    
#     elif request.method == 'PUT':
#         print("Handling PUT request")
#         data = request.get_json()
#         regionIndex = data.get('regIndex', 0)
#         genderIndex = data.get('genIndex', 0)
#         yearIndex = data.get('yearIndex', 0)

#         # Update plot based on new indices
#         regIndex, yrIndex, gendIndex,html_content  = totalStudentsbySector(regionIndex, yearIndex,genderIndex )
# # 
#         return jsonify({
#             "message": "Indices updated",
#             "regions": regIndex,
#             "sectors": yrIndex,
#             "gender": gendIndex,
#             "updatedRegIndex": regionIndex,
#             "updatedGenderIndex": genderIndex,
#             "updatedYearIndex": yearIndex,
#             "updatedPlot": html_content
#         })  
# @app.route('/totalStudentsbyRegion', methods=['GET', 'PUT'])
# def totalStudentsRegion():
    
#     if request.method == 'GET':
#         print("Handling GET request")
#         yrIndex,html_content= totalStudentsbyRegion()
#         return jsonify({
#             "years": yrIndex,
#             'plotHTML': html_content,
#         })
    
#     elif request.method == 'PUT':
#         print("Handling PUT request")
#         data = request.get_json()
#         yearIndex = data.get('yearIndex', 0)

#         # Update plot based on new indices
#         yrIndex ,html_content  = totalStudentsbyRegion(yearIndex )
# # 
#         return jsonify({
#             "message": "Indices updated",
#             "sectors": yrIndex,
#             "updatedYearIndex": yearIndex,
#             "updatedPlot": html_content
#         }) 



