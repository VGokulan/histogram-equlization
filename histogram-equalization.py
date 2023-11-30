#!/usr/bin/env python
# coding: utf-8

# In[2]:


import PIL
from PIL import Image
import numpy as np
import itertools
import matplotlib.pyplot as plt

# Open image
image_path = r"ADD IMAGE PATH"
image = Image.open(image_path)
image = image.convert("L")  # Convert to single-channeled image

# Convert image to numpy array
a = np.array(image)

# Plot the original image and its histogram
plt.figure(figsize=(15, 10))  # Increase the figure size for better visualization

# Original Image
plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

# Original Histogram
plt.subplot(2, 2, 2)
plt.hist(a.ravel(), bins=256)
plt.title('Original Histogram')
plt.ylabel('Frequency')
plt.xlabel('Gray Level')

# Histogram Equalization
width, height = image.size
totalPixels = width * height
freq = image.histogram()
cProbability = [0] * 256
prevSum = 0

for i in range(256):
    prevSum += freq[i] * 1.0 / totalPixels
    cProbability[i] = prevSum

pixels = image.load()
for x, y in itertools.product(range(width), range(height)):
    pixels[x, y] = int((255 * cProbability[pixels[x, y]]))

# Processed Image
plt.subplot(2, 2, 3)
plt.imshow(image, cmap='gray')
plt.title('Processed Image')

# Processed Histogram
plt.subplot(2, 2, 4)
plt.hist(np.array(image).ravel(), bins=256)
plt.title('Processed Histogram')
plt.ylabel('Frequency')
plt.xlabel('Gray Level')

# Display the plot
plt.tight_layout()
plt.show()

