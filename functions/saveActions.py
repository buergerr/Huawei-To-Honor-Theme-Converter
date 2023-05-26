import os
import shutil
import zipfile
from PIL import Image
import xml.etree.ElementTree as ET


# delete the original description.xml file
def delete_description_xml(work_folder):
        os.remove(os.path.join(work_folder, "description.xml"))
        assert os.path.exists(os.path.join(work_folder, "description.xml")) == False

# rename the source_description.xml file to description.xml
def rename_description_xml(work_folder, source_description_file_path):
        
        os.rename(source_description_file_path, os.path.join(work_folder, "description.xml"))
        assert os.path.exists(os.path.join(work_folder, "description.xml")) == True



# Zip the workfolder into a .hwt file
def zip_workfolder(work_folder, title_edit, designer_edit, version_edit, text_edit):
        title = title_edit.text()
        designer = designer_edit.text()
        version = version_edit.text()
        hnt_filename = f"{title}_{designer}_{version}.hnt"
        hnt_filepath = os.path.join(os.path.dirname(work_folder), hnt_filename)

        with zipfile.ZipFile(hnt_filepath, "w", zipfile.ZIP_DEFLATED) as zip_ref:
            for root, _, files in os.walk(work_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    zip_ref.write(file_path, os.path.relpath(file_path, work_folder))

        text_edit.append(f"Zipped workfolder into '{hnt_filename}'")
        assert os.path.exists(hnt_filepath) == True

        # Zip the workfolder into a .hwt file
def zip_workfolder466(work_folder, title_edit, designer_edit, version_edit, text_edit):
        title = title_edit.text()
        designer = designer_edit.text()
        version = version_edit.text()
        hnt_filename = f"{title}_{designer}_{version}_466.hnt"
        hnt_filepath = os.path.join(os.path.dirname(work_folder), hnt_filename)

        with zipfile.ZipFile(hnt_filepath, "w", zipfile.ZIP_DEFLATED) as zip_ref:
            for root, _, files in os.walk(work_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    zip_ref.write(file_path, os.path.relpath(file_path, work_folder))

        text_edit.append(f"Zipped workfolder into '{hnt_filename}'")
        assert os.path.exists(hnt_filepath) == True


        # Zip the workfolder into a .hwt file
def zip_workfolder194(work_folder, title_edit, designer_edit, version_edit, text_edit):
        title = title_edit.text()
        designer = designer_edit.text()
        version = version_edit.text()
        hnt_filename = f"{title}_{designer}_{version}_194.hnt"
        hnt_filepath = os.path.join(os.path.dirname(work_folder), hnt_filename)

        with zipfile.ZipFile(hnt_filepath, "w", zipfile.ZIP_DEFLATED) as zip_ref:
            for root, _, files in os.walk(work_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    zip_ref.write(file_path, os.path.relpath(file_path, work_folder))

        text_edit.append(f"Zipped workfolder into '{hnt_filename}'")
        assert os.path.exists(hnt_filepath) == True