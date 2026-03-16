# 3DGlobe

A Python project for visualizing geographic locations on an interactive 3D globe using Plotly.

## Overview

This project uses Plotly's `Scattergeo` to display marker points on an orthographic (3D sphere) projection of Earth. You can easily add locations by specifying their latitude and longitude coordinates.

## Requirements

- Python 3.x
- plotly

## Installation

Install the required package:

```bash
pip install plotly
```

## Usage

Run the script to display the globe:

```bash
python globe.py
```

## Adding Locations

To add new locations, edit the `lon` and `lat` lists in `globe.py`:

```python
lon=[-95.35, -122.33],  # Houston, TX and Seattle, WA
lat=[29.76, 47.61],     # Corresponding latitudes
```

Each longitude value must have a corresponding latitude value in the same position.

### Example Coordinates

- **Houston, TX**: lat=29.76, lon=-95.35
- **Seattle, WA**: lat=47.61, lon=-122.33
- **New York, NY**: lat=40.71, lon=-74.01
- **Los Angeles, CA**: lat=34.05, lon=-118.24

## Customization

You can customize the appearance by modifying the marker properties:

- `size`: Marker size (default: 12)
- `color`: Marker color (default: "red")
- `line`: Marker outline properties

## Features

- Interactive 3D globe visualization
- Orthographic projection (appears as a sphere)
- Scalable location markers
- Land and ocean boundaries displayed

## License

MIT
