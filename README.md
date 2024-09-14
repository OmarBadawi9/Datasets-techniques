# Datasets-techniques
how can we create and use the datasets to train AI models 

# Dataset Creation Tool for Object Detection Using Frame Subtraction

This project provides a tool for creating datasets by subtracting consecutive video frames to isolate and detect specific objects based on light changes. Originally designed for detecting LED lights in a black dark room, the tool can be adapted for other object detection scenarios.

In the original use case, the tool was used to detect the positions and colors of LED lights that emitted light one by one or simultaneously, against a black background. The subtraction technique highlights areas where changes occur, making it easier to isolate moving or light-emitting objects.

## Features

- **Frame Subtraction**: Subtracts consecutive video frames to detect changes in the scene.
- **LED Detection**: Can be used to detect the position and color of LED lights.
- **Background Customization**: Works best with videos where the background is relatively static or uniform (e.g., black backgrounds).
- **Flexible Dataset Generation**: You can use the tool to generate your own dataset for various object detection tasks.
- **Customizable Parameters**: Adjust frame extraction intervals, thresholds, and output settings to fit your specific use case.

## Requirements

- Python 3.x
- OpenCV
- NumPy
- PIL

Install the required dependencies by running:
```bash
pip install -r requirements.txt
