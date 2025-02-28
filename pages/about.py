import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [   
    
        (
            html.Img(src='assets/Vera.jpg', style= {'width': '100%', 'display': 'inline-block'}, alt="Responsive image", className='mb-4')          
        ),
        dcc.Markdown(
            """
            #### Vera Mendes        
            #### Data Scientist 
            """,
        className='mb-4'),
        # dcc.Markdown(
        #     """  
        #       #### Data Scientist - Yelp Feelers  
        #     """,
        # className='mb-4'),
        # (
        #     html.Img(src='assets/oscar.jpeg', style= {'width': '100%', 'display': 'inline-block'}, alt="Responsive image", className='mb-4')          
        # ),
        
        # dcc.Markdown(
        #     """ 
        #     #### Data Scientist - Yelp Feelers        
        #     """,
        # className='mb-4'),
        # (
        #     html.Img(src='assets/maxime.jpg', style= {'width': '100%', 'display': 'inline-block'}, alt="Responsive image", className='mb-4')          
        # ),
        
             
    ],
)

column2 = dbc.Col(
    [   
       (
            html.Img(src='assets/Tobias.png', style= {'width': '100%', 'display': 'inline-block'}, alt="Responsive image", className='mb-4')          
        ),
        dcc.Markdown(
            """ 
            #### Tobias Reaper       
            #### Data Scientist 
            """,
        className='mb-4'),
    ]
)

column3 = dbc.Col(
    [  
        (
            html.Img(src='assets/maxime.jpg', style= {'width': '100%', 'display': 'inline-block'}, alt="Responsive image", className='mb-4')          
        ),
        dcc.Markdown(
            """ 
            #### Maxime Vacher-Materno       
            #### Data Scientist 
            """,
        className='mb-4'),
    ]
)

layout = dbc.Row([column1,column2,column3])