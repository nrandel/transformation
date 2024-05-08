#%%
# Import
import pandas as pd
import numpy as np

#%%
#Read file

#temp = pd.read_csv("/Users/nadine/Documents/paper/single-larva/generated-data/cell-ID_100nodes_radius.csv")

import pandas as pd

# Define the function for coordinate transformation
def convert_coordinates_s0_to_s4(xyz_s0, calibration_factor=12):
    # Convert from nanometers to pixels (s0)
    xyz_pixels = [coord / calibration_factor for coord in xyz_s0]
    
    # Apply transformation from s0 to s4
    xyz_s4 = [coord / 16 for coord in xyz_pixels]
    
    return xyz_s4

# Read data from CSV into a DataFrame
data = pd.read_csv("/Users/nadine/Documents/paper/single-larva/generated-data/cell-ID_100nodes_radius.csv")

# Step 1: Check Column Names
print("Column Names:")
print(data.columns)

# Step 2: Check Column Types
print("\nColumn Types:")
print(data.dtypes)

# Step 3: Rename Columns if Necessary
# If column names are different, rename them here
data.rename(columns={ ' x': 'x_s0', ' y': 'y_s0', ' z': 'z_s0'}, inplace=True)

# Step 4: Handle String Conversion if Necessary
# Convert columns to numeric if they are strings
# Example: data['x'] = pd.to_numeric(data['x'], errors='coerce')

# Step 5: Print out the column names of the new (re-named) data set
print("New Column Names:")
print(data.columns)


# Apply transformation to coordinates
calibration_factor = 12  # Calibration factor for converting from nanometers to pixels
data[['x_s4', 'y_s4', 'z_s4']] = data.apply(lambda row: convert_coordinates_s0_to_s4([row['x_s0'], row['y_s0'], row['z_s0']], calibration_factor), axis=1, result_type='expand')

# Print out transformed data
print("Transformed Data:")
for index, row in data.iterrows():
    print(f"Skeleton ID: {row['skeleton_id']}, X: {row['x_s4']}, Y: {row['y_s4']}, Z: {row['z_s4']}")

# %%
