import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.graph_objs import Layout


def plotter2(unit_system, h, sigma_h, depth_list, lateral_pressure, centroid):
    if unit_system == "us":
        pressure_unit = "psf"
        lenght_unit = "ft"
    else:
        pressure_unit = "Pa"
        lenght_unit = "m"
    depth_array = np.array(depth_list)
    sigma_h_array = np.array(sigma_h)
    plot = px.line(y=depth_array, x=sigma_h_array, color_discrete_sequence=["#595959"]).update_layout(
        xaxis_title=f"Ϭh ({pressure_unit})",
        yaxis_title=f"Z ({lenght_unit})",
        xaxis={"side": "top",
               "zeroline": True,
               "mirror": "ticks",
               "zerolinecolor": "#969696",
               "zerolinewidth": 4, },
        yaxis={"zeroline": True,
               "mirror": "ticks",
               "zerolinecolor": "#969696",
               "zerolinewidth": 4}
    )
    j = int(len(depth_list) / 5)
    plot['layout']['yaxis']['autorange'] = "reversed"
    plot['layout']['xaxis']['range'] = [-max(sigma_h_array) / 20, max(sigma_h_array) + max(sigma_h_array) / 20]

    # show maximum
    plot.add_traces(
        go.Scatter(
            x=np.array(max(sigma_h_array)), y=np.array(depth_array[np.where(sigma_h_array == max(sigma_h_array))]),
            mode="markers", name="Max", hoverinfo="skip"
        )
    )
    # color and size of maximum point
    plot.update_traces(marker=dict(color='red', size=8), legendgroup="maximum")

    # show some vector to look better
    result = go.layout.Annotation(dict(
        x=0.01,
        y=centroid,
        opacity=0.7,
        xref="x", yref="y",
        text="",
        showarrow=True,
        axref="x", ayref='y',
        ax=max(sigma_h_array),
        ay=centroid,
        arrowhead=3,
        arrowwidth=3,
        arrowcolor='#e6192b', )
    )
    arrow1 = go.layout.Annotation(dict(
        x=0.01,
        y=depth_list[j],
        xref="x", yref="y",
        text="",
        showarrow=True,
        axref="x", ayref='y',
        ax=sigma_h[j],
        ay=depth_list[j],
        arrowhead=3,
        arrowwidth=1.5,
        arrowcolor='#595959', )
    )
    arrow2 = go.layout.Annotation(dict(
        x=0.01,
        y=depth_list[2 * j],
        xref="x", yref="y",
        text="",
        showarrow=True,
        axref="x", ayref='y',
        ax=sigma_h[2 * j],
        ay=depth_list[2 * j],
        arrowhead=3,
        arrowwidth=1.5,
        arrowcolor='#595959', )
    )
    arrow3 = go.layout.Annotation(dict(
        x=0.01,
        y=depth_list[3 * j],
        xref="x", yref="y",
        text="",
        showarrow=True,
        axref="x", ayref='y',
        ax=sigma_h[3 * j],
        ay=depth_list[3 * j],
        arrowhead=3,
        arrowwidth=1.5,
        arrowcolor='#595959', )
    )
    arrow4 = go.layout.Annotation(dict(
        x=0.01,
        y=depth_list[4 * j],
        xref="x", yref="y",
        text="",
        showarrow=True,
        axref="x", ayref='y',
        ax=sigma_h[4 * j],
        ay=depth_list[4 * j],
        arrowhead=3,
        arrowwidth=1.5,
        arrowcolor='#595959', )
    )
    arrow5 = go.layout.Annotation(dict(
        x=0.01,
        y=depth_list[5 * j],
        xref="x", yref="y",
        text="",
        showarrow=True,
        axref="x", ayref='y',
        ax=sigma_h[5 * j],
        ay=depth_list[5 * j],
        arrowhead=3,
        arrowwidth=1.5,
        arrowcolor='#595959', )
    )
    list_of_all_arrows = [result, arrow1, arrow2, arrow3, arrow4, arrow5]

    plot.update_layout(annotations=list_of_all_arrows)

    # add annotation for result force
    plot.add_traces((
        go.Line(x=[max(sigma_h_array) + + max(sigma_h_array) / 80], y=[0], mode='markers + text',
                marker=dict(symbol='triangle-up'), hoverinfo='skip'),
        go.Line(x=[max(sigma_h_array) + max(sigma_h_array) / 80], y=[centroid], mode='markers + text',
                marker=dict(symbol='triangle-down'), hoverinfo='skip', opacity=0.7)
    ))
    plot.update_traces(showlegend=False, marker=dict(color="#e6192b", size=7), legendgroup="dimention")
    plot.add_traces(
        go.Line(x=[max(sigma_h_array) + max(sigma_h_array) / 80, max(sigma_h_array) + max(sigma_h_array) / 80],
                y=[0, centroid], mode="lines", marker=dict(color="#e6192b", size=3), hoverinfo='skip', opacity=0.7))
    plot.update_traces(showlegend=False, legendgroup="dimention")
    # add text for annotations
    plot.add_annotation(dict(font=dict(color="#595959", size=16),
                             # x=x_loc,
                             x=max(sigma_h_array) + max(sigma_h_array) / 20,
                             y=centroid / 2,
                             showarrow=False,
                             text='<b>Zr</b>',
                             textangle=0
                             # xref="x",
                             # yref="paper"
                             ))
    plot.add_annotation(dict(font=dict(color="#595959", size=20),
                             # x=x_loc,
                             x=max(sigma_h_array) + max(sigma_h_array) / 20,
                             y=centroid,
                             showarrow=False,
                             text='<b style="font-size: 0.8vw">Pr</b>',
                             textangle=0
                             # xref="x",
                             # yref="paper"
                             ))

    # changing background color
    layout = Layout(
        paper_bgcolor='#ffffff',
        plot_bgcolor='#ffffff'
    )
    plot.update_layout(layout)

    # plot.show()
    return plot
