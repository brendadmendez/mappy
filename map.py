import plotly.express as px
import pandas as pd
from PIL import Image

# List of countries and their approximate center coordinates
data = pd.DataFrame({
    'country': ["USA", "Canada", "Brazil", "Mexico", "Uruguay", "Peru", "Argentina",
                "Colombia", "Venezuela", "France", "Spain", "Qatar", "Israel",
                "Finland", "Australia", "New Zealand", "United Kingdom", "Macedonia",
                "Romania", "Poland", "Ecuador", "Switzerland", "Netherlands"],
    'latitude': [37.0902, 56.1304, -14.235, 23.6345, -32.5228, -9.19, -38.4161,
                 4.5709, 6.4238, 46.6034, 40.4637, 25.3548, 31.0461,
                 61.9241, -25.2744, -40.9006, 55.3781, 41.6086,
                 45.9432, 51.9194, -1.8312, 46.8182, 52.1326],
    'longitude': [-95.7129, -106.3468, -51.9253, -102.5528, -55.7658, -75.0152, -63.6167,
                  -74.2973, -66.5897, 2.2137, -3.7492, 51.1839, 34.8516,
                  25.7482, 133.7751, 174.8859, -3.436, 21.7453,
                  24.9668, 19.1451, -78.1834, 8.2275, 5.2913]
})

# Create scatter map with dots for each country
fig = px.scatter_geo(data, lat='latitude', lon='longitude',
                     title='Highlighted Countries with Dots',
                     color_discrete_sequence=['purple'])

# Update geos for transparency and cleaner look
fig.update_geos(
    bgcolor='rgba(0,0,0,0)',     # Transparent background
    showcoastlines=False,
    showcountries=False,
    showframe=False,
    showland=True,
    showocean=True,
    oceancolor='rgba(0, 0, 0, 0)',
    landcolor='white'
)

# Update layout for transparent canvas
fig.update_layout(
    margin={"r": 0, "t": 0, "l": 0, "b": 0},
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    title_x=0
)

# Save the image as PNG
image_path = "worldMap.png"
fig.write_image(image_path, width=2400, height=800)

# Custom cropping dimensions
top_crop = 25
left_crop = 400
right_crop = 400
bottom_crop = 140

# Open the image using Pillow
image = Image.open(image_path)

# Get current dimensions
width, height = image.size

# Define the cropping box (left, upper, right, lower)
left = left_crop
upper = top_crop
right = width - right_crop
lower = height - bottom_crop

# Crop the image
cropped_image = image.crop((left, upper, right, lower))

# Save the cropped image
cropped_image_path = "worldMap_custom_cropped.png"
cropped_image.save(cropped_image_path)

print(f"Image saved as {cropped_image_path}")
