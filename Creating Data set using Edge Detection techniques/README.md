# Dataset Creation Tool Using Edge Detection for Object Segmentation

This project provides a tool that helps users create datasets by using edge detection techniques to split or separate objects from a single image. The tool detects edges in an image, isolates individual objects, and prepares them for further analysis or dataset generation.

## Features

- **Edge Detection**: Applies edge detection algorithms to identify and highlight the boundaries of objects in an image.
- **Object Segmentation**: Automatically segments objects based on the detected edges, splitting them from the rest of the image.
- **Customizable Parameters**: Users can adjust edge detection sensitivity and other parameters to fine-tune the results.
- **Dataset Generation**: Outputs the segmented objects in a format suitable for creating datasets for machine learning and computer vision tasks.

## Requirements

- Python 3.x
- NumPy
- glob
- PIL

You can install the necessary dependencies by running:
```bash
pip install -r requirements.txt
