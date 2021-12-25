import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State

def create_figure(color_A, color_B, color_U):
	fig = go.Figure()

	fig.update_xaxes(
		showticklabels=False,
		showgrid=False,
		zeroline=False
	)

	fig.update_yaxes(
		showticklabels=False,
		showgrid=False,
		zeroline=False
	)

	fig.add_shape(
		type="circle",
		line_color="black",
		fillcolor=color_A,
		x0=0, y0=0, x1=3, y1=4
	)

	fig.add_shape(
		type="circle",
		line_color="black",
		fillcolor=color_B,
		x0=2, y0=0, x1=5, y1=4
	)

	fig.add_trace(go.Scatter(
		x=[0, 0.5, 4.5],
		y=[0, 3.8, 3.8],
		text=["U", "A", "B"],
		mode="text",
		textfont=dict(size=18)
	))

	fig.update_shapes(xref="x", yref="y")

	fig.update_layout(
		margin=dict(l=20, r=20, b=100, t=20),
		height=450, width=600,
		plot_bgcolor=color_U
	)
	return fig;

fig = create_figure("rgba(0,0,0,0)", "rgba(0,0,0,0)", "rgba(0,0,0,0)")

app = dash.Dash(__name__)

server = app.server

app.layout = html.Div([
	html.Div([
		html.Label("Basic operations with sets")],
		style={
			"display": "block", "fontSize": "1.6rem"
		}
	),
	html.Div([
		html.P("Not completed options are disabled")
	]),
	dcc.Dropdown(
		id="operations-dropdown",
		options=[
			{"label": "Choose:", "value": ""},
			{"label": "Union", "value": "union"},
			{"label": "Complement of B in A", "value": "complement-of-B-in-A"},
			{"label": "Complement of A in U", "value": "complement-of-A-in-U"},
			{"label": "Complement of B in U", "value": "complement-of-B-in-U"},
			{"label": "Intersection", "value": "intersection", "disabled": True},
			{"label": "Complement of A in B", "value": "complement-of-A-in-B", "disabled": True},
			{"label": "Symmetric difference of A and B", "value": "symmetric-difference", "disabled": True}
		],
		value=""
	),
	dcc.Graph(id="main-graph", figure=fig)
])

@app.callback(
	Output('main-graph', 'figure'),
	[Input('operations-dropdown', 'value')]
)

def update_figure(value):
	if value == 'union':
		return create_figure("#01a3a4", "#01a3a4", "white")
	if value == 'complement-of-B-in-A':
		return create_figure("#01a3a4", "white", "white")
	if value == 'complement-of-A-in-U':
		return create_figure("white", "rgba(0,0,0,0)", "#01a3a4")
	if value == 'complement-of-B-in-U':
		return create_figure("rgba(0,0,0,0)", "white", "#01a3a4")
	return create_figure("rgba(0,0,0,0)", "rgba(0,0,0,0)", "rgba(0,0,0,0)")


if __name__ == '__main__':
	app.run_server(debug=True)
