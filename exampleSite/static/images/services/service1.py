import plotly.graph_objects as go
import numpy as np

t = np.linspace(0, 20, 100)
x, y, z = np.cos(t), np.sin(t), t

fig = go.Figure(data=[go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    marker=dict(
        size=12,
        color='#33FFA2', 
        opacity=0.8
    )
)])

invisible_axis = dict(
    showbackground=False, 
    showgrid=False,       
    showline=False,       
    showticklabels=False, 
    title='',             
    visible=False         
)
fig.update_layout(
    scene=dict(
        xaxis=invisible_axis,
        yaxis=invisible_axis,
        zaxis=invisible_axis,
        bgcolor='rgba(0,0,0,0)' 
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=0, r=0, b=0, t=0),
    showlegend=False
)
fig.write_image("danki_helix.png", width=1000, height=1000)
fig.show()