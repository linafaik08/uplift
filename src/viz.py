from sklift.metrics import uplift_curve
import plotly.graph_objs as go


def plot_uplift(df, col_target, uplifts_df, normalize=False):
    ate = df[df["treatment_group"] == "treatment"][col_target].mean() \
          - df[df["treatment_group"] == "control"][col_target].mean()
    for i, c in enumerate(uplifts_df.columns):
        x, y = uplift_curve(
            df[col_target],
            uplifts_df[c],
            df["treatment_group"].replace({"treatment": 1, "control": 0})
        )

        if normalize:
            total = max(x)
            x = x / total
            y = y / total

            x_rnd = [0, 1]
            y_rnd = [0, ate]

        else:
            x_rnd = [0, max(x)]
            y_rnd = [0, ate * max(x)]

        if i == 0:
            data = [
                go.Scatter(x=x_rnd, y=y_rnd, name="Random", marker_color='grey'),
                go.Scatter(x=x, y=y, name=c, fill='tonexty')
            ]
        else:
            data += [
                go.Scatter(x=x_rnd, y=y_rnd, name="Random", marker_color='grey', showlegend=False),
                go.Scatter(x=x, y=y, name=c, fill='tonexty')
            ]

    fig = go.Figure(data, layout={'width': 800, 'height': 600})

    return fig
