import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

def orthographic():
    fig = go.Figure(go.Scattergeo())
    fig.update_geos(projection_type="orthographic")
    fig.update_geos(showcountries=True)
    fig.update_geos(showocean=True)
    fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()
    
orthographic()