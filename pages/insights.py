import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """        
            #### Data Science - MediZen
            This is the Data Science portion for an Application that uses Machine Learning to build a MediZen App based on User's text description which is then put through a rigorous NLP Analysis.
            #### Flowchart
            """,
        className='mb-4'),
        (
            html.Img(src='assets/FlowChart.png', style= {'width': '100%', 'display': 'inline-block'}, alt="Responsive image", className='mb-4')          
        ),
        dcc.Markdown(
            """  
             #### Project Info   
            For the Data Science portion of this application, we used this Kaggle Medi-Cabinet Dataset. 
            We used data from the Kaggle Cannabis Competition to cluster 5 categories from the description of each strain. We used K-Means Clustering to create the 5 categories. Next we pickled a vectorizer and KNN model to create an API that output the top 5 recommendations.
            """,
        className='mb-4'),
        

        
        dcc.Markdown(
            """
            #### Contributing         
            Pull requests are welcome. However for major changes, please open an issue first to discuss what you would like to change.

            Please make sure to update tests as appropriate.           
            """,
        className='mb-4'),
        
        dcc.Markdown(
            """
            #### License 
            MIT
            """,   
        className='mb-4'),
             
    ],
)

layout = dbc.Row([column1])