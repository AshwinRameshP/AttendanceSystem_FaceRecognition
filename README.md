## Face Recognition based Attendance Monitoring System(FRAMS)  developed as part of internship at Tequed Labs
[![license](https://img.shields.io/github/license/DAVFoundation/captain-n3m0.svg?style=flat-square)](https://github.com/AshwinRameshP/AttendanceSystem_FaceRecognition/blob/master/LICENSE)

### Package Requirements
- Opencv -  `pip install opencv-python`
- Tkinter - Available in python package
- PIL  - `pip install Pillow`
- Pandas - `pip install pandas`

### How To Run the program
1. Download the project to local system.
2. Run the FRAMS.py file (Run from pycharm)
3. Enter student details and click "Take image" button.
   Wait for webcam to open and store your image.PS: make sure your faces are detected in the square boxes.
4. After all students are registered.Click "Train Model" to obtain a trained model in ".yml" format.Model must be retrained every time new students are registered.
5. Now Click on Automatic Attendance to automatically create a .csv file containing student attendance.
6. Attendance can be manually entered by admin also.
7. All attendance records for the class are stored in the Attendance folder.
8. Also we can visualize thw attendance in a bar graph statistics.

#### PS: Feel Free to Fork the Repository, improvise and reuse.

