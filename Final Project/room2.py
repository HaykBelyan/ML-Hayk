import cv2
import numpy as np
import pickle
import face_recognition
import glob

face_cascade = cv2.CascadeClassifier(
    'haar_cascade_files/haarcascade_frontalface_default.xml')

if face_cascade.empty():
    raise IOError("Unable to load the face cascade classifier XML file")

cap = cv2.VideoCapture(0)

scaling_factor = 0.5

# Get the list of all pickle files in the "faces" directory
pickle_files = glob.glob('faces/*.pickle')

# Load face data from all pickle files
face_data = []
for file in pickle_files:
    with open(file, 'rb') as f:
        face_data.extend(pickle.load(f))

# Extract the face encodings, names, and access permissions from the loaded face data
known_face_encodings = []
known_face_names = []
known_face_access = []
for data in face_data:
    if "name" in data and "face_encoding" in data and "access" in data:
        known_face_encodings.append(data["face_encoding"])
        known_face_names.append(data["name"])
        known_face_access.append([access.lower() for access in data["access"]])

while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, None, fx=scaling_factor,
                       fy=scaling_factor, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_rects = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Convert the frame to RGB for face recognition
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    for (x, y, w, h) in face_rects:
        # Convert the face region of interest (ROI) to grayscale
        face_roi = gray[y:y+h, x:x+w]

        # Encode the face ROI as a feature vector
        face_encoding = face_recognition.face_encodings(
            rgb_frame, [(y, x+w, y+h, x)])[0]
	
        # Perform face recognition using the loaded face data
        matched_names = []
        distances = face_recognition.face_distance(
            known_face_encodings, face_encoding)
        min_distance = min(distances)
        if min_distance < 0.5:  # Adjust the distance threshold for face recognition
            matched_names.append(known_face_names[np.argmin(distances)])

        # Draw rectangle
        rectangle_color = (0, 255, 0) if matched_names and "room2" in [access.lower() for access in known_face_access[np.argmin(distances)]] else (
            0, 0, 255)  # Green if recognized and has access, red otherwise
        cv2.rectangle(frame, (x, y), (x+w, y+h), rectangle_color, 3)

        # Get the access text and its size
        if matched_names and "room2" in [access.lower() for access in known_face_access[np.argmin(distances)]]:
            access_text = f"{matched_names[0]} - Access Granted - Room 2"
            # Green if recognized and has access
            access_text_color = (0, 255, 0)
        else:
            access_text = "Unknown" if not matched_names else f"{matched_names[0]} - Access Denied - Room 2"
            access_text_color = (0, 0, 255)  # Red if unrecognized or no access
        (text_width, text_height), _ = cv2.getTextSize(
            access_text, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)

        # Calculate the position for the access text
        text_x = x + (w - text_width) // 2
        text_y = y - 10 if (y - 10) > text_height else y + h + 10

        # Draw access text on top of the rectangle
        cv2.putText(frame, access_text, (text_x, text_y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, access_text_color, 1)

    cv2.imshow("Room 2 Face Detector", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
