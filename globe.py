import plotly.graph_objects as go

fig = go.Figure(go.Scattergeo(
  lon=[-95.35, -122.33],
  lat=[29.76, 47.61],
  mode="markers+text",
  text=["Houston, Texas", "Seattle, Washington"],
  textposition="middle right",
  marker=dict(
    size=12,
    color="red",
    line=dict(width=2, color="DarkSlateGrey")
  )
))

fig.update_geos(projection_type="orthographic", showland=True, showocean=True)

fig.show()
