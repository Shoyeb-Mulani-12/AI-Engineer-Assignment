import cv2
import os
from glob import glob

input_folder = "task_2_input"
output_folder = "task_2_output"

os.makedirs(output_folder, exist_ok=True)

before_images = glob(os.path.join(input_folder, "*.jpg"))
before_images = [x for x in before_images if "~2" not in x]

for before_path in before_images:
    base = os.path.basename(before_path).replace(".jpg", "")
    after_path = os.path.join(input_folder, f"{base}~2.jpg")

    if not os.path.exists(after_path):
        print("Missing after image for:", base)
        continue

    before = cv2.imread(before_path)
    after = cv2.imread(after_path)

    gray_b = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
    gray_a = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(gray_b, gray_a)
    _, thresh = cv2.threshold(diff, 35, 255, cv2.THRESH_BINARY)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    annotated = after.copy()

    for c in contours:
        if cv2.contourArea(c) < 300:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(annotated, (x, y), (x + w, y + h), (0, 0, 255), 3)

    output_path = os.path.join(output_folder, f"{base}~3.jpg")
    cv2.imwrite(output_path, annotated)
    print("Generated:", output_path)
