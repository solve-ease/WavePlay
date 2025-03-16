import cv2
import mediapipe as mp
import pyautogui
import time

def play_pause():
    pyautogui.press('space')  # Spacebar toggles play/pause

def like_video():
    pyautogui.hotkey('shift', '+')  # Simulate Shift++ to like the video

def forward_video():
    pyautogui.press('right')  # Forward 10 seconds

def rewind_video():
    pyautogui.press('left')  # Rewind 10 seconds

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Open the camera
cap = cv2.VideoCapture(0)

state = 0
t = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if time.time() - t > 10:
        state = 1
        # print("time over")

    # Convert the image to RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Convert back to BGR for rendering
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        print("hey")
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks
            # mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the coordinates of specific landmarks
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

            # Calculate distance between index finger tip and thumb tip
            distance = ((index_tip.x - thumb_tip.x) ** 2 + (index_tip.y - thumb_tip.y) ** 2) ** 0.5

            # Detect gestures based on distance
            # if distance < 0.1:
            #     print("Gesture: Thumbs Up")
            #     like_video()  # Like the video
            if distance > 0.1 and state:
                print("Gesture: Open Hand")
                play_pause()  # Play/Pause the video
                state = 0
                t = time.time()

    # # Display the image 
    # cv2.imshow('Hand Gesture Control', image)

    # # Break the loop if 'q' is pressed
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# Release resources
cap.release()
cv2.destroyAllWindows()