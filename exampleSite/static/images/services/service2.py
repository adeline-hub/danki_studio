import plotly.graph_objects as go

import numpy as np
import pandas as pd
import scipy

from scipy import signal

np.random.seed(1)

x = np.linspace(0, 10, 100)
y = np.sin(x)
noise = 2 * np.random.random(len(x)) - 1 # uniformly distributed between -1 and 1
y_noise = y + noise

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x,
    y=y,
    mode='markers',
    marker=dict(size=2, color='black'),
    name='Sine'
))

fig.add_trace(go.Scatter(
    x=x,
    y=y_noise,
    mode='markers',
    marker=dict(
        size=6,
        color='#33FFA2',
        symbol='circle-open'
    ),
    name='Noisy Sine'
))

fig.add_trace(go.Scatter(
    x=x,
    y=signal.savgol_filter(y_noise,
                           53, # window size used for filtering
                           3), # order of fitted polynomial
    mode='markers',
    marker=dict(
        size=6,
        color='#FF33FF',
        symbol='triangle-up'
    ),
    name='Savitzky-Golay'
))


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
        bgcolor='rgba(0,0,0,0)' 
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=0, r=0, b=0, t=0),
    showlegend=False
)
fig.write_image("danki_linspace.png", width=1000, height=1000)
fig.show()