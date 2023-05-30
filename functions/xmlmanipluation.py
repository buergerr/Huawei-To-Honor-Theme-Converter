import os
import shutil
import csv
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom # for xml validation
                

# delete theme.xml file within the workfolder/unlock/ folder and copy source_theme.xml file into the workfolder/unlock/ folder
def delete_and_copy_theme_xml(work_folder):
    os.remove(os.path.join(work_folder, "unlock/theme.xml"))
    assert os.path.exists(os.path.join(work_folder, "unlock/theme.xml")) == False, "Delete theme.xml failed"

    shutil.copyfile(os.path.join("assets/xml/source_theme.xml"), os.path.join(work_folder, "unlock/theme.xml"))
    assert os.path.exists(os.path.join(work_folder, "unlock/theme.xml")) == True, "Copy source_theme.xml failed"

# The following function is used to unzip the files within the workfolder
def unzip_folder(work_folder, folder_name, archive_format):
    folder_path = os.path.join(work_folder, folder_name)
    shutil.unpack_archive(folder_path, folder_name, archive_format)
    assert os.path.exists(folder_name), f"Unzip {folder_name} failed"

# The following function will delete the files within the workfolder. the files are specified in the folders list
def delete_original_files(work_folder, folders):
    for file in folders:
        file_path = os.path.join(work_folder, file)
        os.remove(file_path)
        assert os.path.exists(file_path) == False, f"Delete {file} failed"

# iterate through the xml and replace the name of the resource with keys_mapping
def replace_keys_in_xml(file_path, keys_mapping):
    tree = ET.parse(file_path)
    root = tree.getroot()
    for resources_elem in root.iter("resources"):
        for color_elem in resources_elem.iter("color"):
            name_attr = color_elem.attrib.get("name")
            for old_value, new_value in keys_mapping.items():
                name_attr = name_attr.replace(old_value, new_value)
            color_elem.attrib["name"] = name_attr
            assert color_elem.attrib["name"] == name_attr, "Replace keys in xml failed"
    tree.write(file_path)

# create a function that changes the key "<HWTheme>" to "<HNTheme>" withinn the xml file within the folders
def replace_hwtheme_with_hntheme(folders):
    for folder in folders:
        folder_path = os.path.join(os.getcwd(), folder)
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".xml"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "r+") as f:
                        content = f.read()
                        updated_content = content.replace("HWTheme", "HNTheme")
                        f.seek(0)
                        f.write(updated_content)
                        f.truncate()
                        assert os.path.exists(file_path) == True, "Replace HWTheme with HNTheme failed"


# iterate through the xml files within the folders and replace the name of the resource with keys_mapping
def replace_keys_in_xml_folders(folders, keys_mapping):
    for folder in folders:
        folder_path = os.path.join(os.getcwd(), folder)
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".xml"):
                    file_path = os.path.join(root, file)
                    replace_keys_in_xml(file_path, keys_mapping)
                    assert os.path.exists(file_path) == True, "Replace keys in xml files failed"

# validate the xml files within the folders and terminate the program if the xml is not valid
def validate_xml_files(folders):
    for folder in folders:
        folder_path = os.path.join(os.getcwd(), folder)
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".xml"):
                    file_path = os.path.join(root, file)
                    dom = minidom.parse(file_path)
                    if dom.documentElement.nodeName == "parsererror":
                        print(f"Invalid xml file: {file_path}")
                        exit(1)
                    assert dom.documentElement.nodeName != "parsererror", "Invalid xml file"

 # clean empty lines in the xml files within the folders
def clean_empty_lines_in_xml_files(folders):
    for folder in folders:
        folder_path = os.path.join(os.getcwd(), folder)
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".xml"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "r+") as f:
                        lines = f.readlines()
                        f.seek(0)
                        f.writelines(line for line in lines if line.strip())
                        f.truncate()
                        assert os.path.exists(file_path) == True, "Clean empty lines in xml files failed"

# rename folders within the folders. If folder name is "framework-res-hwext", rename it to "framework-res-hnext"
def rename_framework_folders(folders):
    for folder in folders:
        folder_path = os.path.join(os.getcwd(), folder)
        for root, dirs, _ in os.walk(folder_path):
            for dir in dirs:
                if dir == "framework-res-hwext":
                    old_folder = os.path.join(root, dir)
                    new_folder = os.path.join(root, "framework-res-hnext")
                    os.rename(old_folder, new_folder)
                    assert os.path.exists(new_folder) == True, "Rename 'framework-res-hwext' failed"

# zip the folders abd move the zip file to the workfolder
def zip_folders(folders, archive_format):
    for folder in folders:
        folder_path = os.path.join(os.getcwd(), folder)
        shutil.make_archive(folder_path, archive_format, folder_path)
        assert os.path.exists(folder_path + "." + archive_format) == True, f"Zip {folder} failed"
        shutil.move(folder_path + "." + archive_format, os.path.join(os.getcwd(), "workfolder"))

# remove zip extension from the zip files within the workfolder
def remove_zip_extension_from_zip_files(work_folder,folders,archive_format):
    os.rename(os.path.join(work_folder, folders + "." + archive_format), os.path.join(work_folder, folders))
    assert os.path.exists(os.path.join(work_folder, folders + "." + archive_format)) == False, "Remove Zip from Icons.zip failed"   

# delete the folders
def delete_folders(folders):
    for folder in folders:
        folder_path = os.path.join(os.getcwd(), folder)
        shutil.rmtree(folder_path)
        assert os.path.exists(folder_path) == False, f"Delete {folder} failed"























                    