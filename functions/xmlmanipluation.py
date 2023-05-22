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

##############################################################################################################
# The following functions are used to unzip the files within the workfolder
# Unzip com.android.contacts file within the workfolder with shutil
def unzip_contacts(work_folder,contacts_folder,archive_format):    
    shutil.unpack_archive(os.path.join(work_folder, contacts_folder), contacts_folder, archive_format)
    assert os.path.exists(contacts_folder) == True, "Unzip contacts failed"

# unzip com.android.incallui file within the workfolder with shutil
def unzip_incallui(work_folder,incallui_folder,archive_format):
    shutil.unpack_archive(os.path.join(work_folder, incallui_folder), incallui_folder, archive_format)
    assert os.path.exists(incallui_folder) == True, "Unzip incallui failed"

# unzip com.android.mms file within the workfolder with shutil
def unzip_mms(work_folder,mms_folder,archive_format):
    shutil.unpack_archive(os.path.join(work_folder, mms_folder), mms_folder, archive_format)
    assert os.path.exists(mms_folder) == True, "Unzip mms failed"

# unzip com.android.phone file within the workfolder with shutil
def unzip_phone(work_folder,phone_folder,archive_format):
    shutil.unpack_archive(os.path.join(work_folder, phone_folder), phone_folder, archive_format)
    assert os.path.exists(phone_folder) == True, "Unzip phone failed"


#unzip com.android.systemui file within the workfolder with shutil
def unzip_systemui(work_folder,systemui_folder,archive_format):
    shutil.unpack_archive(os.path.join(work_folder, systemui_folder), systemui_folder, archive_format)
    assert os.path.exists(systemui_folder) == True, "Unzip systemui failed"

#unzip com.android.phone.recorder file within the workfolder with shutil
def unzip_recorder(work_folder,recorder_folder,archive_format):
    shutil.unpack_archive(os.path.join(work_folder, recorder_folder), recorder_folder, archive_format)
    assert os.path.exists(recorder_folder) == True, "Unzip recorder failed"

# unzip com.android.server.telecom file within the workfolder with shutil
def unzip_telecom(work_folder,telecom_folder,archive_format):
    shutil.unpack_archive(os.path.join(work_folder, telecom_folder), telecom_folder, archive_format)
    assert os.path.exists(telecom_folder) == True, "Unzip telecom failed"

# unzip com.hihonor.android.launcher file within the workfolder with shutil
def unzip_launcher(work_folder,launcher_folder,archive_format):
    shutil.unpack_archive(os.path.join(work_folder, launcher_folder), launcher_folder, archive_format)
    assert os.path.exists(launcher_folder) == True, "Unzip launcher failed"

##############################################################################################################

