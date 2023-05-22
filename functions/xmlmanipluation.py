import os
import shutil
import zipfile
from PIL import Image

                

# delete theme.xml file within the workfolder/unlock/ folder and copy source_theme.xml file into the workfolder/unlock/ folder
def delete_and_copy_theme_xml(work_folder):
    os.remove(os.path.join(work_folder, "unlock/theme.xml"))
    assert os.path.exists(os.path.join(work_folder, "unlock/theme.xml")) == False, "Delete theme.xml failed"

    shutil.copyfile("source_theme.xml", os.path.join(work_folder, "unlock/theme.xml"))
    assert os.path.exists(os.path.join(work_folder, "unlock/theme.xml")) == True, "Copy source_theme.xml failed"