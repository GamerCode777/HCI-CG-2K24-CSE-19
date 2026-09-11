# Sample Execution:
# Sample Input
# Input Array: 1080 × 1920 × 3 uint8 matrix — Step Factor N = 8
# Sample Output
# --- DOWNSAMPLING ANALYSIS (N = 8) ---
# Original Shape     : (1080, 1920, 3) | Memory: 6,220,800 bytes
# Downsampled Shape   : (135, 240, 3) | Memory: 97,200 bytes
# Re-expanded Shape   : (1080, 1920, 3) | Visual: Blocky Pixelation
# Dimension Reduction: 87.50% reduction per axis
# Memory Savings      : 98.44% data reduction

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os

# 1. Load image into a NumPy array
img_path = "sample.jpg"

# Automatically create a sample image if it doesn't exist
if not os.path.exists(img_path):
    test_data = np.random.randint(0, 256, (1080, 1920, 3), dtype=np.uint8)
    Image.fromarray(test_data).save(img_path)
    print(f"Generated a synthetic image at '{img_path}' for testing.")
img = np.array(Image.open(img_path))

N = 8  # Step factor

# 2. Downsample using NumPy striding
downsampled = img[::N, ::N, :]

# 3. Re-expand back to original dimensions using np.repeat
re_expanded = np.repeat(downsampled, N, axis=0)
re_expanded = np.repeat(re_expanded, N, axis=1)

# Handle cases where original dims aren't perfectly divisible by N
re_expanded = re_expanded[: img.shape[0], : img.shape[1], :]

# 4. Calculate percentage drop in dimensions and memory
original_mem = img.nbytes
downsampled_mem = downsampled.nbytes

dim_reduction = (1 - (downsampled.shape[0] / img.shape[0])) * 100
mem_reduction = (1 - (downsampled_mem / original_mem)) * 100

# Console Output Summary
print(f"--- DOWNSAMPLING ANALYSIS (N = {N}) ---")
print(f"Original Shape      : {img.shape} | Memory: {original_mem:,} bytes")
print(f"Downsampled Shape   : {downsampled.shape} | Memory: {downsampled_mem:,} bytes")
print(f"Re-expanded Shape   : {re_expanded.shape} | Visual: Blocky Pixelation")
print(f"Dimension Reduction : {dim_reduction:.2f}% reduction per axis")
print(f"Memory Savings      : {mem_reduction:.2f}% data reduction")

# Display original vs pixelated comparison
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].imshow(img)
axes[0].set_title("Original Image")
axes[0].axis("off")

axes[1].imshow(re_expanded)
axes[1].set_title(f"Pixelated (N={N})")
axes[1].axis("off")

plt.tight_layout()
plt.show()