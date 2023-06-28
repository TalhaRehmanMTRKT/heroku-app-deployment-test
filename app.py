import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import random
app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1("Random Number Generator"),
        html.Button("Generate", id="generate-button", n_clicks=0),
        html.Div(id="output-div")
    ]
)

@app.callback(
    Output("output-div", "children"),
    Input("generate-button", "n_clicks")
)
def generate_random_number(n_clicks):
    if n_clicks > 0:
        random_number = random.randint(1, 100)
        return f"Generated number: {random_number}"
    else:
        return ""

if __name__ == "__main__":
    app.run_server(debug=True)
