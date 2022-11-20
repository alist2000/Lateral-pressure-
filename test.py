import numpy as np
from math import *
from scipy import integrate
import decimal

# number = 1.2555
# number2 = 554535.1
# print(cos(np.pi))
# deci = (decimal.Decimal(number).as_tuple())
# print(deci.exponent)
# print(deci.sign)
# print(deci.digits)
# print(str(number2)[::-1].find('.'))  # count number of decimal
# _______________________ 15 aban 12:30 ____________________________
# print(atan(1/1))
# print(pow(10,-1))
# _______________________ 22 aban 12:50 ____________________________
# a = np.array([0,1,2,3])
# b = np.array([0,1,2,3])
# c = np.array([i for i in range(4)])
# print(c)
# c = np.append(c,10)
# print(c)
# print(a*b)
# _________________________ 29 aban 12:30 ______________________________
import plotly.express as px
import plotly.graph_objects as go

# Creating the Figure instance
fig = px.line([1, 2, 3, 4],[1, 2, 3, 2])
arrow = go.layout.Annotation(dict(
    x=2,
    y=5,
    xref="x", yref="y",
    text="",
    showarrow=True,
    axref="x", ayref='y',
    ax=0,
    ay=0,
    arrowhead=3,
    arrowwidth=1.5,
    arrowcolor='rgb(255,51,0)', )
)
list_of_all_arrows = [arrow]

fig.update_layout(annotations=list_of_all_arrows)
# fig.add_annotation(
#     x='2020-03-21'
#     , y=145+1
#     , text=f'Mar 21<br>First day of spring'
#     , yanchor='bottom'
#     , showarrow=False
#     , arrowhead=1
#     , arrowsize=1
#     , arrowwidth=2
#     , arrowcolor="#636363"
#     , ax=-20
#     , ay=-30
#     , font=dict(size=12, color="orange", family="Sans Serif")
#     , align="left"
#     ,)
# showing the plot
fig.show()
