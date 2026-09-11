# Sample Execution:
# Sample Input
# Input File: ’sample.jpg’ (Dimensions: 1080 × 1920 × 3, RGB uint8)
# Sample Output
# --- CHANNEL EXTRACTION SUMMARY--
# Original Image Shape : (1080, 1920, 3)
# Red Channel 2D Shape : (1080, 1920) | Mean Intensity: 124.52
# Green Channel 2D Shape: (1080, 1920) | Mean Intensity: 142.18
# Blue Channel 2D Shape : (1080, 1920) | Mean Intensity: 98.34
# Display Window : Matplotlib 2x3 Subplot Grid Rendered.

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os

# 1. Load image into a NumPy array
img_path = "sample.jpg"

# Automatically create a sample image if it doesn't exist
if not os.path.exists(img_path):
    # Creates a 1080x1920x3 random RGB test image
    test_data = np.random.randint(0, 256, (1080, 1920, 3), dtype=np.uint8)
    Image.fromarray(test_data).save(img_path)
    print(f"Generated a synthetic image at '{img_path}' for testing.")
img = np.array(Image.open(img_path))

# 2. Extract individual 2D intensity grids via Axis 2 slicing
r_2d = img[:, :, 0]
g_2d = img[:, :, 1]
b_2d = img[:, :, 2]

# 3. Construct 3D isolated-channel color images
red_only = np.zeros_like(img)
red_only[:, :, 0] = r_2d

green_only = np.zeros_like(img)
green_only[:, :, 1] = g_2d

blue_only = np.zeros_like(img)
blue_only[:, :, 2] = b_2d

# 4. Console Output Summary
print("--- CHANNEL EXTRACTION SUMMARY ---")
print(f"Original Image Shape : {img.shape}")
print(
    f"Red Channel 2D Shape : {r_2d.shape} | Mean Intensity: {r_2d.mean():.2f}"
)
print(
    f"Green Channel 2D Shape: {g_2d.shape} | Mean Intensity: {g_2d.mean():.2f}"
)
print(
    f"Blue Channel 2D Shape : {b_2d.shape} | Mean Intensity: {b_2d.mean():.2f}"
)

# 5. Display 2x3 Subplot Grid using Matplotlib
fig, axes = plt.subplots(2, 3, figsize=(15, 8))

# Top Row: 3D Color Isolated Views
axes[0, 0].imshow(red_only)
axes[0, 0].set_title("Red-Only Channel (3D)")
axes[0, 0].axis("off")

axes[0, 1].imshow(green_only)
axes[0, 1].set_title("Green-Only Channel (3D)")
axes[0, 1].axis("off")

axes[0, 2].imshow(blue_only)
axes[0, 2].set_title("Blue-Only Channel (3D)")
axes[0, 2].axis("off")

# Bottom Row: 2D Intensity Grids (Grayscale)
axes[1, 0].imshow(r_2d, cmap="gray")
axes[1, 0].set_title("Red Intensity Grid (2D)")
axes[1, 0].axis("off")

axes[1, 1].imshow(g_2d, cmap="gray")
axes[1, 1].set_title("Green Intensity Grid (2D)")
axes[1, 1].axis("off")

axes[1, 2].imshow(b_2d, cmap="gray")
axes[1, 2].set_title("Blue Intensity Grid (2D)")
axes[1, 2].axis("off")

plt.tight_layout()
plt.show()
print("Display Window : Matplotlib 2x3 Subplot Grid Rendered.")