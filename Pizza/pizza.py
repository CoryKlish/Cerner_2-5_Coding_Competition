import pandas as pd
import folium
from folium.plugins import HeatMap

#cerner_2^5_2019

fields = ['name', 'city', 'country', 'postalCode', 'latitude', 'longitude', 'menus.amountMax', 'menus.amountMin']
df = pd.read_csv('pizza_data.csv', usecols = fields).drop_duplicates()
us_map = folium.Map(location=[40, -98], zoom_start=5)
df['latitude'] = df['latitude'].astype(float)
df['longitude'] = df['longitude'].astype(float)
heat_df = df[['latitude', 'longitude']]
heat_data = [[row['latitude'],row['longitude']] for index, row in heat_df.iterrows()]

# Heat map of pizza concentrations in USA...saved in current directory as 'map.html'
HeatMap(heat_data).add_to(us_map)
us_map.save('map.html')

# Top 50 highest pizza concentrations
grouped = df.groupby('city')
top50 = grouped['city'].count().reset_index(name='count').sort_values(['count'], ascending = False).head(50)
print(top50)

