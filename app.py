'''
This python script runs an interactive Plotly map through Dash.

Plotly: https://plot.ly/python/
Dash: https://dash.plot.ly/

Prerequisites: A clean CSV to read into a Pandas dataframe, with columns
for latitude, longitude, a size/weight (here, we used volume of pills),
and text (for the hover title)
'''

# Imports
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output 
import pandas as pd
import plotly.graph_objects as go
import plotly.offline as offline

# Reading in a clean and prepared CSV
df = pd.read_csv("data/TX_County_Buyer_Data_Aggregated.csv")

# Setting a style sheet
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Instantiating the app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Defining the graph, the base map, and the slider, which unfortunately
# I cannot change the size of
app.layout = html.Div([
    dcc.Graph(id='map'),
    dcc.Slider(
        id='year-slider',
        # Setting the min as our minimum year
        min=df["TRANSACTION_YEAR"].min(),
        # And the max as the maximum year
        max=df["TRANSACTION_YEAR"].max(),
        # I believe this sets the default value to start
        value=df["TRANSACTION_YEAR"].min(),
        # And then the marks at the bottom
        marks={str(year): str(year)
               for year in df["TRANSACTION_YEAR"].unique()},
        # Not sure why you don't need to define step
        step=None,

    )
])

# Callback adds interactivity
@app.callback(
    Output('map', 'figure'),
    [Input('year-slider', 'value')])

# Defining our update figure function, which takes our input 
# from the year slider to update the dataframe
def update_figure(selected_year = input):
    # Filtering the dataframe displayed by the year
    filtered_df = df.loc[df["TRANSACTION_YEAR"] == selected_year]

    # Defining the points represented on the map
    datamap = ([go.Scattergeo(
        type = 'scattergeo',
        locationmode = 'USA-states',
        lon = filtered_df["BUYER_LONG"],
        lat = filtered_df["BUYER_LAT"],
        # This sets the hover info, note that it has a <br> tag in the 
        # observations, which doesn't render in a Pandas dataframe but
        # works fine when you feed it through here
        text = filtered_df["TEXT"],
        hoverinfo = 'text',
        mode = 'markers',
        marker=dict(
            # Here we're setting both the size and color of each marker to
            # be dependent on the same weight column
            size=filtered_df["DOSAGE_UNIT"] / 100000,
            color=filtered_df["DOSAGE_UNIT"],
            colorscale="Viridis",
            line=dict(
                width=3,
                color='rgba(68, 68, 68, 0)'
                )
            )
        )])

    # Defining the layout of the base map and other aspects
    layoutmap = go.Layout(
        title_text = "Received Opioid Shipments in Texas, " + str(selected_year),
        showlegend=False,
        margin = go.layout.Margin(
            l = 10,
            r = 10,
            t = 50,
            b = 10
        ),
        # Here is the basemap
        geo=go.layout.Geo(
            scope='usa',
            projection=go.layout.geo.Projection(
                # Using Albers USA even though it puts Hawaii next to Texas,
                # because it shows state lines by default
                type='albers usa',
                # Scaled to just barely include all of TX
                scale=2.3
                ),
            # Centered on the center of Texas
            center={'lat': 31.9686, 'lon': -99.9018},
            showland=True,
            landcolor='rgb(243, 243, 243)',
            countrycolor='rgb(204, 204, 204)',
            )
        )

    # Defining the figure to display
    fig = {'data': datamap, 'layout': layoutmap}
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)