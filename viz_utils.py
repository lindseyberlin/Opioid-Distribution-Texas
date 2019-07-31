def track_shipments(df, start_lat, start_long, end_lat, end_long, weight, title):
    import plotly.graph_objects as go
    fig = go.Figure()
    max_weight = df[weight].max()

    # fig.add_trace(go.Scattergeo(
    #     locationmode = 'USA-states',
    #     lon = data_agg['REPORTER_LONG'],
    #     lat = data_agg['REPORTER_LAT'],
    #     text = data_agg['REPORTER_NAME'],
    #     hoverinfo = 'text',
    #     mode = 'markers',
    #     marker = dict(
    #         size = 2,
    #         color = 'rgb(255, 0, 0)',
    #         line = dict(
    #             width = 3,
    #             color = 'rgba(68, 68, 68, 0)'
    #         )
    #     )))

    for i in range(len(df)):
        fig.add_trace(
            go.Scattergeo(
                locationmode = 'USA-states',
                lon = [df[start_long][i], df[end_long][i]],
                lat = [df[start_lat][i], df[end_lat][i]],
                mode = 'lines',
                line = dict(width = 1, color = 'red'),
                opacity = float(df[weight][i]) / max_weight
            )
        )

    fig.update_layout(
        title_text = title,
        showlegend = False,
        geo = go.layout.Geo(
            scope = 'usa',
            projection_type = 'azimuthal equal area',
            showland = True,
            landcolor = 'rgb(243, 243, 243)',
            countrycolor = 'rgb(204, 204, 204)',
        )
    )

    fig.show()