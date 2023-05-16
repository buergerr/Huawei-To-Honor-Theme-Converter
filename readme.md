# Project Name: Huawei to Honor Converter

## Description
This project is a Huawei to Honor converter that performs various operations on a .hwt file. It unzips the .hwt file into a work folder, renames specific files, resizes an image, unzips another file, renames icon filenames, zips the icon files, deletes the icon workspace, reformats a description.xml file, allows user editing in a GUI, saves the modified description.xml file, and finally, zips all the files in the work folder into a .hnt file.

## Instructions

### Step 1: Uploading the .hwt File
1. Click the "Upload .hwt" button.
2. Select the .hwt file you want to convert.

### Step 2: File Operations
The following operations will be performed on the uploaded .hwt file:

#### 2.1. Unzip the .hwt File
The .hwt file will be extracted into the work folder.

#### 2.2. File Renaming
- Rename the file "com.huawei.android.launcher" to "com.hihonor.android.launcher".
- Rename the file "com.huawei.phone.recorder" to "com.hihonor.phone.recorder".

#### 2.3. Image Resizing
- Resize the "icon_small.jpg" image from 510x340px to 510x345px.

#### 2.4. Unzip Icons File
- Unzip the icons file into the work folder.

#### 2.5. Icon File Renaming
- Rename all icon filenames by replacing "huawei" with "hihonor".

#### 2.6. Zip Icon Files
- Zip all the icon files into an "icon.zip" file.

#### 2.7. Delete Icon Workspace
- Delete the icon workspace folder.

#### 2.8. Reformat Description XML
- Reformat the "description.xml" file.

#### 2.9. Display in GUI and Edit Fields
- Display the reformatted "description.xml" file in a GUI.
- Edit the fields in the GUI as needed.

#### 2.10. Save Description XML
- Save the modified "description.xml" file.

#### 2.11. Zip Files
- Zip all the files in the work folder into a .hnt file.

### Step 3: Saving the Result
1. Click the "Save" button to save the modified files.
2. The work folder will be zipped into a .hnt file with the specified fields from the modified "description.xml" file.
3. The original .hwt file will remain unchanged.


## Dependencies

- Python 3.x: The programming language used for the project.
  - Installation: You can download Python from the official website: [Python.org](https://www.python.org/downloads/)

- PyQt5: A Python library for creating graphical user interfaces (GUI).
  - Installation: Open a terminal or command prompt and run the following command:
    ```shell
    pip install PyQt5
    ```

- Pillow: A Python library for image processing and manipulation.
  - Installation: Open a terminal or command prompt and run the following command:
    ```shell
    pip install pillow
    ```

## Running the Project

Once you have installed the dependencies, you can run the Huawei to Honor Converter project by executing the main Python script. Make sure to navigate to the project directory before running the script.

Open a terminal or command prompt, navigate to the project directory, and run the following command:

```shell
python converter.py

Please note that the instructions assume you have a working Python installation and have set up the PATH environment variable correctly.