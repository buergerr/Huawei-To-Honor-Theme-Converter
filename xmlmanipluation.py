import os
import shutil
import zipfile
from PIL import Image

# Read the description.xml file
def read_description_xml(work_folder):
    description_file_path = os.path.join(work_folder, "description.xml")
    with open(description_file_path, "r", encoding='utf-8') as file:
        xml_text = file.read()
    assert os.path.exists(description_file_path) == True
    
# Extract the desired fields from the original description
def extract_fields_from_description_xml(xml_text):
    import xml.etree.ElementTree as ET
    root = ET.fromstring(xml_text)
    title = root.find(".//title").text            
    brief_info = root.find(".//briefinfo").text

    assert title != None
    assert brief_info != None


    
# Copy the source_description.xml file into the workfolder
def copy_source_description_xml(work_folder):
    shutil.copyfile("source_description.xml", os.path.join(work_folder, "source_description.xml"))
    assert os.path.exists(os.path.join(work_folder, "source_description.xml")) == True
    
# Read the source_description.xml file within the workfolder
def read_source_description_xml(work_folder):
    source_description_file_path = os.path.join(work_folder, "source_description.xml")
    with open(source_description_file_path, "r") as file:
        xml_text = file.read()
    assert os.path.exists(source_description_file_path) == True
    
# Extract and display the version and designer from the source_description.xml file
def extract_version_and_designer_from_source_description_xml(xml_text):
    root = ET.fromstring(xml_text)
    designer = root.find(".//designer").text
    version = root.find(".//version").text

    assert designer != None
    assert version != None
                
# convert all characters to english
def convert_all_characters_to_english(work_folder):
    title = title.encode('ascii', 'ignore').decode('ascii')
    designer = designer.encode('ascii', 'ignore').decode('ascii')
    version = version.encode('ascii', 'ignore').decode('ascii')
    brief_info = brief_info.encode('ascii', 'ignore').decode('ascii')

    assert title != None
    assert designer != None
    assert version != None
    assert brief_info != None

# Update the GUI fields with the extracted values
    title_edit.setText(title)
    designer_edit.setText(designer)
    version_edit.setText(version)
    brief_info_edit.setText(brief_info)

    
        
    text_edit.setText(result_text)

# delete theme.xml file within the workfolder/unlock/ folder and copy source_theme.xml file into the workfolder/unlock/ folder
def delete_and_copy_theme_xml(work_folder):
    os.remove(os.path.join(work_folder, "unlock/theme.xml"))
    assert os.path.exists(os.path.join(work_folder, "unlock/theme.xml")) == False, "Delete theme.xml failed"

    shutil.copyfile("source_theme.xml", os.path.join(work_folder, "unlock/theme.xml"))
    assert os.path.exists(os.path.join(work_folder, "unlock/theme.xml")) == True, "Copy source_theme.xml failed"