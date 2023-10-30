# Importando las bibliotecas necesarias
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Inicializando la aplicación
app = dash.Dash(__name__)

# Datos de ejemplo (puedes reemplazarlos con tus datos reales)
visitas_totales = 1000
tasa_conversion = 5
cpa = 10
roi = 400
canales_trafico = {'Orgánico': 40, 'Pago': 30, 'Redes Sociales': 20, 'Directo': 10}
paginas_visitadas = {'Inicio': 50, 'Productos': 30, 'Contacto': 20}
tiempo_promedio = 5
tasa_rebote = 40
segmentacion_audiencia = {'18-24': 40, '25-34': 30, '35-44': 20, '45+': 10}
dispositivos = {'Móvil': 60, 'Desktop': 30, 'Tablet': 10}

# Diseño del dashboard
app.layout = html.Div([
    html.H1('Dashboard Fravega'),

    html.Div([
        html.Label('Recolección de datos'),
        dcc.Input(value='Web fravega Octubre', type='text'),
        html.Label('Fecha de Inicio:'),
        dcc.DatePickerSingle(id='date-picker-inicio', date='2023-01-01'),
        html.Label('Fecha de Término:'),
        dcc.DatePickerSingle(id='date-picker-termino', date='2023-12-31'),
    ]),

    html.Div([
        html.Label(f'Visitas Totales: {visitas_totales}'),
        html.Br(),
        html.Label(f'Tasa de Conversión: {tasa_conversion}%'),
        html.Br(),
        html.Label(f'Costo Por Adquisición (CPA): ${cpa}'),
        html.Br(),
        html.Label(f'Retorno de Inversión (ROI): ${roi}'),
    ]),

    html.Div([
        dcc.Graph(
            id='grafico-canales',
            figure={
                'data': [{'type': 'pie', 'labels': list(canales_trafico.keys()), 'values': list(canales_trafico.values())}],
                'layout': {'title': 'Desglose de Canales de Tráfico'}
            }
        )
    ]),

    html.Div([
        dcc.Graph(
            id='grafico-paginas',
            figure={
                'data': [{'type': 'bar', 'x': list(paginas_visitadas.keys()), 'y': list(paginas_visitadas.values())}],
                'layout': {'title': 'Páginas más visitadas'}
            }
        ),
        html.Label(f'Tiempo promedio en el sitio: {tiempo_promedio} minutos'),
        html.Label(f'Tasa de rebote: {tasa_rebote}%'),
    ]),

    html.Div([
        dcc.Graph(
            id='grafico-audiencia',
            figure={
                'data': [{'type': 'pie', 'labels': list(segmentacion_audiencia.keys()), 'values': list(segmentacion_audiencia.values())}],
                'layout': {'title': 'Segmentación de Audiencia'}
            }
        ),
        dcc.Graph(
            id='grafico-dispositivos',
            figure={
                'data': [{'type': 'pie', 'labels': list(dispositivos.keys()), 'values': list(dispositivos.values())}],
                'layout': {'title': 'Dispositivos utilizados'}
            }
        ),
    ]),

    html.Div([
        html.Label('Feedback y Comentarios:'),
        dcc.Textarea(value='Comentario de ejemplo...', style={'width': '100%', 'height': 100}),
    ]),

    html.Div([
        html.Label('Recomendaciones y Acciones Futuras:'),
        dcc.Textarea(value='Recomendación de ejemplo...', style={'width': '100%', 'height': 100}),
    ]),
], style={
    'width': '1000px',
    'height': '2600px',
    'backgroundColor': '#f0f0f0',
    'border': '1px solid black',
    'padding': '10px',
    'margin': '20px'
})

if __name__ == '__main__':
    app.run_server(debug=True)
p