import cv2
import dlib
import numpy as np

# Load the image
image_path = 'path_to_your_image.jpg'
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load pre-trained face detector and shape predictor from dlib
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# Detect faces in the image
faces = detector(gray)

for face in faces:
    # Get the landmarks
    landmarks = predictor(gray, face)

    # Convert landmarks to a numpy array
    landmarks_points = []
    for n in range(0, 68):
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        landmarks_points.append((x, y))

    # Analyze facial shape (simple example)
    jawline_points = landmarks_points[0:17]
    chin_width = np.linalg.norm(np.array(jawline_points[0]) - np.array(jawline_points[-1]))
    face_height = np.linalg.norm(np.array(jawline_points[8]) - np.array(jawline_points[19]))

    if chin_width / face_height < 0.6:
        face_shape = "Oval"
    else:
        face_shape = "Round"

    print(f'Detected face shape: {face_shape}')

    # Draw landmarks on the image
    for point in landmarks_points:
        cv2.circle(image, point, 2, (0, 255, 0), -1)

# Save or display the output image
output_path = 'output_image.jpg'
cv2.imwrite(output_path, image)
cv2.imshow("Output", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
