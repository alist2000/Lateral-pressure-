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
# import plotly.express as px
# import plotly.graph_objects as go
# from plotly.graph_objs import Layout
#
# # Creating the Figure instance
# fig = px.line([1, 2, 3, 4], [1, 2, 3, 2], color_discrete_sequence=["#ff97ff"])
# fig2 = px.line([2, 3, 4, 5], [-1, -2, -3, -2])
# fig.add_traces((
#     go.Line(x=np.array([5]), y=[5], mode='markers + text', marker=dict(size=15, symbol='star-triangle-up-dot')),
#     go.Line(x=np.array([5]), y=[-5], mode='markers + text', marker=dict(size=15, symbol='star-triangle-down-dot')),
#     go.Line(x=np.array([5, 5]), y=[5, -5])))
# fig.update_traces(showlegend=False)
# # fig.add_traces(
# #     go.Line(x=np.array([5]), y=[-5], mode='markers + text', marker=dict(size=15, symbol='star-triangle-down-dot')))
# # fig.add_traces(go.Line(x=np.array([5, 5]), y=[5, -5]))
#
# arrow = go.layout.Annotation(dict(
#     x=2,
#     y=5,
#     xref="x", yref="y",
#     text="",
#     showarrow=True,
#     axref="x", ayref='y',
#     ax=0,
#     ay=0,
#     arrowhead=3,
#     arrowwidth=1.5,
#     arrowcolor='rgb(255,51,0)', )
# )
# list_of_all_arrows = [arrow]
#
# fig.update_layout(annotations=list_of_all_arrows)
# fig.add_traces(
#     go.Scatter(
#         x=np.array([1]), y=np.array([5]), mode="markers", name="Ground Truth", hoverinfo="skip"
#     )
# )
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
# layout = Layout(
#     paper_bgcolor='rgba(0,0,0,0)',
#     plot_bgcolor='rgba(0,0,0,0)'
# )
# fig.update_layout(layout)
# fig.update_layout(xaxis={
#
#
#     "ticks": "outside",
#
#     "tick0": 2,
#
#     "dtick": 0.25,
#
#     "ticklen": 8,
#
#     "tickwidth": 4,
#
#     "tickcolor": "#000"
#
#   })
# fig.update_layout(xaxis={
#
#     "zeroline": True,
#
#     "showline": True,
#
#     "mirror": "ticks",
#
#     "gridcolor": "#bdbdbd",
#
#     "gridwidth": 2,
#
#     "zerolinecolor": "#969696",
#
#     "zerolinewidth": 4,
#
#     "linecolor": "#636363",
#
#     "linewidth": 6
#
# },
#
#     yaxis={
#
#         "showgrid": True,
#
#         "zeroline": True,
#
#         "showline": True,
#
#         "mirror": "ticks",
#
#         "gridcolor": "#bdbdbd",
#
#         "gridwidth": 2,
#
#         "zerolinecolor": "#969696",
#
#         "zerolinewidth": 4,
#
#         "linecolor": "#636363",
#
#         "linewidth": 6
#
#     })

# fig.update_layout(xaxis={
#
#     "zeroline": True,
#
#     "mirror": "ticks",
#
#     "zerolinecolor": "#969696",
#
#     "zerolinewidth": 4,
#
# },
#
#     yaxis={
#
#         "zeroline": True,
#
#         "mirror": "ticks",
#
#         "zerolinecolor": "#969696",
#
#         "zerolinewidth": 4,
#
#     })
# color = px.colors.qualitative.Plotly = ["#19D3F3"]
# fig.update_traces(marker=dict(color='black'))
#
# fig.plotly_update(color="black")
# # fig.update_layout(color)
# # showing the plot
#
# # add annotation
# fig.add_annotation(dict(font=dict(color='yellow',size=15),
#                                         x=0,
#                                         y=-0.12,
#                                         showarrow=False,
#                                         text="A very clear explanation",
#                                         textangle=0,
#                                         xanchor='left',
#                                         xref="paper",
#                                         yref="paper"))
#
# fig.update_layout(annotations=list_of_all_arrows)
#
# fig.show()
# _______________________ 2 azar : 10:45 _________________________
# a = atan(-1 / 1)
# b = atan(1 / 1)
# print(a)
# print(b)
# print((b - a) * 180 / np.pi)

# print(pow(10,-1))

# ______________________ 6 azar ____________________________
# # imports
# from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
# # from IPython.core.display import display, HTML
# import plotly.figure_factory as ff
# import plotly.graph_objs as go
#
# # setup
# # display(HTML("<style>.container { width:50% !important; } .widget-select > select {background-color: gainsboro;}</style>"))
# # init_notebook_mode(connected=True)
#
# #%qtconsole --style vim
#
# # dates
# StartA = '2009-01-01'
# StartB = '2009-03-05'
# StartC = '2009-02-20'
#
# FinishA='2009-02-28'
# FinishB='2009-04-15'
# FinishC='2009-05-30'
#
# LabelDateA='2009-01-25'
# LabelDateB='2009-03-20'
# LabelDateC='2009-04-01'
#
# # sample data
# df = [dict(Task="Task A", Start=StartA, Finish=FinishA),
#       dict(Task="Task B", Start=StartB, Finish=FinishB),
#       dict(Task="Task C", Start=StartC, Finish=FinishC)]
#
# # figure
# fig = ff.create_gantt(df)
#
# # add annotations
# annots =  [dict(x=LabelDateA,y=0,text="Task label A", showarrow=False, font=dict(color='white')),
#            dict(x=LabelDateB,y=1,text="Task label B", showarrow=False, font=dict(color='White')),
#            dict(x=LabelDateC,y=2,text="Task label C", showarrow=False, font=dict(color='White'))]
#
# # plot figure
# fig['layout']['annotations'] = annots
#
#
# # Step 1 - adjust margins to make room for the text
# fig.update_layout(margin=dict(t=150))
#
# # Step 2 - add line
# fig.add_shape(type='line',
#                 x0=LabelDateB,
#                 y0=0,
#                 x1=LabelDateB,
#                 y1=1,
#                 line=dict(color='black', dash='dot'),
#                 xref='x',
#                 yref='paper'
# )
#
# # Step 3 - add text with xref set to x
# # and yref set to 'paper' which will let you set
# # text outside the plot itself by specifying y > 1
# fig.add_annotation(dict(font=dict(color="black",size=10),
#                             #x=x_loc,
#                             x=LabelDateB,
#                             y=1.06,
#                             showarrow=False,
#                             text='<b>Today</b>',
#                             textangle=0,
#                             xref="x",
#                             yref="paper"
#                            ))
#
#
# fig.update_layout(
#     title_text="Academic year 2019/2020"
# )
#
# fig.show()

#  _______________ 13 azar ____________________
# a = "excel12354"
# print(a[5:])

# ___________________ 14 AZAR _______________________
# f = open("test.html", "a")
# f.write("helllllllooooo")
# f.close()
f = open("p25u44_Solution1_SurchargeLoad_Report.html", "r")
f.read()
print(f.name)
