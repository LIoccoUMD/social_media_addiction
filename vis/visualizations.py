import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
# from transform.py import avgDailyUsageByCountry

# In this example we set layout.geo.visible to False to hide the base map and frame, 
# and we set layout.geo.fitbounds to 'locations'   to automatically zoom the map to show just the area of interest. 
# See the Geo map configuration documentation for more information on projections and bounds.

def orthographic(df):
    fig = go.Figure(data=go.Chloropleth(
        locations = df["Country"],
        z = df["Avg_Daily_Usage_Hours"],
        locationmode = "country names",
    ))
    fig.update_geos(projection_type="orthographic", showcountres=True, showocean=True)
    fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()
    
    


orthographic()