# Sample Execution:
# Sample Input
# Program initialization (No file input required — synthetic matrix generation).
# Sample Output
# --- SYNTHETIC MATRIX METRICS--
# Array Shape (H, W, C) : (300, 400, 3)
# Data Type : uint8
# Total Elements : 360,000 values
# Memory Footprint : 360,000 bytes (351.56 KB)

import numpy as np

def create_synthetic_image():
    # 1. Create 300x400x3 matrix initialized with zeros
    height, width, channels = 300, 400, 3
    img = np.zeros((height, width, channels), dtype=np.uint8)

    half_h = height // 2
    half_w = width // 2

    # 2. Fill four quadrants using spatial slicing
    # Top-Left: Red [255, 0, 0]
    img[0:half_h, 0:half_w] = [255, 0, 0]

    # Top-Right: Green [0, 255, 0]
    img[0:half_h, half_w:width] = [0, 255, 0]

    # Bottom-Left: Blue [0, 0, 255]
    img[half_h:height, 0:half_w] = [0, 0, 255]

    # Bottom-Right: White [255, 255, 255]
    img[half_h:height, half_w:width] = [255, 255, 255]

    # 3. Print matrix parameters
    print("--- SYNTHETIC MATRIX METRICS ---")
    print(f"Array Shape (H, W, C) : {img.shape}")
    print(f"Data Type             : {img.dtype}")
    print(f"Total Elements        : {img.size:,} values")
    print(
        f"Memory Footprint      : {img.nbytes:,} bytes ({img.nbytes / 1024:.2f} KB)"
    )


if __name__ == "__main__":
    create_synthetic_image()