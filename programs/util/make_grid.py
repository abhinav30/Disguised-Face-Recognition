import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
try:
    from PIL import Image
except ImportError:
    import Image

# Open image file
image = Image.open('P1_1.jpeg')
my_dpi=72.

# Set up figure
fig=plt.figure(figsize=(float(image.size[0])/my_dpi,float(image.size[1])/my_dpi),dpi=my_dpi)
ax=fig.add_subplot(111)

# Remove whitespace from around the image
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)

# Set the gridding interval: here we use the major tick interval
xInterval=26.
yInterval=30.
loc1 = plticker.MultipleLocator(base=xInterval)
loc2 = plticker.MultipleLocator(base=yInterval)
ax.xaxis.set_major_locator(loc1)
ax.yaxis.set_major_locator(loc2)

# Add the grid
ax.grid(which='major', axis='both', linestyle='-')

# Add the image
ax.imshow(image,cmap="gray")

# Find number of gridsquares in x and y direction
nx=abs(int(float(ax.get_xlim()[1]-ax.get_xlim()[0])/float(xInterval)))
ny=abs(int(float(ax.get_ylim()[1]-ax.get_ylim()[0])/float(yInterval)))

# Add some labels to the gridsquares
for j in range(ny):
    y=yInterval/2+j*yInterval
    for i in range(nx):
        x=xInterval/2.+float(i)*xInterval
        ax.text(x,y,'{:d}'.format(i+j*nx),color='w',ha='center',va='center')

# Save the figure
fig.savefig('myImageGrid.tiff',dpi=my_dpi)