### **Hand Gesture-Controlled YouTube Player**

This application allows you to control YouTube videos using hand gestures. By leveraging **MediaPipe** for hand gesture detection and **Selenium** for browser automation, the program maps specific hand gestures to YouTube actions such as play/pause, like/dislike, and seeking forward/backward. Simply perform gestures in front of your webcam, and the application will translate them into commands to control YouTube in real-time.

#### **Features**
- **Play/Pause**: Open hand gesture to toggle play/pause.
- **Like/Dislike**: Thumbs up to like, thumbs down to dislike.
- **Seek Forward/Backward**: Gestures to skip or rewind the video.
- **Real-Time Gesture Detection**: Uses your webcam to detect and respond to gestures instantly.

#### **Technologies Used**
- **MediaPipe**: For hand gesture detection and tracking.
- **Selenium**: For automating YouTube in the browser.
- **OpenCV**: For webcam input and video processing.

#### **How It Works**
1. The application detects hand gestures using your webcam.
2. It maps these gestures to specific YouTube actions (e.g., play, pause, like, seek).
3. Selenium interacts with the YouTube website to perform the corresponding actions.

#### **Use Cases**
- Hands-free YouTube control for accessibility.
- Fun and interactive way to control media playback.
- Learning tool for gesture recognition and browser automation.

#### **How to Run**
1. Clone the repository:
   ```bash
   git clone 
   cd <repository-folder>
   ```
2. Install dependencies using `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
3. Download the appropriate WebDriver (e.g., ChromeDriver) and ensure it's in your PATH.
4. Run the script:
   ```bash
   python3 main.py
   ```
5. Perform gestures in front of your webcam to control YouTube.

---

Feel free to contribute, report issues, or suggest improvements! 🚀