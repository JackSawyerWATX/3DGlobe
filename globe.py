import plotly.graph_objects as go

fig = go.Figure(go.Scattergeo(
  lon=[-95.35],
  lat=[29.76],
  mode="markers",
  marker=dict(
    size=12,
    color="red",
    line=dict(width=2, color="DarkSlateGrey")
  )
))

fig.update_geos(projection_type="orthographic", showland=True, showocean=True)

fig.show()
