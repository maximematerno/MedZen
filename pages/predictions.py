import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
from app import app
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer



column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions
            """, className='mb-3'
        ),
        dcc.Input(id='tokens',
    placeholder='Enter a value...',
    type='text',
    value=''
),  
               
        # for _ in ALLOWED_TYPES
    ],
    md=7,
)

column2 = dbc.Col(
    [
        html.H2('Strain Recommender', className='mb-5'), 
        html.Div(id='prediction-content', className='lead'),
        html.Img(src='assets/meditation1.jpeg', className='img-fluid')
    ]
)

layout = dbc.Row([column1, column2])


@app.callback(
    Output('prediction-content', 'children'),
    [Input('tokens','value')],
)


# def predict(tokens):
#     # df = pd.DataFrame(
#     #     columns=['tokens'], 
#     #     data=[[tokens.astype(str)]]
#     # )
#     y_pred = pipeline.predict([tokens])[0]
#     return f'{y_pred:10,.2f} Strain'

def predict(tokens):
    df = pd.read_csv('notebooks/cannabis.csv')
    df = df.dropna(subset = ['Description'])

    tfidf = pickle.load(open("notebooks/vect_01.pkl", "rb"))
    nn = pickle.load(open("notebooks/knn_01.pkl", "rb"))

   # Transform
    request = pd.Series(tokens)
    request_sparse = tfidf.transform(request)

    # Send to df
    request_tfidf = pd.DataFrame(request_sparse.todense())

    # Return a list of indexes
    #top5 = nn.kneighbors([request_tfidf][0], n_neighbors=5)[1][0].tolist()
    results = nn.kneighbors([request_tfidf][0], n_neighbors=5)
    
    # Send recomendations to DataFrame
    #recommendations_df = df.iloc[top5]
    
    #string = str(recommendations_df['Strain'])
    indexes = results[1]

    # result1 = "{}: {}\n".format(df['Strain'][indexes[0][0]],df['Description'][indexes[0][0]])
    # result2 = "{}: {}".format(df['Strain'][indexes[0][1]],df['Description'][indexes[0][1]])

    result1 = "{}".format(df['Strain'][indexes[0][0]])
    # result2 = "{}".format(df['Strain'][indexes[0][1]])


    return result1

