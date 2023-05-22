import os
import shutil
import zipfile
from PIL import Image


# Unzip .hwt file into work folder   
def unzip_hwt(file_path, work_folder):
           
    os.makedirs(work_folder, exist_ok=True)
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(work_folder)
            
    assert os.path.exists(work_folder) == True, "Unzip failed"
   

# Rename files
def rename_files(work_folder):
    old_launcher_path = os.path.join(work_folder, "com.huawei.android.launcher")
    new_launcher_path = os.path.join(work_folder, "com.hihonor.android.launcher")
    os.rename(old_launcher_path, new_launcher_path)

    old_recorder_path = os.path.join(work_folder, "com.huawei.phone.recorder")
    new_recorder_path = os.path.join(work_folder, "com.hihonor.phone.recorder")
    os.rename(old_recorder_path, new_recorder_path)

    assert os.path.exists(new_launcher_path) == True, "Rename failed"
    assert os.path.exists(new_recorder_path) == True, "Rename failed"




# Unzip icons file within the workfolder with shutil
def unzip_icons(work_folder,icon_file_name,icons_folder,archive_format):    
    shutil.unpack_archive(os.path.join(work_folder, icon_file_name), icons_folder, archive_format)
    assert os.path.exists(icons_folder) == True, "Unzip icons failed"

# Zip icon files and all folders within the icon_folder into "icons" file
def zip_icons(work_folder,icon_file_name,icons_folder, archive_format):
    shutil.make_archive(os.path.join(work_folder, icon_file_name), archive_format, icons_folder)    
    assert os.path.exists(os.path.join(work_folder, icon_file_name + "." + archive_format)) == True, "Zip icons failed"



# Rename icon files
def rename_icons(work_folder,icons_folder):
    for filename in os.listdir(icons_folder):
        if filename.startswith("com.huawei"):
            old_filename = os.path.join(icons_folder, filename)
            new_filename = os.path.join(icons_folder, filename.replace("com.huawei", "com.hihonor"))
            os.rename(old_filename, new_filename)
            assert os.path.exists(new_filename) == True, "Rename Icons huwei to hihonor failed"

# rename folder within icons folder /dynamic_icons/com.huawei.android.totemweather to /dynamic_icons/com.hihonor.android.totemweather
    old_folder = os.path.join(icons_folder, "dynamic_icons/com.huawei.android.totemweather")
    new_folder = os.path.join(icons_folder, "dynamic_icons/com.hihonor.android.totemweather")
    os.rename(old_folder, new_folder)
    assert os.path.exists(new_folder) == True, "Rename 'totemweather'failed"

# rename folder within icons folder com.android.deskclock OR com.huawei.deskclock to /dynamic_icons/com.hihonor.deskclock
    old_folder = os.path.join(icons_folder, "dynamic_icons/com.android.deskclock")
    new_folder = os.path.join(icons_folder, "dynamic_icons/com.hihonor.deskclock")
    if os.path.exists(old_folder):
        os.rename(old_folder, new_folder)        
    else:
        old_folder = os.path.join(icons_folder, "dynamic_icons/com.huawei.deskclock")
        os.rename(old_folder, new_folder)            
        assert os.path.exists(new_folder) == True, "Rename 'deskclock' failed"



# delete original icon file
def delete_icons_file (work_folder,icon_file_name):      
    os.remove(os.path.join(work_folder, icon_file_name))
    assert os.path.exists(os.path.join(work_folder, icon_file_name)) == False, "Delete icon file failed"

#remove .zip extension from the file
def remove_icons_zip_extension(work_folder,icon_file_name,archive_format):
    os.rename(os.path.join(work_folder, icon_file_name + "." + archive_format), os.path.join(work_folder, icon_file_name))
    assert os.path.exists(os.path.join(work_folder, icon_file_name + "." + archive_format)) == False, "Remove Zip from Icons.zip failed"        

# Delete icon workspace
def delete_icons_workspace(icons_folder):
    shutil.rmtree(icons_folder)
    assert os.path.exists(icons_folder) == False, "Delete failed"