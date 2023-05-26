import os
import shutil
import zipfile
from PIL import Image
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton, QFileDialog,QLabel, QLineEdit
from functions.uploadActions import unzip_hwt, rename_files
from functions.helperFunctions import delete_work_folders
from functions.xmlmanipluation import unzip_folder, delete_original_files, zip_folders, remove_zip_extension_from_zip_files
from functions.saveActions import delete_description_xml, rename_description_xml, zip_workfolder194

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Huawei to Honor WF 194 Converter")
        self.setGeometry(500, 500, 500, 500)
        self.text_edit = QTextEdit()
        self.button_upload = QPushButton("Upload 194 WF.hwt")
        self.button_upload.clicked.connect(self.upload_hwt)
        self.save_button = QPushButton("Save")
        self.save_button.setCheckable(True)
        self.save_button.clicked.connect(self.save)
        
        self.title_label = QLabel("Title:")
        self.title_edit = QLineEdit()
        self.designer_label = QLabel("Designer:")
        self.designer_edit = QLineEdit()
        self.version_label = QLabel("Version:")
        self.version_edit = QLineEdit()
        self.brief_info_label = QLabel("Brief Info:")
        self.brief_info_edit = QTextEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.button_upload)
        layout.addWidget(self.title_label)
        layout.addWidget(self.title_edit)
        layout.addWidget(self.designer_label)
        layout.addWidget(self.designer_edit)
        layout.addWidget(self.version_label)
        layout.addWidget(self.version_edit)
        layout.addWidget(self.brief_info_label)
        layout.addWidget(self.brief_info_edit)
        layout.addWidget(self.save_button)
        self.setLayout(layout)

     

        # Declare variables for save function
        self.work_folder = "workfolder"
        self.old_aod_name = "com.huawei.watchface"
        self.new_aod_name = "com.honor.watchface"
        self.xml_text = None
        self.icon_file_name = "icons"
        self.icons_folder = "icon_workfolder"
        self.archive_format = "zip"  
        self.aod_folder = "com.honor.watchface"
        self.assets_folder = "assets/"
        self.folders = ["com.honor.watchface"]
        self.files_to_delete = ["com.honor.watchface"]
        self.keys_mapping = {"HWTheme": "HNTheme"}



        
       # Clean up work folder at the start of each app launch
        for folder in self.folders:
            delete_work_folders(folder)
            assert os.path.exists(folder) == False, "Delete workfolder failed"

        # Clean up work folder at the start of each app launch
        delete_work_folders(self.work_folder)

             

    def upload_hwt(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select .hwt file", "", "HWT Files (*.hwt)")
        if file_path:

            # Call the unzip_hwt function from uploadActions.py
            unzip_hwt(file_path, self.work_folder)
            result_text = "Unzipped .hwt file successfully\n"
            
            # Call the rename_files function from uploadActions.py
            rename_files(self.work_folder, self.old_aod_name, self.new_aod_name)
            result_text += "Renamed launcher files successfully\n"
      
            
            ############################# Description.xml management and GUI ##########################################
            # Read the description.xml file
            description_file_path = os.path.join(self.work_folder, "description.xml")
            with open(description_file_path, "r", encoding='utf-8') as file:
                xml_text = file.read()

            result_text += f"Read '{description_file_path}'\n"

            assert os.path.exists(description_file_path) == True, "Description file not found"
            
            # Extract the desired fields from the original description
            import xml.etree.ElementTree as ET
            root = ET.fromstring(xml_text)
            title = root.find(".//title").text            
            brief_info = root.find(".//briefinfo").text
            
            # Copy the /assets/xml/aod_source_description.xml file into the workfolder
            shutil.copyfile(os.path.join(self.assets_folder, "xml/wf194_description.xml"), os.path.join(self.work_folder, "source_description.xml"))
            result_text += f"Copied 'source_description.xml' into '{self.work_folder}'\n"
            assert os.path.exists(os.path.join(self.work_folder, "source_description.xml")) == True, "Source description file not copied"
            
            # Read the source_description.xml file within the workfolder
            self.source_description_file_path = os.path.join(self.work_folder, "source_description.xml")
            with open(self.source_description_file_path, "r") as file:
                self.xml_text = file.read()
            result_text += f"Read '{self.source_description_file_path}'\n"
            assert os.path.exists(self.source_description_file_path) == True, "Source description file not found"
            
            # Extract and display the version and designer from the source_description.xml file
            root = ET.fromstring(self.xml_text)
            designer = root.find(".//designer").text
            version = root.find(".//version").text
                      
            # convert all characters to english
            title = title.encode('ascii', 'ignore').decode('ascii')
            designer = designer.encode('ascii', 'ignore').decode('ascii')
            version = version.encode('ascii', 'ignore').decode('ascii')
            brief_info = brief_info.encode('ascii', 'ignore').decode('ascii')

            result_text += f"Extracted fields from '{description_file_path}'\n"
            assert title != None, "Title not extracted"
            assert designer != None, "Designer not extracted"
            assert version != None, "Version not extracted"
            assert brief_info != None, "Brief Info not extracted"

            # Update the GUI fields with the extracted values
            self.title_edit.setText(title)
            self.designer_edit.setText(designer)
            self.version_edit.setText(version)
            self.brief_info_edit.setText(brief_info)
        
            assert self.title_edit.text() == title, "Title not updated"
            assert self.designer_edit.text() == designer, "Designer not updated"
            assert self.version_edit.text() == version, "Version not updated"
            assert self.brief_info_edit.toPlainText() == brief_info, "Brief Info not updated"
                    
            # diplay the result text in the GUI
            self.text_edit.setText(result_text)
            assert self.text_edit.toPlainText() == result_text, "Result text not displayed"

        




    def save(self):
        # Update the description.xml file with the new values
        import xml.etree.ElementTree as ET
        root = ET.fromstring(self.xml_text)
        root.find(".//title").text = self.title_edit.text()
        root.find(".//designer").text = self.designer_edit.text()
        root.find(".//version").text = self.version_edit.text()
        root.find(".//briefInfo").text = self.brief_info_edit.toPlainText()  # Use toPlainText() instead of text()

        assert root.find(".//title").text == self.title_edit.text(), "Title not updated"
        assert root.find(".//designer").text == self.designer_edit.text(), "Designer not updated"
        assert root.find(".//version").text == self.version_edit.text(), "Version not updated"
        assert root.find(".//briefInfo").text == self.brief_info_edit.toPlainText(), "Brief Info not updated"

        # Write the updated description.xml file
        with open(self.source_description_file_path, "w", encoding='utf-8') as file:
            file.write(ET.tostring(root, encoding="utf-8").decode('utf-8'))

        self.text_edit.setText("Saved")
        assert self.text_edit.toPlainText() == "Saved", "Saved text not displayed"

        # Delete the original description.xml file
        delete_description_xml(self.work_folder)

        # Rename the source_description.xml file to description.xml
        rename_description_xml(self.work_folder, self.source_description_file_path)

        # Unzip files within the workfolder #
        for folder in self.folders:
            unzip_folder(self.work_folder, folder, self.archive_format)
            result_text = f"Unzipped '{folder}' file successfully\n"
            

        # copy workfolder/description.xml to folder/watchface/watch_face_info.xml
        shutil.copyfile(os.path.join(self.work_folder, "description.xml"), os.path.join("com.honor.watchface/watchface/watch_face_info.xml"))

        # Delete the original files within the workfolder #
        delete_original_files(self.work_folder, self.folders)
        result_text += f"Deleted the original files within the workfolder successfully\n"

        # Zip the folders within the workfolder #
        zip_folders(self.folders, self.archive_format)
        result_text += f"Zipped the folders within the workfolder successfully\n"

        # Remove .zip extension from the zip files within the workfolder #
        for folder in self.folders:
            remove_zip_extension_from_zip_files(self.work_folder, folder, self.archive_format)
            result_text += f"Removed .zip extension from the '{folder}' file successfully\n"
        
        # Zip the workfolder into a .hwt file
        zip_workfolder194(self.work_folder, self.title_edit, self.designer_edit, self.version_edit, self.text_edit)
                
        # Clean up work folder at the start of each app launch
        for folder in self.folders:
            delete_work_folders(folder)
            assert os.path.exists(folder) == False, "Delete workfolder failed"

        # Clean up work folder at the start of each app launch
        delete_work_folders(self.work_folder)
    

if __name__ == "__main__":
    app = QApplication([])
    window = App()
    window.show()
    app.exec()
