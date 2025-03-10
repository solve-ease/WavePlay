import cv2
import mediapipe as mp
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def play_pause():
    video = driver.find_element(By.TAG_NAME, "video")
    video.send_keys(Keys.SPACE)  # Spacebar toggles play/pause

def like_video():
    like_button = driver.find_element(By.XPATH, '//button[@aria-label="Like this video"]')
    like_button.click()

def forward_video():
    video = driver.find_element(By.TAG_NAME, "video")
    video.send_keys(Keys.ARROW_RIGHT)  # Forward 10 seconds

def rewind_video():
    video = driver.find_element(By.TAG_NAME, "video")
    video.send_keys(Keys.ARROW_LEFT)  # Rewind 10 seconds

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Initialize Selenium
driver = webdriver.Chrome()  # Use the appropriate WebDriver
driver.get("https://www.youtube.com")
time.sleep(5)  # Wait for the page to load

# Open the camera
cap = cv2.VideoCapture(0)

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
            distance = ((index_tip.x - thumb_tip.x) ** 2 + (index_tip.y - thumb_tip.y) ** 2) ** 0.5

            # Detect gestures based on distance
            if distance < 0.05:
                print("Gesture: Thumbs Up")
                like_video()  # Like the video
            elif distance > 0.1:
                print("Gesture: Open Hand")
                play_pause()  # Play/Pause the video

# Release resources
cap.release()
cv2.destroyAllWindows()
driver.quit()  # Close the browser