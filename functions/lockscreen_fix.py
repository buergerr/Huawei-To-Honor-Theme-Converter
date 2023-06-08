import os
import xml.etree.ElementTree as ET




# open the manifest.xml file in workfolder/unlock/lockscreen manifest.xml and replace any value for format with "EEEE, MMMM dd"
# use ElementTree to parse the xml file
def update_datetime_format_in_manifest(work_folder):
    manifest_path = os.path.join(work_folder, "unlock/lockscreen/manifest.xml")
    tree = ET.parse(manifest_path)
    root = tree.getroot()

    for element in root.iter("DateTime"):
        element.set("format", "EEEE, MMMM dd")

    tree.write(manifest_path)
    assert element.attrib["format"] == "EEEE, MMMM dd", "Update string in manifest failed"
    


# read the manifest.xml file in workfolder/unlock/lockscreen manifest.xml and check if the formate is equal to "EEEE, MMMM dd"
# MMMM dd EEEE is part of <DateTime color="#0B4C6B" size="50" x="148" y="652" format="MMMM dd EEEE" />
# use ElementTree to parse the xml file
# if not equal, raise an exception
# if missing the format, then add the format attribute and set the value to "EEEE, MMMM dd"
def add_datetime_format_in_manifest(work_folder):
    manifest_path = os.path.join(work_folder, "unlock/lockscreen/manifest.xml")
    tree = ET.parse(manifest_path)
    root = tree.getroot()

    format_exists = False
    for element in root.iter("DateTime"):
        format_attr = element.attrib.get("format")
        if format_attr == "EEEE, MMMM dd":
            format_exists = True
            break
    
    if not format_exists:
        datetime_element = root.find("DateTime")
        datetime_element.set("format", "EEEE, MMMM dd")
        tree.write(manifest_path)
        assert datetime_element.attrib["format"] == "EEEE, MMMM dd", "Add string in manifest failed"

