# Driver Drowsiness Detector
### Video Demo:  https://www.youtube.com/channel/UClCgj3PHsNcHNcBi4gR9sDg

### Description:
The Driver Drowsiness Detector is an application designed to enhance road safety by detecting driver drowsiness in real-time. This project utilizes a combination of computer vision techniques and machine learning models to analyze video streams and identify signs of driver fatigue. Upon detection of drowsiness, an alert is triggered to wake the driver, thus preventing potential accidents.

### Project Structure:
* main.py: The main script that runs the application. It sets up the user interface, initializes the video capture, and handles the detection logic.
* police-siren.mp3: The audio file that plays an alert sound when drowsiness is detected.
* requirements.txt: A list of required Python packages to run the project.
* README.md: The documentation file you are currently reading.

### Installation and Setup:
1. **Clone the repository**:

```git clone https://github.com/MisfarJalal/Driver_Drowsiness_Detectorv01-04```


2. **Install the required packages**:

```pip install -r requirements.txt```

#### Download the YOLO model:
Place the YOLO model weights file (best.pt) in the runs/detect/train/weights/ directory.

Run the application:

```python main.py```

#### Detailed Description:
The application leverages the YOLO model trained to detect drowsiness in drivers. The user interface is built using Tkinter and CustomTkinter to provide a dark mode theme and better UI elements.

### Key Components:

**User Interface**:
* The main window is created using Tkinter and CustomTkinter with a dark appearance mode.
* A video frame is set up to display the real-time video stream from the webcam.
* A counter and reset button are included to keep track of drowsiness detections and reset the counter when necessary.
**Detection Logic**:
* The YOLO model is loaded to perform real-time detection on the video stream.
* The video is captured using OpenCV, and frames are processed to detect drowsiness.
* If the model detects drowsiness with a confidence greater than 60%, the counter is incremented.
* The police siren sound is played as an alert if the counter reaches a certain threshold.
**Audio Alert**:
* Pygame is used to initialize the mixer and play the alert sound (police-siren.mp3) when drowsiness is detected.
**Design Choices**:
* Tkinter and CustomTkinter: Chosen for their simplicity and ability to create a modern-looking UI with minimal effort.
* YOLO Model: Provides fast and accurate object detection suitable for real-time applications.
* Pygame: Utilized for it's easy-to-use audio playback capabilities.
**Future Improvements**:
* Enhancing Detection Accuracy: Further training the model with more diverse datasets to improve detection accuracy.
* Adding More Alerts: Implementing different types of alerts (e.g., visual warnings) in addition to audio alerts.
* User Customization: Allowing users to customize alert settings and detection sensitivity.
##### Conclusion:
The Driver Drowsiness Detector project showcases the integration of computer vision and machine learning to address a critical safety issue. By providing real-time detection and alerts, this application aims to reduce the risk of accidents caused by driver fatigue.

Feel free to contribute to the project by opening issues and submitting pull requests on the GitHub repository. Your feedback and suggestions are highly appreciated!