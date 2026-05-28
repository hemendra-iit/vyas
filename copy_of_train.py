# -*- coding: utf-8 -*-
"""Copy of train.ipynb

Original file is located at
    https://colab.research.google.com/drive/1FngjqMjmfAeVSs_rVsJuikWdJzSWjUN4
"""

!pip install OpenCV-Python

#import the libraries below
import cv2
import numpy as np
import matplotlib.pyplot as plt

# STEP 1: Upload image

from google.colab import files

uploaded = files.upload()

# STEP 2: Check uploaded filename

import os

print(os.listdir())

# STEP 3: Read and display image

import cv2
from google.colab.patches import cv2_imshow

# Replace with your exact filename from STEP 2
img = cv2.imread('Screenshot 2026-04-08 095453.png')

# Check image loaded or not
if img is None:
    print("Image not found. Check filename.")
else:
    print("Image loaded successfully")
    cv2_imshow(img)

#use grey image for identifying the face
import cv2
import matplotlib.pyplot as plt

# Read your image
img = cv2.imread('Screenshot 2026-04-08 095453.png')

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Show grayscale image
plt.figure(figsize=(8,8))
plt.imshow(gray, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')
plt.show()

#
import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread('Screenshot 2026-04-08 095453.png')  # use the actual attached filename

if img is None:
    raise FileNotFoundError("Image not found. Check the file path and filename.")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

if face_cascade.empty():
    raise RuntimeError("Failed to load Haar cascade classifier.")

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Draw rectangles directly on all detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Show result
plt.figure(figsize=(8, 8))
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Detected Faces")
plt.axis("off")
plt.show()

import cv2
import os

input_folder = "training_img"
output_folder = "training_img_grayscale"
os.makedirs(output_folder, exist_ok=True)

print("Current working directory:", os.getcwd())

if not os.path.exists(input_folder):
    raise FileNotFoundError(f"Folder not found: {input_folder}")

print("Files in folder:", os.listdir(input_folder))

training_images = []
training_labels = []

for file in os.listdir(input_folder):
    if file.lower().endswith((".jpg", ".jpeg", ".png")):
        img_path = os.path.join(input_folder, file)
        print("Reading:", img_path)

        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            print(f"Warning: could not read {img_path}")
            continue

        training_images.append(img)
        training_labels.append(file)

        save_path = os.path.join(output_folder, f"gray_{file}")
        cv2.imwrite(save_path, img)

print("Loaded images:", len(training_images))
print("Labels:", training_labels)

#check for the 1st array training image shape
training_images[0].shape

#check whether labels are properly appended.
training_labels

import cv2
import numpy as np
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()

numeric_labels = []
valid_images = []

for img, label in zip(training_images, training_labels):
    if isinstance(label, str):
        label_num = os.path.splitext(label)[0]   # "1.jpg" -> "1"
        label_num = int(label_num)              # "1" -> 1
    else:
        label_num = int(label)

    valid_images.append(img)
    numeric_labels.append(label_num)

recognizer.train(valid_images, np.array(numeric_labels, dtype=np.int32))
recognizer.save("trainer.yml")

print("Training completed and model saved.")

import cv2
import numpy as np

test_path = "training_img/1.jpg"   # use the real path if the file is inside the folder
test_img = cv2.imread(test_path, cv2.IMREAD_GRAYSCALE)

if test_img is None:
    raise FileNotFoundError(f"Could not read test image: {test_path}")

label, confidence = recognizer.predict(test_img)
print(f"Label: {label}, Confidence: {confidence}")

"""## Accessing Camera"""

from IPython.display import display, Javascript
from google.colab.output import eval_js
from base64 import b64decode
import cv2
import numpy as np

def take_photo(filename='photo.jpg', quality=0.8):
    js = Javascript('''
        async function takePhoto(quality) {
            const div = document.createElement('div');
            const capture = document.createElement('button');
            capture.textContent = 'Capture';
            div.appendChild(capture);

            const video = document.createElement('video');
            video.style.display = 'block';
            const stream = await navigator.mediaDevices.getUserMedia({video: true});

            document.body.appendChild(div);
            div.appendChild(video);
            video.srcObject = stream;
            await video.play();

            // Resize the output to fit the video element.
            google.colab.output.setIframeHeight(document.documentElement.scrollHeight, true);

            await new Promise((resolve) => capture.onclick = resolve);

            const canvas = document.createElement('canvas');
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            canvas.getContext('2d').drawImage(video, 0, 0);
            stream.getVideoTracks()[0].stop();
            div.remove();
            return canvas.toDataURL('image/jpeg', quality);
        }
    ''')
    display(js)
    data = eval_js('takePhoto({})'.format(quality))
    binary = b64decode(data.split(',')[1])
    with open(filename, 'wb') as f:
        f.write(binary)
    return filename

try:
    filename = take_photo('captured_face.jpg') # This will prompt you to allow camera access
    print(f'Saved to {filename}')

    # You can now read and process this image with OpenCV
    # img = cv2.imread(filename)
    # if img is not None:
    #     from google.colab.patches import cv2_imshow
    #     cv2_imshow(img)

except Exception as err:
    print(str(err))

#just rename the captured image to a labeled format such that it do not have any random name. use below name to identify seperately from the known images
import os
os.rename('captured_face.jpg', 'person_2.jpg')
print("Photo renamed to 'person_2.jpg'")

import cv2
import numpy as np
import os

# from here, same steps as performd earlier.
new_img = cv2.imread('person_2.jpg', cv2.IMREAD_GRAYSCALE)

#append to training data used earlier but using new label. because this image will need new label, not any label used earlier. here we are labeling it 7
training_images.append(new_img)
training_labels.append(7)  # Assign the same label as before

# Recreate numeric labels to ensure all are integers
# This loop iterates through the training_labels list. If a label is a string (like '1.jpg'),
# it extracts the base filename (e.g., '1') and converts it to an integer. If it's already
# an integer, it uses it directly. This ensures all labels are in the correct numerical format.
updated_numeric_labels = []
for label in training_labels:
    if isinstance(label, str):
        label_num = int(os.path.splitext(label)[0])
    else:
        label_num = int(label)
    updated_numeric_labels.append(label_num)

#now again train the recognizer with the updated data
recognizer.train(training_images, np.array(updated_numeric_labels, dtype=np.int32))
print("Model retrained with the newly captured image")

#now access the default camera again
cap = cv2.VideoCapture(0)

while True:
    #capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    #amd convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #now predict using the trained model (recognizer, used above to train)
    label, confidence = recognizer.predict(gray_frame)

    #display proper label and confidence on the frame
    cv2.putText(frame, f'Label: {label}, Confidence: {confidence}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    #now show the live camera feed until you press 'q'
    cv2.imshow('Face Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

"""Now, let's use the `captured_face.jpg` (or `person_1.jpg` after renaming) to test our trained recognizer. We'll load the image, convert it to grayscale, detect faces, and then predict the label and confidence."""

import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# Path to the captured image (or renamed image)
# Use 'person_1.jpg' if you ran the rename cell, otherwise 'captured_face.jpg'
image_to_recognize_path = 'person_2.jpg'

# Load the image and convert to grayscale
test_face_img = cv2.imread(image_to_recognize_path, cv2.IMREAD_GRAYSCALE)

if test_face_img is None:
    raise FileNotFoundError(f"Could not read image: {image_to_recognize_path}")

# Load face detector (same as before)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

if face_cascade.empty():
    raise RuntimeError("Failed to load Haar cascade classifier.")

# Detect faces in the captured image
faces_detected = face_cascade.detectMultiScale(
    test_face_img,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

if len(faces_detected) == 0:
    print("No faces detected in the captured image.")
else:
    for (x, y, w, h) in faces_detected:
        # Extract the detected face region
        face_roi = test_face_img[y:y+h, x:x+w]

        # Predict the label and confidence using the trained recognizer
        predicted_label, confidence = recognizer.predict(face_roi)

        # Draw rectangle and put text on the original (color) image for display
        # If you only have the grayscale image, convert it back to color for text drawing
        display_img = cv2.cvtColor(test_face_img, cv2.COLOR_GRAY2BGR)
        cv2.rectangle(display_img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(display_img, f'Label: {predicted_label}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        cv2.putText(display_img, f'Conf: {int(confidence)}', (x, y+h+25), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the result
    cv2_imshow(display_img)
    print(f"Predicted Label: {predicted_label}, Confidence: {confidence}")
