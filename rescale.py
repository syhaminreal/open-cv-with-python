import cv2 as cv  # Import the OpenCV library

def rescaleFrame(frame, scale=0.75):
    # Calculate the new width and height based on the scaling factor
    #for the local videos or saved videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    # Resize the frame using the calculated dimensions
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width,height):
    #live video or real time video
    capture.set(3,width)
    capture.set(4,height)



# Load the image from the specified path
img_path = 'photo/mali.jpg'  # Adjust this path as needed
img = cv.imread(img_path)

# Check if the image was loaded correctly
if img is None:
    print(f"Error: Could not load image from {img_path}")
else:
    # Display the original image
    cv.imshow('Original Image', img)

    # Rescale the image
    resized_image = rescaleFrame(img)

    # Display the rescaled image
    cv.imshow('Rescaled Image', resized_image)

    # Wait until a key is pressed to close the image windows
    cv.waitKey(0)
    cv.destroyAllWindows()

# Open the video file for reading
video_path = 'video/x.mp4'  # Adjust this path as needed
capture = cv.VideoCapture(video_path)

# Check if the video file was opened successfully
if not capture.isOpened():
    print(f"Error: Could not open video file from {video_path}")
else:
    # Loop to read and display frames from the video
    while True:
        # Read a frame from the video
        isTrue, frame = capture.read()
        # Break the loop if the frame was not read successfully (end of video)
        if not isTrue:
            break

        # Rescale the frame to 20% of its original size
        frame_resized = rescaleFrame(frame, scale=0.2)

        # Display the original frame
        cv.imshow('Video', frame)
        # Display the rescaled frame
        cv.imshow('Rescaled Video', frame_resized)
        
        # Wait for 20 milliseconds and check if 'd' key is pressed to break the loop
        if cv.waitKey(20) & 0xFF == ord('d'):
            break

    # Release the video capture object and close all OpenCV windows
    capture.release()
    cv.destroyAllWindows()
