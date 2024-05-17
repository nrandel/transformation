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
