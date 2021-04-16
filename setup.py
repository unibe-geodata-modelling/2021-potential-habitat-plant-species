#####Easy Steps To Plot Geographic Data on a Map — Python




import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Location on computer')
df.head()  # looking at the head

# BBox = ((df.longitude.min(), df.longitude.max(),
            df.latitude.min(), df.latitude.max())
### extent of figure/map display, probably not necessary as whole map has to be shown!!!

### load map as png
ruh_m = plt.imread('location and map in png?')


# plot the coordinates in the map
fig, ax = plt.subplots(figsize= ()?) # is it necessary?

ax.scatter(df.longitude,df.latitude, zorder= 1, alpha= 0.2 c='b', s=10)
#donnt know what zorder alpha, s an c is!

ax.set_title('nice title')
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])

ax.imshow(ruh-m, zorder=0, extent= BBox, aspect='equal')








