import numpy as np
import plotly.express as px
import plotly.graph_objects as go


def plotter2(unit_system, h, sigma_h, depth_list, lateral_pressure, centroid):
    if unit_system == "us":
        pressure_unit = "psf"
        lenght_unit = "ft"
    else:
        pressure_unit = "Pa"
        lenght_unit = "m"
    depth_array = np.array(depth_list)
    sigma_h_array = np.array(sigma_h)
    plot = px.line(y=depth_array, x=sigma_h_array).update_layout(title_text="Lateral Pressure",
                                                                 xaxis_title=f"Ϭh ({pressure_unit})",
                                                                 yaxis_title=f"Z ({lenght_unit})",
                                                                 xaxis={"side": "top"})
    j = int(len(depth_list) / 5)
    plot['layout']['yaxis']['autorange'] = "reversed"
    result = go.layout.Annotation(dict(
        x=0.01,
        y=centroid,
        xref="x", yref="y",
        text="",
        showarrow=True,
        axref="x", ayref='y',
        ax=max(sigma_h_array),
        ay=centroid,
        arrowhead=3,
        arrowwidth=4,
        arrowcolor='rgb(255,51,0)', )
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
        arrowcolor='rgb(0,128,255)', )
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
        arrowcolor='rgb(0,128,255)', )
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
        arrowcolor='rgb(0,128,255)', )
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
        arrowcolor='rgb(0,128,255)', )
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
        arrowcolor='rgb(0,128,255)', )
    )
    list_of_all_arrows = [result, arrow1, arrow2, arrow3, arrow4, arrow5]

    plot.update_layout(annotations=list_of_all_arrows)
    plot.write_html(f"output.html",
                    full_html=False,
                    include_plotlyjs='cdn')
    plot.show()
    return None
