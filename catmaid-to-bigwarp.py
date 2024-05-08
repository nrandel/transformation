# %%
import pandas as pd
import numpy as np
from tps import ThinPlateSpline

# %%

# Read landmarks bigwarp
landmarks_bw = pd.read_csv("/Users/nadine/Documents/Zlatic_lab/manual_registration_1099/Albert/1099/landmarks_1099_nr_V16.csv", header=None)
columns = ["name", "validity", "lsm_x", "lsm_y", "lsm_z", "em_x", "em_y", "em_z"]
landmarks_bw.columns = columns

# %%
# Read ladmarks from Catmaid
df = pd.read_csv("/Users/nadine/Documents/paper/single-larva/generated-data/cell-ID_100nodes_radius.csv")

# Print out the column names to inspect
print("Columns in the dataframe:", df.columns)

# Define the subset of columns you want to keep
desired_columns = ['skeleton_id', ' x', ' y', ' z'] 

# Create a new dataframe with only the desired columns
landmarks_cat = df[desired_columns]

# %%
# Plot x,y,z in 3D space of catmaid

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Read the CSV file into a dataframe
df = pd.read_csv("/Users/nadine/Documents/paper/single-larva/generated-data/cell-ID_100nodes_radius.csv")

# Define the subset of columns (x, y, z coordinates)
desired_columns = [' x', ' y', ' z']

# Create a new dataframe with only the desired columns
coordinates_df = df[desired_columns]

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Extract x, y, z coordinates
x = coordinates_df[' x']
y = coordinates_df[' y']
z = coordinates_df[' z']

# Plot points
ax.scatter(x, y, z)

# Set labels and title
ax.set_xlabel(' X')
ax.set_ylabel(' Y')
ax.set_zlabel(' Z')
ax.set_title('3D Plot of catmaid xyz')

# Show plot
plt.show()

# %%
# Plot multiple pointclouds in 3D

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Read the first CSV file into a dataframe
df1 = pd.read_csv("/Users/nadine/Documents/paper/single-larva/generated-data/cell-ID_100nodes_radius.csv")


# Read the second CSV file into a dataframe
df2 = pd.read_csv("/Users/nadine/Documents/Zlatic_lab/manual_registration_1099/Albert/1099/landmarks_1099_nr_V16.csv", header=None)
columns = ["name", "validity", "lm_x", "lm_y", "lm_z", " x", " y", " z"]
df2.columns = columns

# Define the subset of columns (x, y, z coordinates)
desired_columns = [' x', ' y', ' z']

# Create dataframes with only the desired columns
coordinates_df1 = df1[desired_columns]
coordinates_df2 = df2[desired_columns]

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Extract x, y, z coordinates for each dataset
x1, y1, z1 = coordinates_df1[' x'], coordinates_df1[' y'], coordinates_df1[' z']
x2, y2, z2 = coordinates_df2[' x'], coordinates_df2[' y'], coordinates_df2[' z']

# Plot points for the first dataset
ax.scatter(x1, y1, z1, c='b', label='catmaid em')

# Plot points for the second dataset
ax.scatter(x2, y2, z2, c='r', label='bigwarp em')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Plot of em coordinates')

# Add legend
ax.legend()

# Show plot
plt.show()

# %%
#Test lm and em from bigwarp landmark file
# Read the first CSV file into a dataframe
df2 = pd.read_csv("/Users/nadine/Documents/Zlatic_lab/manual_registration_1099/Albert/1099/landmarks_1099_nr_V16.csv", header=None)
columns = ["name", "validity", " x", " y", " z", "em_x", "em_y", "em_z"]
df2.columns = columns

# Read the second CSV file into a dataframe
df2 = pd.read_csv("/Users/nadine/Documents/Zlatic_lab/manual_registration_1099/Albert/1099/landmarks_1099_nr_V16.csv", header=None)
columns = ["name", "validity", "lm_x", "lm_y", "lm_z", " x", " y", " z"]
df2.columns = columns

# Define the subset of columns (x, y, z coordinates)
desired_columns = [' x', ' y', ' z']

# Create dataframes with only the desired columns
coordinates_df1 = df1[desired_columns]
coordinates_df2 = df2[desired_columns]

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Extract x, y, z coordinates for each dataset
x1, y1, z1 = coordinates_df1[' x'], coordinates_df1[' y'], coordinates_df1[' z']
x2, y2, z2 = coordinates_df2[' x'], coordinates_df2[' y'], coordinates_df2[' z']

# Plot points for the first dataset
ax.scatter(x1, y1, z1, c='b', label='bigwarp lm')

# Plot points for the second dataset
ax.scatter(x2, y2, z2, c='r', label='bigwarp em')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Plot of bigwarp coordinates')

# Add legend
ax.legend()

# Show plot
plt.show()
# %%
# %%
# Plot x,y,z in 3D space of bigwarp

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Read the second CSV file into a dataframe
df = pd.read_csv("/Users/nadine/Documents/Zlatic_lab/manual_registration_1099/Albert/1099/landmarks_1099_nr_V16.csv", header=None)
columns = ["name", "validity", " x", " y", " z", "em_x", "em_y", "em_z"]
df.columns = columns

# Define the subset of columns (x, y, z coordinates)
desired_columns = [' x', ' y', ' z']
# Define the subset of columns (x, y, z coordinates)
desired_columns = [' x', ' y', ' z']

# Create a new dataframe with only the desired columns
coordinates_df = df[desired_columns]

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Extract x, y, z coordinates
x = coordinates_df[' x']
y = coordinates_df[' y']
z = coordinates_df[' z']

# Plot points
ax.scatter(x, y, z)

# Set labels and title
ax.set_xlabel(' X')
ax.set_ylabel(' Y')
ax.set_zlabel(' Z')
ax.set_title('3D Plot of lm xyz')

# Show plot
plt.show()
# %%
