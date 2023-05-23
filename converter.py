import os
import shutil
import zipfile
from PIL import Image
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton, QFileDialog,QLabel, QLineEdit
from functions.uploadActions import unzip_hwt, rename_files, unzip_icons, rename_icons, zip_icons, delete_icons_file, remove_icons_zip_extension, delete_icons_workspace
from functions.imageManipulation import resize_icon_small_preview
from functions.xmlmanipluation import delete_and_copy_theme_xml, unzip_folder, replace_keys_in_xml_folders
from functions.helperFunctions import delete_work_folders
from functions.saveActions import delete_description_xml, rename_description_xml, zip_workfolder

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Huawei to Honor Converter")
        self.setGeometry(500, 500, 500, 500)
        self.text_edit = QTextEdit()
        self.button_upload = QPushButton("Upload .hwt")
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
        self.source_description_file_path = os.path.join(self.work_folder, "source_description.xml")
        self.xml_text = None
        self.icon_file_name = "icons"
        self.icons_folder = "icon_workfolder"
        self.archive_format = "zip"  
        self.contacts_folder = "com.android.contacts"
        self.incallui_folder = "com.android.incallui"
        self.mms_folder = "com.android.mms"
        self.phone_folder = "com.android.phone"
        self.systemui_folder = "com.android.systemui"
        self.recorder_folder = "com.hihonor.phone.recorder"
        self.telecom_folder = "com.android.server.telecom"
        self.launcher_folder = "com.hihonor.android.launcher"
        self.assets_folder = "assets/"
        self.xmlNameConversionFile = "xmlNameConversions.csv"
        self.folders = [
            "com.android.contacts", 
            "com.android.incallui", 
            "com.android.mms",
            "com.android.phone", 
            "com.android.systemui", 
            "com.hihonor.phone.recorder", 
            "com.android.server.telecom", 
            "com.hihonor.android.launcher"]
        self.keys_mapping = {
            "emui": "magic"    
            }



        
       # Clean up work folder at the start of each app launch
        delete_work_folders(self.contacts_folder, self.icons_folder, self.work_folder, self.launcher_folder, self.telecom_folder, self.recorder_folder, self.systemui_folder, self.phone_folder, self.mms_folder, self.incallui_folder)
        assert os.path.exists(self.contacts_folder) == False, "Delete workfolder failed"
             

    def upload_hwt(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select .hwt file", "", "HWT Files (*.hwt)")
        if file_path:

            # Call the unzip_hwt function from uploadActions.py
            unzip_hwt(file_path, self.work_folder)
            result_text = "Unzipped .hwt file successfully\n"
            
            # Call the rename_files function from uploadActions.py
            rename_files(self.work_folder)
            result_text += "Renamed systen files successfully\n"

            # Resize icon_small.jpg within the preview folder
            resize_icon_small_preview(self.work_folder)
            result_text += f"Overwrote icon_small.jpg with resized image (510x345px)\n" 
                     
            # Unzip icons file within the workfolder with shutil
            unzip_icons(self.work_folder,self.icon_file_name,self.icons_folder, self.archive_format)
            result_text += f"Unzipped '{self.icon_file_name}' file successfully\n"

            # Rename icon files
            rename_icons(self.work_folder,self.icons_folder)
            result_text += f"Renamed icon files successfully\n"
            
            # Zip icon files and all folders within the icon_folder into "icons" file
            zip_icons(self.work_folder,self.icon_file_name,self.icons_folder, self.archive_format)
            result_text += f"Zipped icon files and all folders within the icon_folder into '{self.icon_file_name}' file successfully\n"

            # Delete the icons workfolder from workspace
            delete_icons_file(self.work_folder,self.icon_file_name)
            result_text += f"Deleted '{self.icon_file_name}' file successfully\n"
            

            #remove .zip extension from the file
            remove_icons_zip_extension(self.work_folder,self.icon_file_name,self.archive_format)
            result_text += f"Removed .zip extension from the file successfully\n"

            # Delete icon workspace
            delete_icons_workspace(self.icons_folder)
            result_text += f"Deleted icon workspace successfully\n"
            
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
            
            # Copy the source_description.xml file into the workfolder
            shutil.copyfile("source_description.xml", os.path.join(self.work_folder, "source_description.xml"))

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
                
            self.text_edit.setText(result_text)
            assert self.text_edit.toPlainText() == result_text, "Result text not displayed"

          
            #delete theme.xml file within the workfolder/unlock/ folder and copy source_theme.xml file into the workfolder/unlock/ folder
            delete_and_copy_theme_xml(self.work_folder)
            result_text += f"Deleted theme.xml file within the workfolder/unlock/ folder and copied source_theme.xml file into the workfolder/unlock/ folder successfully\n"
            ##############################################################################################################
            
            
            
            # Unzip files within the workfolder #
            for folder in self.folders:
                unzip_folder(self.work_folder, folder, self.archive_format)
                result_text += f"Unzipped '{folder}' file successfully\n"
            

            # Replace keys in xml files within the workfolder #     
            replace_keys_in_xml_folders(self.folders, self.keys_mapping)
            result_text += f"Replaced keys in xml files within the workfolder successfully\n"
            

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
        

        zip_workfolder(self.work_folder, self.title_edit, self.designer_edit, self.version_edit, self.text_edit)
                
        delete_work_folders(self.contacts_folder, self.icons_folder, self.work_folder, self.launcher_folder, self.telecom_folder, self.recorder_folder, self.systemui_folder, self.phone_folder, self.mms_folder, self.incallui_folder)
        assert os.path.exists(self.contacts_folder) == False, "Delete workfolder failed"
    

if __name__ == "__main__":
    app = QApplication([])
    window = App()
    window.show()
    app.exec()
