import cv2
import numpy as np
import os
from glob import glob

input_folder = "task_1_input"
output_folder = "task_1_output"

os.makedirs(output_folder, exist_ok=True)

def overlay_thermal(rgb_path, thermal_path, output_path):
    rgb = cv2.imread(rgb_path)
    thermal = cv2.imread(thermal_path)

    # Convert to grayscale
    gray_rgb = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
    gray_th = cv2.cvtColor(thermal, cv2.COLOR_BGR2GRAY)

    # ORB feature extraction
    orb = cv2.ORB_create(5000)
    kp1, des1 = orb.detectAndCompute(gray_rgb, None)
    kp2, des2 = orb.detectAndCompute(gray_th, None)

    # Matcher
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = matcher.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)[:100]

    pts1 = []
    pts2 = []
    for m in matches:
        pts1.append(kp1[m.queryIdx].pt)
        pts2.append(kp2[m.trainIdx].pt)

    pts1 = np.float32(pts1)
    pts2 = np.float32(pts2)

    # Homography
    H, _ = cv2.findHomography(pts2, pts1, cv2.RANSAC)

    warped_thermal = cv2.warpPerspective(thermal, H, (rgb.shape[1], rgb.shape[0]))

    # Overlay (60% RGB + 40% Thermal)
    overlay = cv2.addWeighted(rgb, 0.6, warped_thermal, 0.4, 0)

    cv2.imwrite(output_path, overlay)


# ---- PROCESS ALL IMAGE PAIRS ----
thermal_images = glob(os.path.join(input_folder, "*_T.JPG"))

for thermal_img in thermal_images:
    base = os.path.basename(thermal_img).replace("_T.JPG", "")
    rgb_img = os.path.join(input_folder, f"{base}_Z.JPG")

    if not os.path.exists(rgb_img):
        print("Missing RGB for:", base)
        continue

    output_name = os.path.join(output_folder, base + "_AT.JPG")
    overlay_thermal(rgb_img, thermal_img, output_name)
    print("Generated:", output_name)
