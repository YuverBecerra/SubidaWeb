import dash
from dash import html, dcc,Input, Output,callback
import dash_bootstrap_components as dbc 
import numpy as np

from frontend.Estructuras.area_superior.titulo import variableA
from frontend.Estructuras.area_subtitulos.subtitulos import variableB


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(variableA, md=12, style={'textAlign': 'center'}),
        dbc.Col(variableB, md=12,style={'background-color':'gold','textAlign': 'center'}),

    ])
])


#-------------------------------------
#CANAL RECTANGULAR
#-------------------------------------

# Callback para actualizar los cálculos cuando se ingresan nuevos valores de B y Y
@app.callback(
    [Output("Area_CanalR", "children"),
      Output("Perimetro_CanalR", "children"),
      Output("RH_CanalR", "children"),
      Output("T_CanalR", "children")],
    [Input("valorB", "value"),
     Input("valorY", "value")],
)

def propiedadesCR(valorB,valorY):
    # Aquí se realizan los cálculos necesarios
    
    area = (valorB*valorY)  # Cálculo del área 
    perimetro = ((2*valorY)+valorB)  # Cálculo del perímetro
    radio_hidraulico = (valorB*valorY)/(valorB+(2*valorY)) # Cálculo del radio hidráulico
    espejo_agua_T =(valorB)  # Cálculo del espejo de agua T
    return str(area), str(perimetro), str(format(radio_hidraulico, '.5f')), str(espejo_agua_T)




#-------------------------------------
#CANAL TRAPEZOIDAL
#-------------------------------------

# Callback para actualizar los cálculos cuando se ingresan nuevos valores de B y Y
@app.callback(
    [Output("Area_CanalT", "children"),
     Output("Perimetro_CanalT", "children"),
     Output("RH_CanalT", "children"),
     Output("T_CanalT", "children")],
    [Input("valorB1", "value"),
     Input("valorY1", "value"),
     Input("valorZ1", "value")]
)
def PropiedadesT(valorB1, valorY1, valorZ1):
    
    
    # Aquí se realizan los cálculos necesarios
    area2 = (valorB1+(valorZ1 * valorY1))*valorY1  # Cálculo del área
    perimetro2 = (valorB1+((2*valorY1)*((1-valorZ1**2) **(1/2))))  # Cálculo del perímetro
    radio_hidraulico2 = (valorZ1* valorY1)/(2*(1+valorZ1^2)**(1/2)) # Cálculo del radio hidráulico
    espejo_agua_T2 = valorB1+(2*valorZ1*valorY1) # Cálculo del espejo de agua T
    
    return str(area2), str(format(perimetro2, '.1f')), str(format(radio_hidraulico2, '.5f')), str(espejo_agua_T2)


#-------------------------------------
#CANAL CIRCULAR
#-------------------------------------

# Callback para actualizar los cálculos cuando se ingresan nuevos valores de B y Y
@app.callback(
    [Output("Area_CanalC", "children"),
     Output("Perimetro_CanalC", "children"),
     Output("RH_CanalC", "children"),
     Output("T_CanalC", "children")],
    [Input("ValorD", "value"),
     Input("ValorTeta", "value")]
)
def PropiedadesT(ValorD, ValorTeta):
    
    # Aquí se realizan los cálculos necesarios
    area3 = (((ValorTeta*np.sin(ValorTeta))*ValorD**2)/8) # Cálculo del área
    perimetro3 = (ValorTeta*ValorD)/2  # Cálculo del perímetro
    radio_hidraulico3 = ((1*(np.sin(ValorTeta)*ValorTeta))*(ValorD/4)) # Cálculo del radio hidráulico
    espejo_agua_T3 = ((np.sin(ValorTeta/2))*ValorD) # Cálculo del espejo de agua T
    
    return str(format(area3, '.5f')), str(perimetro3), str(format(radio_hidraulico3, '.5f')), str(format(espejo_agua_T3 , '.5f'))


#-------------------------------------
#CANAL TRIANGULAR
#-------------------------------------

# Callback para actualizar los cálculos cuando se ingresan nuevos valores de B y Y
@app.callback(
    [Output("Area_CanalTR", "children"),
     Output("Perimetro_CanalTR", "children"),
     Output("RH_CanalTR", "children"),
     Output("T_CanalTR", "children")],
    [Input("ValorY2", "value"),
     Input("ValorZ2", "value")]
)
def PropiedadesT(ValorY2, ValorZ2):
    
    # Aquí se realizan los cálculos necesarios
    area4 = (ValorZ2*ValorY2**2) # Cálculo del área
    perimetro4 = (2*ValorY2)*((1+ ValorZ2**2)**(1/2)) # Cálculo del perímetro
    radio_hidraulico4 = (ValorZ2*ValorY2)/(2*((1+ValorZ2**2)**(1/2))) # Cálculo del radio hidráulico
    espejo_agua_T4 = 2*ValorZ2*ValorY2 # Cálculo del espejo de agua T
    
    return str(area4), str(format(perimetro4, '.5f')), str(format(radio_hidraulico4, '.5f')), str(format(espejo_agua_T4, '.5f'))

if __name__ == '__main__':
    app.run_server(debug=True)