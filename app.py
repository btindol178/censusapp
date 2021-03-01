# TO DO !!!!!!!!!!!!!!!!!
# JUST DO CSS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# UPLOAD THE DATA MANIPULATION PART INTO CSV.. TURN THE FIPS INTO A INT AND RECONVERT AFTER UPLOAD INTO THIS SCRIPT
# FROM THERE PUT THE FINAL MANIPULATION FROM WIDE TO NARROW INSIDE THE CALLBACKS TO BE ABLE TO MANIPULATE FOR THE DROPDOWNS 
# CHANGE df.year.unique() for the dropdown selection to year = ['2015','2016'] etc to remove all the extra dropdowns!!!!!!!!!!!!
# FORMAT THE MAP IN COOL STYLE
# ADD A INTERACTIVE FEATURE WHEN CLICK MAP FILTER FOR THAT GEOID/FIPS AND GIVE THE POPULATION FOR FEMALE AND MALE AND A FEW RACES 
# The text hover is not showing correct percent moving over a few columns doesnt make sense.....


import plotly.graph_objects as go # or plotly.express as px
#fig = go.Figure() # or any Plotly Express function e.g. px.bar(...)
# fig.add_trace( ... )
# fig.update_layout( ... )

import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc

import dash_html_components as html
from urllib.request import urlopen
import json
import pandas as pd
import plotly.express as px
import numpy as np 
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import zipfile

###########################################################################################################################################################################
################################################################################################################################################################################
# Data Extraction for the coropleth map
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
#
# ALL you need is the s

# New Way to load the app!!!! refer to demographic extraction ipby notebook
# Location of manipulation script C:\Users\btindol\OneDrive - Stryker\Python Scripts\GlobalDatabaseExtractionToMYSQL\CustomerGlobalIntelligenceScripts\Census Extraction
# This is fed by R script also location of this is "C:/Users/btindol/OneDrive - Stryker/Python Scripts/GlobalDatabaseExtractionToMYSQL/CustomerGlobalIntelligenceScripts/Census Extraction/CountyPopulationExtractionFiles/USACountyPopulation.csv"
# and r file is C:\Users\btindol\OneDrive - Stryker\Python Scripts\GlobalDatabaseExtractionToMYSQL\CustomerGlobalIntelligenceScripts\Census Extraction

df1z = zipfile.ZipFile('df1.zip') ;df2z = zipfile.ZipFile('df2.zip') ;df3z = zipfile.ZipFile('df3.zip');df4z = zipfile.ZipFile('df4.zip');df5z = zipfile.ZipFile('df5.zip');  
df6z = zipfile.ZipFile('df6.zip') ;df7z = zipfile.ZipFile('df7.zip') ;df8z = zipfile.ZipFile('df8.zip');df9z = zipfile.ZipFile('df9.zip');df10z = zipfile.ZipFile('df10.zip');  

df1 = pd.read_csv(df1z.open('df1.csv'));df2 = pd.read_csv(df2z.open('df2.csv'));df3 = pd.read_csv(df3z.open('df3.csv'));df4 = pd.read_csv(df4z.open('df4.csv'));df5 = pd.read_csv(df5z.open('df5.csv'));
df6 = pd.read_csv(df6z.open('df6.csv'));df7 = pd.read_csv(df7z.open('df7.csv'));df8 = pd.read_csv(df8z.open('df8.csv'));df9 = pd.read_csv(df9z.open('df9.csv'));df10 = pd.read_csv(df10z.open('df10.csv'));

# df1 = pd.read_csv("df1.csv");df2 = pd.read_csv("df2.csv");df3 = pd.read_csv("df3.csv");df4 = pd.read_csv("df4.csv")
# df5 = pd.read_csv("df5.csv");df6 = pd.read_csv("df6.csv");df7 = pd.read_csv("df7.csv");df8 = pd.read_csv("df8.csv")
# df9 = pd.read_csv("df9.csv");df10 = pd.read_csv("df10.csv")

dfz = ( df1.append(df2).append(df3).
              append(df4).append(df5).append(df6).
              append(df7).append(df8).
              append(df9).append(df10))

dfz2 = dfz.drop('Unnamed: 0', 1)
dfz3 = dfz2.drop('Unnamed: 0.1', 1)
demographics = dfz3

demographics['fipsmerge'] = np.where(demographics['name'].str.contains('California', case=False).fillna(False),0,
np.where(demographics['name'].str.contains('Alabama', case=False).fillna(False),0,
np.where(demographics['name'].str.contains('Arkansas',case=False).fillna(False),0,
np.where(demographics['name'].str.contains('Arizona',case=False).fillna(False),0,
np.where(demographics['name'].str.contains('Colorado',case=False).fillna(False),0,
np.where(demographics['name'].str.contains('Connecticut',case=False).fillna(False),0,""))))))
demographics['fipsmerge'] = demographics['fipsmerge'].astype(str)
demographics["fips3"]= demographics["fipsmerge"].astype(str) + demographics["fips"].astype(str)
demographics = demographics[["fips3","name","sex","race","year",'Age 0 to 4 years', 'Age 5 to 9 years' ,'Age 10 to 14 years', 'Age 15 to 19 years',
 'Age 20 to 24 years', 'Age 25 to 29 years', 'Age 30 to 34 years', 'Age 35 to 39 years', 'Age 40 to 44 years', 'Age 45 to 49 years', 'Age 50 to 54 years',
 'Age 55 to 59 years', 'Age 60 to 64 years', 'Age 65 to 69 years', 'Age 70 to 74 years', 'Age 75 to 79 years', 'Age 80 to 84 years', 'Age 85 years and older',
 'Percent_0_to_4', 'Percent_5_to_9', 'Percent_10_to_14', 'Percent_15_to_19', 'Percent_20_to_24', 'Percent_25_to_29', 'Percent_30_to_34',
 'Percent_35_to_39', 'Percent_40_to_44', 'Percent_45_to_49', 'Percent_50_to_54', 'Percent_55_to_59', 'Percent_60_to_64', 'Percent_65_to_69',
 'Percent_70_to_74', 'Percent_75_to_79', 'Percent_80_to_84', 'Percent_85_older','deaths','births','net_migration','Median age','Total_Population']]
demographics.columns = ['fips', 'name','sex','race','year','Age 0 to 4 years', 'Age 5 to 9 years' ,'Age 10 to 14 years', 'Age 15 to 19 years',
 'Age 20 to 24 years', 'Age 25 to 29 years', 'Age 30 to 34 years', 'Age 35 to 39 years', 'Age 40 to 44 years', 'Age 45 to 49 years', 'Age 50 to 54 years',
 'Age 55 to 59 years', 'Age 60 to 64 years', 'Age 65 to 69 years', 'Age 70 to 74 years', 'Age 75 to 79 years', 'Age 80 to 84 years', 'Age 85 years and older',
 'Percent_0_to_4', 'Percent_5_to_9', 'Percent_10_to_14', 'Percent_15_to_19', 'Percent_20_to_24', 'Percent_25_to_29', 'Percent_30_to_34',
 'Percent_35_to_39', 'Percent_40_to_44', 'Percent_45_to_49', 'Percent_50_to_54', 'Percent_55_to_59', 'Percent_60_to_64', 'Percent_65_to_69',
 'Percent_70_to_74', 'Percent_75_to_79', 'Percent_80_to_84', 'Percent_85_older', 'deaths','births','net_migration','Median age','Total_Population']    

cols_dd = [
  'Percent_0_to_4', 'Percent_5_to_9', 'Percent_10_to_14', 'Percent_15_to_19', 'Percent_20_to_24', 'Percent_25_to_29', 'Percent_30_to_34',
 'Percent_35_to_39', 'Percent_40_to_44', 'Percent_45_to_49', 'Percent_50_to_54', 'Percent_55_to_59', 'Percent_60_to_64', 'Percent_65_to_69',
 'Percent_70_to_74', 'Percent_75_to_79', 'Percent_80_to_84', 'Percent_85_older']

years = demographics["year"].unique()

###########################################################################################################################################################################
################################################################################################################################################################################

# Load the data without all the code 
demographics2 = pd.melt(demographics, id_vars=['fips', 'name', 'sex', 'race', 'year'], value_vars=[ 'Age 0 to 4 years', 'Age 5 to 9 years','Age 10 to 14 years', 'Age 15 to 19 years',
 'Age 20 to 24 years', 'Age 25 to 29 years', 'Age 30 to 34 years', 'Age 35 to 39 years', 'Age 40 to 44 years',
 'Age 45 to 49 years', 'Age 50 to 54 years', 'Age 55 to 59 years', 'Age 60 to 64 years',
 'Age 65 to 69 years', 'Age 70 to 74 years', 'Age 75 to 79 years', 'Age 80 to 84 years', 'Age 85 years and older', 'Percent_0_to_4', 'Percent_5_to_9', 'Percent_10_to_14',
 'Percent_15_to_19', 'Percent_20_to_24', 'Percent_25_to_29', 'Percent_30_to_34', 'Percent_35_to_39', 'Percent_40_to_44',
 'Percent_45_to_49', 'Percent_50_to_54', 'Percent_55_to_59', 'Percent_60_to_64', 'Percent_65_to_69', 'Percent_70_to_74',
 'Percent_75_to_79', 'Percent_80_to_84', 'Percent_85_older', 'births', 'deaths', 'net_migration','Median age' , 'Total_Population'])
demographics2.columns = ['fips', 'name','sex','race','year','agegroup','value'] 
demographics2z = demographics2[(demographics2.agegroup == 'births') | (demographics2.agegroup == 'deaths') | (demographics2.agegroup == 'net_migration') | (demographics2.agegroup == 'Total_Population') | (demographics2.agegroup == 'Median age') ]
demographics2 = demographics2[(demographics2.agegroup == 'Age 0 to 4 years') | (demographics2.agegroup == 'Age 5 to 9 years') | (demographics2.agegroup == 'Age 10 to 14 years') | (demographics2.agegroup ==  'Age 15 to 19 years') | (demographics2.agegroup ==  'Age 20 to 24 years') | (demographics2.agegroup ==  'Age 25 to 29 years') | (demographics2.agegroup ==  'Age 30 to 34 years')| (demographics2.agegroup ==  'Age 35 to 39 years') | (demographics2.agegroup ==  'Age 40 to 44 years') | (demographics2.agegroup ==  'Age 45 to 49 years') | (demographics2.agegroup ==  'Age 50 to 54 years')| (demographics2.agegroup ==  'Age 55 to 59 years') | (demographics2.agegroup ==  'Age 60 to 64 years') | (demographics2.agegroup ==  'Age 65 to 69 years') | (demographics2.agegroup ==  'Age 70 to 74 years') | (demographics2.agegroup ==  'Age 75 to 79 years') | (demographics2.agegroup ==  'Age 80 to 84 years') | (demographics2.agegroup ==  'Age 85 years and older')]
demographics = demographics[(demographics.sex == "Both sexes") & (demographics.race == "All races")]


# for bar charts
years = demographics2["year"].unique()
race = demographics2["race"].unique()
name = demographics2["name"].unique()
sex = demographics2["sex"].unique()

#for the cards
yearsz = demographics2z["year"].unique()
racez = demographics2z["race"].unique()
namez = demographics2z["name"].unique()
sexz = demographics2z["sex"].unique()

external_stylesheets=["assets/template.css", "assets/bootstrap.min.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.layout = html.Div([

html.Div([

    html.Div([
                    dbc.Row([html.Img(src=('/assets/census.jpg'), width=200, height = 200,
                                    style={"margin-left": "2rem"})
                            ])
                    ]),

            html.Div([
                html.P(children =['Explore the Demographics of the United States for 2015-2019!',html.Br(),'Datsource: https://data.census.gov',html.Br(),'Code: https://github.com/btindol178'], className = 'fix_label', style = {'color': 'white', 'margin-top': '2px'}),
            #    dcc.Dropdown(id='row-dropdownzz', options=[{'label' : p, 'value' : p} for p in years], # This is the same as bar chart values the same so i guess this works filtering demographics2z
            #                                           multi=False, value=years[0],
            #                                           style = {'display': True},
            #                                           className='dcc_compon'),
                ], className = "create_container2 four columns", style = {'margin-bottom': '20px', "margin-top": "20px"}),
 html.Div([
               html.P(children=['Author: Blake Tindol',html.Br(), 'Email: blaketindol@gmail.com',html.Br(),'LinkedIn: https://www.linkedin.com/in/blake-tindol-a17121ba/'], className = 'fix_label', style = {'color': 'white', 'margin-top': '2px'}),
# dcc.Dropdown(id='row-dropdown2z', options=[{'label' : p, 'value' : p} for p in name],
#                                                       multi=False, value=name[0],
#                                                       style = {'display': True},
#                                                       className='dcc_compon'),
                ], className = "create_container2 four columns", style = {'margin-bottom': '20px', "margin-top": "20px"})

            ], className = "row flex-display"),  


html.Div([
         html.Div([
              html.Div(id='live_text1'),

         ], className = "create_container two columns", style = {'text-align': 'center'}),


         html.Div([
              html.Div(id='live_text2'),

         ], className = "create_container two columns", style = {'text-align': 'center'}),

         
          html.Div([
              html.Div(id='live_text3'),

         ], className = "create_container two columns", style = {'text-align': 'center'}),


         html.Div([
              html.Div(id='live_text4'),

         ], className = "create_container two columns", style = {'text-align': 'center'}),

          html.Div([
              html.Div(id='live_text5'),

         ], className = "create_container two columns", style = {'text-align': 'center'}),

          html.Div([
              html.Div(id='live_text6'),

         ], className = "create_container two columns", style = {'text-align': 'center'}),

            ], className = "row flex-display"),



html.Div(children=[   
    html.Div([
               html.P('Select Age Group', className = 'fix_label', style = {'color': 'white', 'margin-top': '2px'}),
               dcc.Dropdown(id='column-dropdown', options=[{'label' : p, 'value' : p} for p in cols_dd],
                                                      multi=False, value=cols_dd[0],
                                                      style = {'display': True},
                                                      className='dcc_compon'),
                ], className = "create_container2 four columns", style = {'margin-bottom': '20px', "margin-top": "20px",'margin-left':'20px'}),
    # html.Div([
    #            html.P('Select Year', className = 'fix_label', style = {'color': 'white', 'margin-top': '2px'}),
    #            dcc.Dropdown(id='row-dropdown', options=[{'label' : p, 'value' : p} for p in years],
    #                                                   multi=False, value=years[0],
    #                                                   style = {'display': True},
    #                                                   className='dcc_compon'),
    #             ], className = "create_container2 four columns", style = {'margin-bottom': '20px', "margin-top": "20px"}),
     html.Div([
               html.P('Select Race', className = 'fix_label', style = {'color': 'white', 'margin-top': '2px'}),            
               dcc.Dropdown(id='row-dropdown1', options=[{'label' : p, 'value' : p} for p in race],
                                                      multi=False, value=race[0],
                                                      style = {'display': True},
                                                      className='dcc_compon'),
                ], className = "create_container2 four columns", style = {'margin-bottom': '20px', "margin-top": "20px",'margin-left':'20px'}),
    html.Div([
               html.P('Select County', className = 'fix_label', style = {'color': 'white', 'margin-top': '2px'}), 
               dcc.Dropdown(id='row-dropdown2', options=[{'label' : p, 'value' : p} for p in name],
                                                      multi=False, value=name[0],
                                                      style = {'display': True},
                                                      className='dcc_compon'),
                ], className = "create_container2 four columns", style = {'margin-bottom': '20px', "margin-top": "20px",'margin-left':'20px'}),
                

html.Div([
    html.P('Select Year', className = 'fix_label', style = {'color': 'white', 'margin-top': '2px'}), 
    dcc.Slider(
    id='row-dropdownz',
    min=2015,
    max=2019,
    marks={
        2015: {'label': '2015', 'style': {'color': '#ffffff'}},
        2016: {'label': '2016', 'style': {'color': '#ffffff'}},
        2017: {'label': '2017', 'style': {'color': '#ffffff'}},
        2018: {'label': '2018', 'style': {'color': '#ffffff'}},
        2019: {'label': '2019', 'style': {'color': '#ffffff'}}

    },
    step = 1,
    value = 2019
    )
    ], className = "create_container2 four columns", style = {'margin-bottom': '20px', "margin-top": "20px",'margin-left':'20px'}),
], className = "row flex-display"),  

 html.Div(children=[
    dcc.Loading(
            id="loading-1",
            type="default",
            children=dcc.Graph(id='display-selected-values' ,className='dcc_compon',style={'display': 'inline-block'})),
    dcc.Loading(
            id="loading-2",
            type="default",
             children= dcc.Graph(id='demographicbarchart3',className='dcc_compon',style={'display': 'inline-block'})),
], className = "row flex-display",style={"margin-left": "225px"}),

html.Div(children=[
    dcc.Loading(
            id="loading-3",
            type="default",
            children=dcc.Graph(id='demographicbarchart2',className='dcc_compon',style ={'display': 'inline-block'})),

    dcc.Loading(
            id="loading-4",
            type="default",
             children=dcc.Graph(id='demographicbarchart' ,className='dcc_compon',style ={'display': 'inline-block'})),
], className = "row flex-display",style={"margin-left": "225px"}),

])

# LOADING CODE FOR THE MAP
@app.callback(Output("display-selected-values", "children"), Input("loading-input-1", "value"))
def input_triggers_spinner(value):
    time.sleep(1)
    return value


# LOADING CODE FOR THE MAP
@app.callback(Output("demographicbarchart", "children"), Input("loading-input-2", "value"))
def input_triggers_spinner(value):
    time.sleep(1)
    return value



# LOADING CODE FOR THE MAP
@app.callback(Output("demographicbarchart2", "children"), Input("loading-input-3", "value"))
def input_triggers_spinner(value):
    time.sleep(1)
    return value



# LOADING CODE FOR THE MAP
@app.callback(Output("demographicbarchart3", "children"), Input("loading-input-4", "value"))
def input_triggers_spinner(value):
    time.sleep(1)
    return value



@app.callback(
    dash.dependencies.Output('display-selected-values', 'figure'),
    [dash.dependencies.Input('column-dropdown', 'value'),
    dash.dependencies.Input('row-dropdownz', 'value')])
def update_output(columndropdown,rowdropdownz):
    demographics2 = demographics[demographics["year"] == rowdropdownz]
    var =demographics2.columns.get_loc(columndropdown)
            # 24 and 48 for actual valu 
    newindex = var-18 # To get the index of the matching age group quantile column with the same age group percentil move over to left 18 columns 
    newestindex = demographics2.iloc[:,[newindex]] # to get the percentile cordinating to the value 
    newestindexvar= newestindex.columns[0]
    #var1 = demographics2["Percent_50_to_54"].astype(str)
    maxvar = demographics2[columndropdown].max().astype(int) # DYNAMIC MOVMENT OF WHATEVER THE MAX VALUE IS OF THAT COLUMN TO BE THE NEW MAX POINT..
    fig = go.Figure()
    fig.add_trace(go.Choroplethmapbox(geojson=counties, locations=demographics2.fips, z=round(demographics2[columndropdown].astype(float),2),
                                    colorscale="Viridis", zmin=0, zmax=maxvar, # how to chunck it out into bins alsuuse max var? (picking bins helps it have more granularity)
                                    marker_opacity=0.5, marker_line_width=0,
                                    text =demographics2["name"],
                                    customdata = round(demographics2[newestindexvar],2),
                                    hovertemplate = '<b>County Name </b>: <b>%{text}</b>'+
                                            '<br><b>Percent of Population </b>: %{z}<br>' +
                                            '<b>Population</b>: <b> %{customdata}</b>'))

    fig.update_layout(mapbox_style="carto-positron",mapbox_zoom=3, mapbox_center = {"lat": 37.0902, "lon": -95.7129})
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig

@app.callback(
    dash.dependencies.Output('demographicbarchart', 'figure'),
    [dash.dependencies.Input('row-dropdownz', 'value'),
    dash.dependencies.Input('row-dropdown1', 'value'),
    dash.dependencies.Input('row-dropdown2', 'value')])
def update_output(year,race,name):
    demographics3 = demographics2[(demographics2.year == year) &(demographics2.race == race) & (demographics2.name == name) &(demographics2.sex == "Male") ]
    #demographics2 = demographics[(demographics["year"] == year) & (demographics["sex"] == sex) & (demographics["race"] == race) & (demographics["fips"] == fips)]
    data = go.Bar(x=demographics3.agegroup,
                  y=demographics3.value,marker=dict(color = demographics3.value,colorscale='viridis'))
    layout = go.Layout(title=  "Male Age Demographics")
    fig = go.Figure(data=data, layout=layout)
    return fig

@app.callback(
    dash.dependencies.Output('demographicbarchart2', 'figure'),
    [dash.dependencies.Input('row-dropdownz', 'value'),
    dash.dependencies.Input('row-dropdown1', 'value'),
    dash.dependencies.Input('row-dropdown2', 'value')])
def update_output(year,race,name):
    demographics3 = demographics2[(demographics2.year == year) &(demographics2.race == race) & (demographics2.name == name) &(demographics2.sex == "Female") ]
    #demographics2 = demographics[(demographics["year"] == year) & (demographics["sex"] == sex) & (demographics["race"] == race) & (demographics["fips"] == fips)]
    data = go.Bar(x=demographics3.agegroup,
                  y=demographics3.value,marker=dict(color = demographics3.value,colorscale='viridis'))
    layout = go.Layout(title=  "Female Age Demographics")
    fig = go.Figure(data=data, layout=layout)
    return fig


@app.callback(
    dash.dependencies.Output('demographicbarchart3', 'figure'),
    [dash.dependencies.Input('row-dropdownz', 'value'),
    dash.dependencies.Input('row-dropdown1', 'value'),
    dash.dependencies.Input('row-dropdown2', 'value')])
def update_output(year,race,name):
    demographics3 = demographics2[(demographics2.year == year) &(demographics2.race == race) & (demographics2.name == name) &(demographics2.sex == "Both sexes") ]
    #demographics2 = demographics[(demographics["year"] == year) & (demographics["sex"] == sex) & (demographics["race"] == race) & (demographics["fips"] == fips)]
    data = go.Bar(x=demographics3.agegroup,
                  y=demographics3.value,marker=dict(color = demographics3.value,colorscale='viridis'))
    layout = go.Layout(title=  "Both Sexes Demographics")
    fig = go.Figure(data=data, layout=layout)
    return fig

# CARD FOR THE MIGRATION FOR THAT COUNTY
@app.callback(
    dash.dependencies.Output('live_text1', 'children'),
    [dash.dependencies.Input('row-dropdownz', 'value'),
    dash.dependencies.Input('row-dropdown2', 'value')]
    )

# MAKE SURE THAT YEAR GOES INTO CARDS AS A INT OR STRING WHICH EVER IS USED...
def update_graph(year,name):
   demographics3 = demographics2z[(demographics2z.race == 'All races') & (demographics2z.agegroup == 'net_migration') & (demographics2z.year == year) & (demographics2z.name == name) & (demographics2z.sex == "Both sexes")]
   demographics3 = pd.DataFrame(demographics3)
   var = demographics3.iloc[0,6]


   return [
            html.H6(children = 'Net Migration',
                    style={'textAlign': 'center',
                              'color': 'white'}
                    ),
            html.P("{}%".format(str(round(var,2))),style={'textAlign': 'center',
                              'color': 'white'}),
             
  ]

# CARD FOR THE MIGRATION FOR THAT COUNTY
@app.callback(
    dash.dependencies.Output('live_text2', 'children'),
    [dash.dependencies.Input('row-dropdownz', 'value'),
    dash.dependencies.Input('row-dropdown2', 'value')]
    )

# MAKE SURE THAT YEAR GOES INTO CARDS AS A INT OR STRING WHICH EVER IS USED...
def update_graph(year,name):
   demographics3 = demographics2z[(demographics2z.race == 'All races') & (demographics2z.agegroup == 'births') & (demographics2z.year == year) & (demographics2z.name == name) & (demographics2z.sex == "Both sexes")]
   demographics3 = pd.DataFrame(demographics3)
   var = demographics3.iloc[0,6]


   return [
            html.H6(children = 'Total Births',
                    style={'textAlign': 'center',
                              'color': 'white'}
                    ),
            html.P("{}".format(str(round(var,2))),style={'textAlign': 'center',
                              'color': 'white'}),
             
  ]

# CARD FOR THE MIGRATION FOR THAT COUNTY
@app.callback(
    dash.dependencies.Output('live_text3', 'children'),
    [dash.dependencies.Input('row-dropdownz', 'value'),
    dash.dependencies.Input('row-dropdown2', 'value')]
    )
# MAKE SURE THAT YEAR GOES INTO CARDS AS A INT OR STRING WHICH EVER IS USED...
def update_graph(year,name):
   demographics3 = demographics2z[(demographics2z.race == 'All races') & (demographics2z.agegroup == 'deaths') & (demographics2z.year == year) & (demographics2z.name == name) & (demographics2z.sex == "Both sexes")]
   demographics3 = pd.DataFrame(demographics3)
   var = demographics3.iloc[0,6]


   return [
            html.H6(children = 'Total Deaths',
                    style={'textAlign': 'center',
                              'color': 'white'}
                    ),
            html.P("{}".format(str(round(var,2))),style={'textAlign': 'center',
                              'color': 'white'}),
             
  ]

@app.callback(
    dash.dependencies.Output('live_text4', 'children'),
    [dash.dependencies.Input('row-dropdownz', 'value'),
    dash.dependencies.Input('row-dropdown2', 'value')]
    )
# MAKE SURE THAT YEAR GOES INTO CARDS AS A INT OR STRING WHICH EVER IS USED...
def update_graph(year,name):
   demographics3 = demographics2z[(demographics2z.race == 'All races') & (demographics2z.agegroup == 'Total_Population') & (demographics2z.year == year) & (demographics2z.name == name) & (demographics2z.sex == "Both sexes")]
   demographics3 = pd.DataFrame(demographics3)
   var = demographics3.iloc[0,6]


   return [
            html.H6(children = 'Total Population',
                    style={'textAlign': 'center',
                              'color': 'white'}
                    ),
            html.P("{}".format(str(round(var,2))),style={'textAlign': 'center',
                              'color': 'white'}),
             
  ] 

@app.callback(
    dash.dependencies.Output('live_text5', 'children'),
    [dash.dependencies.Input('row-dropdownz', 'value'),
    dash.dependencies.Input('row-dropdown2', 'value')]
    )
# MAKE SURE THAT YEAR GOES INTO CARDS AS A INT OR STRING WHICH EVER IS USED...
def update_graph(year,name):
   demographics3 = demographics2z[(demographics2z.race == 'All races') & (demographics2z.agegroup == 'Median age') & (demographics2z.year == year) & (demographics2z.name == name) & (demographics2z.sex == "Both sexes")]
   demographics3 = pd.DataFrame(demographics3)
   var = demographics3.iloc[0,6]


   return [
            html.H6(children = 'Median Age',
                    style={'textAlign': 'center',
                              'color': 'white'}
                    ),
            html.P("{}".format(str(round(var,2))),style={'textAlign': 'center',
                              'color': 'white'}),
             
  ] 


@app.callback(
    dash.dependencies.Output('live_text6', 'children'),
    [dash.dependencies.Input('row-dropdown2', 'value')]
    )
# MAKE SURE THAT YEAR GOES INTO CARDS AS A INT OR STRING WHICH EVER IS USED...
def update_graph(name):
   demographics3 = demographics2z[(demographics2z.race == 'All races') & (demographics2z.agegroup == 'net_migration') &(demographics2z.name == name) & (demographics2z.sex == "Both sexes")]
   demographics3 = pd.DataFrame(demographics3)
   var2 = demographics3.iloc[3,6]
   var1 = demographics3.iloc[0,6]
   var3 = var2-var1

   return [
            html.H6(children = 'Net Migration 2015:2019',
                    style={'textAlign': 'center',
                              'color': 'white'}
                    ),
            html.P("{}%".format(str(round(var3,2))),style={'textAlign': 'center',
                              'color': 'white'}),
             
  ] 


if __name__ == '__main__':
    app.run_server()