import cv2
import mediapipe as mp
import pyautogui
import math
import os

# Create a directory to save cropped hand images
if not os.path.exists("hand_images"):
    os.makedirs("hand_images")

# Function to play/pause the video
def play_pause():
    pyautogui.press('space')  # Spacebar toggles play/pause

# Function to like the video
def like_video():
    pyautogui.hotkey('shift', '+')  # Simulate Shift++ to like the video

# Function to forward the video by 10 seconds
def forward_video():
    pyautogui.press('right')  # Forward 10 seconds

# Function to rewind the video by 10 seconds
def rewind_video():
    pyautogui.press('left')  # Rewind 10 seconds

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Open the camera
cap = cv2.VideoCapture(0)

# Counter to save unique images
image_counter = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the image to RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Convert back to BGR for rendering
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the coordinates of specific landmarks
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

            # Calculate distance between index finger tip and thumb tip
            distance = math.sqrt((index_tip.x - thumb_tip.x) ** 2 + (index_tip.y - thumb_tip.y) ** 2)

            # Print the distance for debugging
            # print(f"Distance: {distance}")

            # Visualize the distance on the frame
            # cv2.putText(image, f"Distance: {distance:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            if distance > 0.1:  # Adjust this threshold as needed
                print("Gesture: Open Hand")
                play_pause()  # Play/Pause the video

            # Extract the bounding box of the hand
            x_coords = [landmark.x for landmark in hand_landmarks.landmark]
            y_coords = [landmark.y for landmark in hand_landmarks.landmark]
            min_x, max_x = int(min(x_coords) * frame.shape[1]), int(max(x_coords) * frame.shape[1])
            min_y, max_y = int(min(y_coords) * frame.shape[0]), int(max(y_coords) * frame.shape[0])

            # Add padding to the bounding box
            padding = 20
            min_x = max(0, min_x - padding)
            max_x = min(frame.shape[1], max_x + padding)
            min_y = max(0, min_y - padding)
            max_y = min(frame.shape[0], max_y + padding)

            # Crop the hand region
            hand_crop = frame[min_y:max_y, min_x:max_x]

            # Save the cropped hand image
            if hand_crop.size != 0:  # Ensure the cropped image is not empty
                image_counter += 1
                cv2.imwrite(f"hand_images/hand_{image_counter}.jpg", hand_crop)
                print(f"Saved hand image: hand_images/hand_{image_counter}.jpg")

    # Display the image
    cv2.imshow('Hand Gesture Control', image)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()