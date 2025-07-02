import cv2
import numpy as np
import os

# Ask user for image path
path = input("Enter the full path of the image: ")

# Check if the file exists
if not os.path.exists(path):
    print("❌ File not found. Please check the path and try again.")
else:
    # Read image
    img = cv2.imread(path)

    if img is None:
        print("❌ Could not read the image. Check file format or path.")
    else:
        # Resize for display (optional: remove if you want original size)
        img = cv2.resize(img, (500, 500))  # Resize to 500x500

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Convert grayscale to BGR for stacking
        gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

        # Combine side-by-side
        combined = np.hstack((img, gray_bgr))

        # Show result
        cv2.imshow("Original and Grayscale", combined)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
