# %%
import pandas as pd
import numpy as np
from tps import ThinPlateSpline

# %%
# Read landmarks
landmarks = pd.read_csv("/Users/nadine/Documents/Zlatic_lab/manual_registration_1099/dff_WB/landmarksV16-1.csv", header=None)
columns = ["name", "validity", "lsm_x", "lsm_y", "lsm_z", "em_x", "em_y", "em_z"]
landmarks.columns = columns

# Get valid landmarks
valid_landmarks = landmarks[landmarks["validity"]==True]

# Get EM points of interest
em_pointsOfInterest = landmarks[landmarks["validity"]==False]

# Create the tps object
tps = ThinPlateSpline(alpha=0.0)  # 0 Regularization

# Fit the control (fixed) and moving (target) points (the code uses - https://pypi.org/project/thin-plate-spline/)
lsm_points = valid_landmarks[["lsm_x", "lsm_y", "lsm_z"]].values
em_points = valid_landmarks[["em_x", "em_y", "em_z"]].values

# Put EM points into lsm space
tps.fit(em_points, lsm_points)

# Put lsm points into EM space
#tps.fit(lsm_points, em_points)

# %%
# pick point in em-space (if tps.fit(em_points, lsm_points)) 

cur_point = np.array([[467.7832181292197,95.37989996157012,158.71022731614192]], dtype=float)
cur_point_transformed = tps.transform(cur_point)

print(cur_point_transformed, cur_point)
#%%
# n x xyz - something MC did
'''
cur_point = np.array(em_pointsOfInterest.iloc[-1][["em_x","em_y","em_z"]].values, dtype=float)
points_to_transform = np.array([
    cur_point
])
points_to_transform = em_points

em_points_transformed = tps.transform(points_to_transform)

for e, l in zip(em_points_transformed, lsm_points):
    print(e,l)

print(em_points_transformed)


print("EM", cur_point)
print("LSM-transformed", em_points_transformed)
'''

# %%
