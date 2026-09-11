# Sample Input
# Enter horizontal resolution (pixels): 1920
# Enter vertical resolution (pixels): 1080
# Enter physical diagonal size (inches): 24
# Sample Output
# --- DISPLAY METRICS ANALYSIS ---
# Total Pixel Count : 2,073,600 pixels
# Aspect Ratio : 16:9
# Calculated DPI : 91.79 DPI
# Density Category : Low Density (Standard Monitor)

import math

def calculate_screen_metrics():
    # Prompt user for inputs
    w_px = int(input("Enter horizontal resolution (pixels): "))
    h_px = int(input("Enter vertical resolution (pixels): "))
    d_inches = float(input("Enter physical diagonal size (inches): "))

    # 1. Total pixel count
    total_pixels = w_px * h_px

    # 2. Simplified aspect ratio using GCD
    gcd = math.gcd(w_px, h_px)
    aspect_w = w_px // gcd
    aspect_h = h_px // gcd

    # 3. Screen DPI (PPI) calculation
    # Formula: sqrt(W_px^2 + H_px^2) / Diagonal_inches
    dpi = math.sqrt(w_px**2 + h_px**2) / d_inches

    # 4. Classify display density
    if dpi < 100:
        category = "Low Density (Standard Monitor)"
    elif 100 <= dpi <= 200:
        category = "Medium Density (HD Display)"
    else:
        category = "High Density (Retina / Mobile)"

    # Output formatted results
    print("\n--- DISPLAY METRICS ANALYSIS ---")
    print(f"Total Pixel Count : {total_pixels:,} pixels")
    print(f"Aspect Ratio      : {aspect_w}:{aspect_h}")
    print(f"Calculated DPI    : {dpi:.2f} DPI")
    print(f"Density Category  : {category}")

if __name__ == "__main__":
    calculate_screen_metrics()