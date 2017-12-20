# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 12:55:18 2017

@author: uhpad
"""

#! pip install dash==0.19.0  # The core dash backend
#! pip install dash-renderer==0.11.1  # The dash front-end
#! pip install dash-html-components==0.8.0  # HTML components
#! pip install dash-core-components==0.14.0  # Supercharged components
#! pip install plotly --upgrade  # Latest Plotly graphing library


import dash
import dash_core_components as dcc
import dash_html_components as html
#import dash_renderer


app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Simple Dash Application'),

    html.Div(children='''
        Dash: A simple web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                 {'x': [1, 2, 3], 'y': [11, 8,9], 'type': 'bar', 'name': u'Toronto'},
            ],
            'layout': {
                'title': 'Data Visualization using Python Dash'
            }
        }
    ),

   
   dcc.Graph(
        id='example-graph2',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [11, 8, 4], 'type': 'line', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [6, 6, 10], 'type': 'line', 'name': u'Montréal'},
                 {'x': [1, 2, 3], 'y': [11, 8,9], 'type': 'line', 'name': u'Toronto'},
            ],
            'layout': {
                'title': 'Second Data Visualization using Python Dash'
            }
        }
    )


])

if __name__ == '__main__':
   
 app.run_server()
 
 