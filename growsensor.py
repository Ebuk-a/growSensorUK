import pandas as pd
import matplotlib.pyplot as plt

#Read the data
grow_df = pd.read_csv('resources/GrowLocations.csv')

#Data Cleaning: Rename the wrongly named columns
grow_df.rename(columns={"Latitude": "Longitude", "Longitude": "Latitude"}, inplace=True)

#Data Cleaning: Filtering the necesarry boundary from the data
filtered_grow_df = grow_df[(grow_df['Latitude'] >= 50.681) & (grow_df['Latitude'] <= 57.985) 
                        & (grow_df['Longitude'] >= -10.592) & (grow_df['Longitude'] <= 1.6848)]

# Creating the plot variables (x, y and area of plot)
x_axis = filtered_grow_df['Latitude']
y_axis= filtered_grow_df['Longitude']
figure, ax = plt.subplots()


#Reading the UK image and plotting the cleaned data on the uk map, and saving output
ax.scatter(y_axis, x_axis)
ukmap = plt.imread('resources/map7.png')
plt.title("Plotting Grow Sensor Data")
plt.xlabel('Longitude')
plt.ylabel('Latitude')
ax.imshow(ukmap, extent = (-10.5, 1.8, 50.6, 57.8))
figure.savefig('ebukaGrowLocationsMaps')
