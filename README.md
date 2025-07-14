# Face-Recognition

## Overview

Face-Recognition is a Python-based project for automated face recognition and attendance marking. It leverages OpenCV and the `face_recognition` library to detect and identify faces from images and webcam streams. The project demonstrates both basic face comparison and a practical attendance system using facial identification.

## Features

- **Face Comparison**: Compare faces from the images in the Images folder and display confidence scores.
- **Live Face Recognition**: Use your webcam to recognize faces in real time.
- **Attendance Marking**: Automatically record recognized faces with timestamps in a CSV file.
- **Easy Person Enrollment**: Add new people by simply placing their images in the `ImagesAttendance` folder.

## Directory Structure

```
.
├── venv/
│   ├── Basics.py            # Basic image face comparison demo
│   ├── Attendance.py        # Main attendance system using live webcam and face recognition
│   ├── Attendance.csv       # Attendance log output
├── ImagesBasic/             # Images for basic face comparison example
│   ├── Elon Musk.jpg
│   ├── Elon Test.jpg
├── ImagesAttendance/        # Images of people to recognize for attendance
│   └── [Person1].jpg
│   └── [Person2].jpg
└── README.md
```

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/IliasCoder/Face-Recognition.git
   cd Face-Recognition
   ```

2. **Set Up a Virtual Environment (Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Linux/Mac
   venv\Scripts\activate         # On Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install opencv-python face_recognition numpy
   ```

## Usage

### Basic Face Comparison

- Place two images in the `ImagesBasic` folder:
  - Reference image (e.g., `Elon Musk.jpg`)
  - Test image (e.g., `Elon Test.jpg`)
- Run the demo:
  ```bash
  python venv/Basics.py
  ```
- The script will show both images, draw rectangles around detected faces, and print the similarity score.

### Attendance System

- Add images (JPG/PNG) of people to recognize into the `ImagesAttendance` folder. Use clear, front-facing photos.
- Run the attendance system:
  ```bash
  python venv/Attendance.py
  ```
- The webcam will launch, and whenever a known face is detected, their name and timestamp are logged in `Attendance.csv`.
- To enroll a new person, simply add their image to `ImagesAttendance` and restart the script.

## Contribution Guide

1. **Fork the repository** and create your feature branch (`git checkout -b feature/AmazingFeature`).
2. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`).
3. **Push to the branch** (`git push origin feature/AmazingFeature`).
4. **Open a pull request**.

For bug reports or feature requests, please use the Issues tab.

## Notes

- This project does not currently include a requirements.txt file.
- Images for recognition should be clear and high-resolution for best results.
- Attendance data is stored in a simple CSV file and not protected from manual editing.
- The project is for educational/demo purposes and may require adaptation for production use.

## License

MIT LICENSE

## Acknowledgements

- [OpenCV](https://opencv.org/)
- [face_recognition](https://github.com/ageitgey/face_recognition)
