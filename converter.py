import os
import shutil
import zipfile
from PIL import Image
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton, QFileDialog,QLabel, QLineEdit
from uploadActions import unzip_hwt, rename_files, unzip_icons, rename_icons, zip_icons, delete_icons_file, remove_icons_zip_extension, delete_icons_workspace
from imageManipulation import resize_icon_small_preview
from xmlmanipluation import read_description_xml, delete_and_copy_theme_xml

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

        # Clean up work folder at the start of each app launch
        self.cleanup_work_folder()

        # Declare variables for save function
        self.work_folder = "workfolder"
        self.source_description_file_path = os.path.join(self.work_folder, "source_description.xml")
        self.xml_text = None
        self.icon_file_name = "icons"
        self.icons_folder = "icon_workfolder"
        self.archive_format = "zip"

    def cleanup_work_folder(self):
        work_folder = "workfolder"
        if os.path.exists(work_folder):
            shutil.rmtree(work_folder)
        if os.path.exists("icon_workfolder"):
            shutil.rmtree("icon_workfolder")

        assert os.path.exists(work_folder) == False
        assert os.path.exists("icon_workfolder") == False
                   

        

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

            
             # Read the description.xml file
            description_file_path = os.path.join(self.work_folder, "description.xml")
            with open(description_file_path, "r", encoding='utf-8') as file:
                xml_text = file.read()

            result_text += f"Read '{description_file_path}'\n"

            assert os.path.exists(description_file_path) == True
            
            # Extract the desired fields from the original description
            import xml.etree.ElementTree as ET
            root = ET.fromstring(xml_text)
            title = root.find(".//title").text            
            brief_info = root.find(".//briefinfo").text

            assert title != None
            assert brief_info != None
            
            # Copy the source_description.xml file into the workfolder
            shutil.copyfile("source_description.xml", os.path.join(self.work_folder, "source_description.xml"))

            result_text += f"Copied 'source_description.xml' into '{self.work_folder}'\n"
            assert os.path.exists(os.path.join(self.work_folder, "source_description.xml")) == True
            
            # Read the source_description.xml file within the workfolder
            self.source_description_file_path = os.path.join(self.work_folder, "source_description.xml")
            with open(self.source_description_file_path, "r") as file:
                self.xml_text = file.read()

            result_text += f"Read '{self.source_description_file_path}'\n"
            assert os.path.exists(self.source_description_file_path) == True
            
            # Extract and display the version and designer from the source_description.xml file
            root = ET.fromstring(self.xml_text)
            designer = root.find(".//designer").text
            version = root.find(".//version").text

            assert designer != None
            assert version != None
                      
            # convert all characters to english
            title = title.encode('ascii', 'ignore').decode('ascii')
            designer = designer.encode('ascii', 'ignore').decode('ascii')
            version = version.encode('ascii', 'ignore').decode('ascii')
            brief_info = brief_info.encode('ascii', 'ignore').decode('ascii')

            result_text += f"Extracted fields from '{description_file_path}'\n"
            assert title != None
            assert designer != None
            assert version != None
            assert brief_info != None

            # Update the GUI fields with the extracted values
            self.title_edit.setText(title)
            self.designer_edit.setText(designer)
            self.version_edit.setText(version)
            self.brief_info_edit.setText(brief_info)
        
            assert self.title_edit.text() == title
            assert self.designer_edit.text() == designer
            assert self.version_edit.text() == version
            assert self.brief_info_edit.toPlainText() == brief_info
                
            self.text_edit.setText(result_text)
            assert self.text_edit.toPlainText() == result_text

            # delete theme.xml file within the workfolder/unlock/ folder
            os.remove(os.path.join(self.work_folder, "unlock/theme.xml"))

            result_text += f"Deleted '{os.path.join(self.work_folder, 'unlock/theme.xml')}'\n"
            assert os.path.exists(os.path.join(self.work_folder, "unlock/theme.xml")) == False

            # copy source_theme.xml file into the workfolder/unlock/ folder
            shutil.copyfile("source_theme.xml", os.path.join(self.work_folder, "unlock/theme.xml"))

            result_text += f"Copied 'source_theme.xml' into '{os.path.join(self.work_folder, 'unlock/theme.xml')}'\n"
            assert os.path.exists(os.path.join(self.work_folder, "unlock/theme.xml")) == True

            
            
           

            
            

    def save(self):
        # Update the description.xml file with the new values
        import xml.etree.ElementTree as ET
        root = ET.fromstring(self.xml_text)
        root.find(".//title").text = self.title_edit.text()
        root.find(".//designer").text = self.designer_edit.text()
        root.find(".//version").text = self.version_edit.text()
        root.find(".//briefInfo").text = self.brief_info_edit.toPlainText()  # Use toPlainText() instead of text()

        assert root.find(".//title").text == self.title_edit.text()
        assert root.find(".//designer").text == self.designer_edit.text()
        assert root.find(".//version").text == self.version_edit.text()
        assert root.find(".//briefInfo").text == self.brief_info_edit.toPlainText()

        # Write the updated description.xml file
        with open(self.source_description_file_path, "w", encoding='utf-8') as file:
            file.write(ET.tostring(root, encoding="utf-8").decode('utf-8'))

        self.text_edit.setText("Saved")
        assert self.text_edit.toPlainText() == "Saved"

        # delete the original description.xml file
        os.remove(os.path.join(self.work_folder, "description.xml"))
        assert os.path.exists(os.path.join(self.work_folder, "description.xml")) == False
        # rename the source_description.xml file to description.xml
        os.rename(self.source_description_file_path, os.path.join(self.work_folder, "description.xml"))
        assert os.path.exists(os.path.join(self.work_folder, "description.xml")) == True
        
        # Zip the workfolder into a .hwt file
        title = self.title_edit.text()
        designer = self.designer_edit.text()
        version = self.version_edit.text()
        hnt_filename = f"{title}_{designer}_{version}.hnt"
        hnt_filepath = os.path.join(os.path.dirname(self.work_folder), hnt_filename)

        with zipfile.ZipFile(hnt_filepath, "w", zipfile.ZIP_DEFLATED) as zip_ref:
            for root, _, files in os.walk(self.work_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    zip_ref.write(file_path, os.path.relpath(file_path, self.work_folder))

        self.text_edit.append(f"Zipped workfolder into '{hnt_filename}'")
        assert os.path.exists(hnt_filepath) == True


        # Delete the workfolder
        shutil.rmtree(self.work_folder)
        assert  os.path.exists(self.work_folder) == False


if __name__ == "__main__":
    app = QApplication([])
    window = App()
    window.show()
    app.exec()
