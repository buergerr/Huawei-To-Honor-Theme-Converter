import os
import xml.etree.ElementTree as ET




# open the manifest.xml file in workfolder/unlock/lockscreen manifest.xml and replace the value "MMMM dd EEEE" with "EEEE, MMMM dd"
# MMMM dd EEEE is part of <DateTime color="#0B4C6B" size="50" x="148" y="652" format="MMMM dd EEEE" />
# use ElementTree to parse the xml file

def update_datetime_format_in_manifest(work_folder):
    manifest_path = os.path.join(work_folder, "unlock/lockscreen/manifest.xml")
    tree = ET.parse(manifest_path)
    root = tree.getroot()
    for element in root.iter("DateTime"):
        format_attr = element.attrib.get("format")
        if format_attr == "MMMM dd EEEE":
            element.attrib["format"] = "EEEE, MMMM dd"
            assert element.attrib["format"] == "EEEE, MMMM dd", "Replace string in manifest failed"
    tree.write(manifest_path)