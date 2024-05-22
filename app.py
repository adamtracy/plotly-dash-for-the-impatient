import dash
from dash import dcc, html
import plotly.express as px
from dash.dependencies import Input, Output

# Initialize the Dash app
app = dash.Dash(__name__)

# Create some sample data
df = px.data.iris()

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Dropdown(
        id='species-dropdown',
        options=[
            {'label': species, 'value': species}
            for species in df['species'].unique()
        ],
        value=df['species'].unique()[0]
    ),

    dcc.Graph(
        id='example-graph',
    )
])

# Define callback to update graph
@app.callback(
    Output('example-graph', 'figure'),
    [Input('species-dropdown', 'value')]
)
def update_figure(selected_species):
    filtered_df = df[df['species'] == selected_species]
    fig = px.scatter(filtered_df, x='sepal_width', y='sepal_length', color='species')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
