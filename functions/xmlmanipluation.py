import os
import shutil
import csv
import xml.etree.ElementTree as ET
                

# delete theme.xml file within the workfolder/unlock/ folder and copy source_theme.xml file into the workfolder/unlock/ folder
def delete_and_copy_theme_xml(work_folder):
    os.remove(os.path.join(work_folder, "unlock/theme.xml"))
    assert os.path.exists(os.path.join(work_folder, "unlock/theme.xml")) == False, "Delete theme.xml failed"

    shutil.copyfile("source_theme.xml", os.path.join(work_folder, "unlock/theme.xml"))
    assert os.path.exists(os.path.join(work_folder, "unlock/theme.xml")) == True, "Copy source_theme.xml failed"

# The following function is used to unzip the files within the workfolder
def unzip_folder(work_folder, folder_name, archive_format):
    folder_path = os.path.join(work_folder, folder_name)
    shutil.unpack_archive(folder_path, folder_name, archive_format)
    assert os.path.exists(folder_name), f"Unzip {folder_name} failed"


# open /assets/xmlNameConversion.csv file and read the file and create a dictionary
def read_xmlNameConversion(assets_folder, xmlNameConversionFile):
    xmlNameConversion = os.path.join(assets_folder + xmlNameConversionFile)
    assert os.path.exists(xmlNameConversion) == True, "xmlNameConversion.csv not found"
    print(xmlNameConversion)

    # Read the xmlNameConversion.csv file and create a dictionary
    with open(xmlNameConversion, mode='r') as infile:
        reader = csv.reader(infile)
        for rows in reader:
            xmlNameConversion_dict = {rows[0]:rows[1]}
    
    print(xmlNameConversion_dict)

    return xmlNameConversion_dict


# iterate through the xml and replace the name of the resource with keys_mapping
def replace_keys_in_xml(file_path, keys_mapping):
    tree = ET.parse(file_path)
    root = tree.getroot()
    for resources_elem in root.iter("resources"):
        for color_elem in resources_elem.iter("color"):
            for key in keys_mapping:
                if color_elem.attrib.get("name") == key:
                    color_elem.attrib["name"] = keys_mapping[key]
    tree.write(file_path)





def replace_keys_in_xml_folders(folders, keys_mapping):
    for folder in folders:
        folder_path = os.path.join(os.getcwd(), folder)
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".xml"):
                    file_path = os.path.join(root, file)
                    replace_keys_in_xml(file_path, keys_mapping)
                    


