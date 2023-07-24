# Huawei to Honor Converter - README

## Introduction
This README provides an overview of the Huawei to Honor Converter application, its functionalities, and usage instructions. The application allows users to convert Huawei themes to Honor themes effortlessly.

## Getting Started
Follow the steps below to set up and use the Huawei to Honor Converter application:

### Prerequisites
Make sure you have the following software installed on your system:
- Python 3.x
- PyQt5
- PIL (Python Imaging Library)

### Installation
1. Clone or download this repository to your local machine.
2. Install the required Python packages using the following command:
   ```bash
   pip install PyQt5 Pillow

## Usage
Launch the application by running the following command:
   ```bash
   python converter.py
   ```

The application window will open, showing various input fields and buttons.

## Buttons and Functions
### Upload .hwt:
Click this button to upload the Huawei theme (.hwt) file you want to convert. The application will process the file and display the progress in the text area.
### Save:
After uploading the .hwt file and making any necessary changes, click this button to save the converted Honor theme (.hwt) file. The application will prompt you to provide the required details, such as title, designer, version, and brief info, before saving.


## Features
- Unzips the uploaded .hwt file and performs necessary modifications.
- Resizes the icon_small.jpg within the preview folder to 510x345px.
- Renames launcher and recorder files to match the Honor package names.
- Unzips and renames icon files within the icon_workfolder.
- Validates and cleans up XML files within the workfolder.
- Converts characters in fields to English within description.xml.
- Manages source_description.xml and updates GUI fields with extracted values.
- Generates previews for the converted theme.
- Renames files within the workfolder and zips the folders.
- Removes .zip extension from zip files and cleans up the workspace.

## Acknowledgements
Special thanks to the developers and contributors of PyQt5 and Pillow libraries for enabling the creation of this application.

## License
This project is licensed under the MIT License.

