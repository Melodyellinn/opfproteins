# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

df= pd.read_csv('C:/Users/Simplon/Documents/meloyellinn/Flask/Untitled_Folder/nutrition.csv')

app = dash.Dash(__name__)

columns_to_be_analyzed = ['fat_100g', 'energy-kcal_100g', 'sugars_100g', 'salt_100g','proteins_100g']
from plotly.subplots import make_subplots
df_proteins =df.groupby(by = ['nutriscore_grade']).agg({'fat_100g':'sum' ,'sugars_100g':'sum',
                                              'salt_100g':'sum', 'energy-kcal_100g':'sum','proteins_100g':'sum'}).reset_index()

fig = make_subplots(rows = 2, cols = 4, subplot_titles=columns_to_be_analyzed)
cnt = 0

for i in range(2):
    for j in range(3):
        if cnt == 4 :
            break
            
        fig.add_trace(go.Bar(x = df_proteins['nutriscore_grade'].to_numpy(), 
                             y = df_proteins[columns_to_be_analyzed[cnt]].to_numpy()), row = i+1, col=j+1 )
        cnt+=1
fig.update_layout(  title = 'Columns Vs Number of Purchase',font=dict(
        family="Courier New, monospace",size=12,color="#7f7f7f"),showlegend=False,autosize=True,width=1200,height=800)
fig.show()



app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)