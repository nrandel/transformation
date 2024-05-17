#%%
import numpy as np
import skimage.io
from skimage.measure import regionprops
segs = skimage.io.imread("/Users/nadine/Desktop/1099-nuc-seg/soma_labels.tif")
regions = regionprops(segs)
centroids = np.array([r.centroid for r in regions])
print(centroids.shape)

# %%
# Save to CSV with float formatting
np.savetxt('/Users/nadine/Desktop/1099-nuc-seg/centroids.csv', centroids, delimiter=',', fmt='%.8f')
# %%
import csv
import pandas as pd

# Step 1: Open CSV File Without Headers
with open('/Users/nadine/Desktop/1099-nuc-seg/centroids_zyx.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# Step 2: Add Headers
header = ['z', 'y', 'x']  # Replace with your header names

# Insert header at the beginning of the data
data.insert(0, header)

# Step 3: Reorganize Columns
# Convert data to DataFrame
df = pd.DataFrame(data[1:], columns=data[0])

# Reorganize columns based on header
new_order = ['x', 'y', 'z']
df = df[new_order]

# Output DataFrame to CSV file with headers
df.to_csv('/Users/nadine/Desktop/1099-nuc-seg/centroids_xyz.csv', index=False)

# %%
import csv

# Step 1: Open CSV File and Read Contents
with open('/Users/nadine/Desktop/1099-nuc-seg/centroids_xyz.csv', 'r') as infile, open('/Users/nadine/Desktop/1099-nuc-seg/centroids_brain-only_z-450.csv', 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    # Step 2: Iterate through Rows and Filter
    for row in reader:
        # Step 3: Convert Value in Column z to Float and Filter
        if float(row['z']) <= 450.0:  # Convert to float and compare
            # Step 4: Save Filtered Rows to New CSV File
            writer.writerow(row)

# %%
