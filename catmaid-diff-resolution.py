# Transformation guideline:
# To transform from s0 to s4, the scale levels (the s0, s1, s2, ...) are powers of two. 
# So s4 means pow(2, 4) = 16, which means 1/16th.
# Another transformation is the calibration. Coordinates in CATMAID world space are calibrated, 
# in nanometers. So if the volume was imaged at e.g., 12x12x12, you will have to consider this when 
# mapping. First, map the s0 coordinates from calibrated space in nanometers to pixels. Do this by, 
# in this example, dividing by 12. Second, apply the s0 to s4 transform, which means further divide by 
# 16.

#%%
# Transform s0 to s4

# Import
import pandas as pd

# Define the function for coordinate transformation
def convert_coordinates_s0_to_s4(xyz_s0, calibration_factor=12):
    # Convert from nanometers to pixels (s0)
    xyz_pixels = [coord / calibration_factor for coord in xyz_s0]
    
    # Apply transformation from s0 to s4
    xyz_s4 = [coord / 16 for coord in xyz_pixels]
    
    return xyz_s4

# Read data from CSV into a DataFrame
data = pd.read_csv("/Users/nadine/Documents/Zlatic_lab/1099-nuc-seg/S0-skeleton_coordinates_soma.csv")

# Inspect column names to identify any discrepancies
print("Column Names:")
print(data.columns)

# Define the subset of columns you want to keep
desired_columns = ['skeleton_id', 'x', 'y', 'z'] 

# Create a new dataframe with only the desired columns
data = data[desired_columns]

# Display the headers of the skeleton_coordinates_soma file
print(f"Headers of the skeleton_coordinates_soma CSV file: {data.columns.tolist()}")


# Step 1: Check Column Names
print("Column Names:")
print(data.columns)

# Step 2: Check Column Types
print("\nColumn Types:")
print(data.dtypes)

# Step 3: Rename Columns if Necessary
# If column names are different, rename them here
data.rename(columns={ 'x': 'x_s0', 'y': 'y_s0', 'z': 'z_s0'}, inplace=True)

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

# Save the transformed data to a CSV file
data.to_csv('/Users/nadine/Documents/Zlatic_lab/1099-nuc-seg/S4-skeleton_coordinates_soma.csv', index=False)
print("Transformed data saved to 'transformed_data.csv'")


# %%
# Transform s4 to s0

# Import
import pandas as pd

# Define the function for coordinate transformation
def convert_coordinates_s4_to_s0(xyz_s4, calibration_factor=12):
    # Apply transformation from s4 to s0
    xyz_pixels = [coord * 16 for coord in xyz_s4]
    
    # Convert from pixels to nanometers (s0)
    xyz_s0 = [coord * calibration_factor for coord in xyz_pixels]
    
    return xyz_s0

# Read data from CSV into a DataFrame
data = pd.read_csv("/Users/nadine/Documents/Zlatic_lab/1099-nuc-seg/centroids_brain-only_z-450.csv")

# Define the subset of columns you want to keep
desired_columns = ['x', 'y', 'z'] 

# Create a new dataframe with only the desired columns
data = data[desired_columns]

# Step 1: Check Column Names
print("Column Names:")
print(data.columns)

# Step 2: Check Column Types
print("\nColumn Types:")
print(data.dtypes)

# Step 3: Rename Columns if Necessary
# If column names are different, rename them here
data.rename(columns={ 'x': 'x_s4', 'y': 'y_s4', 'z': 'z_s4'}, inplace=True)

# Step 4: Handle String Conversion if Necessary
# Convert columns to numeric if they are strings
# Example: data['x'] = pd.to_numeric(data['x'], errors='coerce')

# Step 5: Print out the column names of the new (re-named) data set
print("New Column Names:")
print(data.columns)

# Apply transformation to coordinates
calibration_factor = 12  # Calibration factor for converting from pixels to nanometers
data[['x_s0', 'y_s0', 'z_s0']] = data.apply(lambda row: convert_coordinates_s4_to_s0([row['x_s4'], row['y_s4'], row['z_s4']], calibration_factor), axis=1, result_type='expand')

# Print out transformed data
print("Transformed Data:")
for index, row in data.iterrows():
    print(f"X: {row['x_s0']}, Y: {row['y_s0']}, Z: {row['z_s0']}")

# Save the transformed data to a CSV file
data.to_csv('/Users/nadine/Documents/Zlatic_lab/1099-nuc-seg/S0-centroids_brain-only_z-450.csv', index=False)
print("Transformed data saved to 'transformed_data.csv'")


# %%
# Concatenate csv files with corresponding rows
# Rename columns if necessary

import pandas as pd

# Paths to the input CSV files
file1_path = '/Users/nadine/Documents/Zlatic_lab/1099-nuc-seg/S0-skeleton_coordinates_soma.csv'
file2_path = '/Users/nadine/Documents/Zlatic_lab/1099-nuc-seg/S4-skeleton_coordinates_soma.csv'

# Load the input CSV files
df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)

# Rename headers using a dictionary
rename_dict1 = {'x': 'x_S0', 'y': 'y_S0', 'z': 'z_S0'}
rename_dict2 = {'x': 'x_S4', 'y': 'y_S4', 'z': 'z_S4'}

df1.rename(columns=rename_dict1, inplace=True)
df2.rename(columns=rename_dict2, inplace=True)

# Concatenate the DataFrames along columns
concatenated_df = pd.concat([df1, df2], axis=1)

# Display the concatenated DataFrame
print(concatenated_df)

# Save the concatenated DataFrame to a new CSV file
output_csv_path = '/path/to/concatenated_output.csv'
concatenated_df.to_csv(output_csv_path, index=False)

print(f"Concatenated output saved to {output_csv_path}")
